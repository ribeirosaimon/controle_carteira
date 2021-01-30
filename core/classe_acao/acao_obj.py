from .acao.calculos import *

class Carteira:
    
    def reset_carteira(self):
        self.portfolio = list()
        self.vendas = list()
        self.caixa_br = list()
        self.caixa_usa = list()
        self.info_portfolio = list()
        self.posicao_usa = list()
        self.posicao_br = list()
        self.info_vendas = list()

    def inicializar_carteira(self):
        for acoes in self.portfolio:
            if acoes['acao'] == 'caixa':
                pass
            else:
                info_acao = info_das_acoes(acoes['acao'], acoes['nacional'])
                self.info_portfolio.append(info_acao)

    def portfolio_carteira(self):
        return self.portfolio

    def relatorio_vendas(self):
        return self.vendas
    
    def info_caixa(self, dolar):
        peso = self.patrimonio(dolar)
        caixa_br = {'caixa_br':round(sum(self.caixa_br),2),
                    'peso':round(sum(self.caixa_br)/peso,5)}
        caixa_usa = {'caixa_usa':round(sum(self.caixa_usa) * dolar,2),
                    'peso':round((sum(self.caixa_usa) * dolar) / peso,5)}
        return [caixa_br, caixa_usa]

    def caixa(self, valor, nacional):
        if nacional == True:
            self.caixa_br.append(valor)
            return round(sum(self.caixa_br),2)
        else:
            self.caixa_usa.append(valor)
            return round(sum(self.caixa_usa),2)



    def comprar(self, acao, pm, qtd, nacional, data):
        if len(self.portfolio) == 0:
            dicionario = {
                'acao':acao,
                'pm':pm,
                'qtd':qtd,
                'nacional':nacional,
                'data_compra':data
            }
            self.portfolio.append(dicionario)
        else:
            if acao in [x['acao'] for x in self.portfolio]:
               for valores in self.portfolio:
                   if valores['acao'] == acao:
                        valores['pm'] = calculo_preco_medio(valores['pm'],valores['qtd'],pm,qtd)
                        valores['qtd'] = valores['qtd'] + qtd
            else:
                dicionario = {
                    'acao':acao,
                    'pm':pm,
                    'qtd':qtd,
                    'nacional':nacional,
                    'data_compra':data
                }
                self.portfolio.append(dicionario)


    def vender(self, acao, pv, pm_acao, qtd, data, nacional=True, dolar=0):
        for valores in self.portfolio:
            if acao not in [x['acao'] for x in self.portfolio]:
                erro = {'error':'Você não tem essa ação'}
                return erro
        dicionario = {
            'acao':acao,
            'preco_venda':pv,
            'preco_medio':pm_acao,
            'qtd':qtd,
            'nacional':nacional,
            'data_venda':data
        }
        if nacional == False:
            dicionario['dolar'] = dolar
        self.vendas.append(dicionario)
        return True

    def patrimonio(self, dolar, nacional=None, usdbrl=True):
        todo_patrimonio = []
        patrimonio_separado = []
        soma_caixa_br = sum(self.caixa_br)
        soma_caixa_usa = sum(self.caixa_usa) * dolar
        for acao in self.portfolio:
            preco = preco_acao(acao['acao'], self.info_portfolio)
            posicao = preco * acao['qtd']
            if acao['nacional'] == False:
                posicao = posicao * dolar
            todo_patrimonio.append(posicao)
            preco = preco_acao(acao['acao'], self.info_portfolio)
            posicao = preco * acao['qtd']
            if nacional == True:
                if acao['nacional'] == True:
                    patrimonio_separado.append(posicao)
            if nacional == False:
                if acao['nacional'] == False:
                    patrimonio_separado.append(posicao)
        if nacional == True:
            soma = sum(patrimonio_separado)
            soma = soma + soma_caixa_br
            return round(soma,2)
        if nacional == False:
            soma = sum(patrimonio_separado)
            soma = soma + soma_caixa_usa
            if usdbrl == True:
                soma = soma * dolar
            return round(soma,2)
        soma = sum(todo_patrimonio)
        soma = soma + soma_caixa_br + soma_caixa_usa
        return round(soma,2)

    def lucro_carteira(self,dolar,acao=None,nacional=None):
        acao_separada = []
        todas_acoes = []
        usa_acao = []
        br_acao = []
        for valores in self.portfolio:
            patrimonio = preco_acao(valores['acao'], self.info_portfolio) * valores['qtd']
            custo = valores['pm'] * valores['qtd']
            lucro = patrimonio - custo
            if nacional == False:
                lucro = lucro * dolar
                usa_acao.append(lucro)
            if nacional == True:
                br_acao.append(lucro)
            if acao == valores['acao']:
                acao_separada.append(lucro)
            todas_acoes.append(lucro)
        if acao == None:
            if nacional == None:
                return round(sum(todas_acoes),2)
            if nacional == True:
                return round(sum(br_acao),2)
            if nacional == False:
                return round(sum(usa_acao),2)
        if acao != None:
            return round(sum(acao_separada),2)


    def retorno(self, dolar, acao=None):
        posicao_total = []
        custo_total = []
        posicao_de_acao_separada = []
        custo_de_acao_separada = []

        for valores in self.portfolio:
            posicao = preco_acao(valores['acao'], self.info_portfolio) * valores['qtd']
            custo = valores['pm'] * valores['qtd']
            if valores['nacional'] == False:
                posicao = posicao * dolar
                custo = custo * dolar
            posicao_total.append(posicao)
            custo_total.append(custo)
            if acao != None:    
                if acao == valores['acao']:
                    posicao_de_acao_separada.append(posicao)
                    custo_de_acao_separada.append(custo)
        if acao != None:
            calculo_separado = round((sum(posicao_de_acao_separada) / sum(custo_de_acao_separada)) - 1,4)
            return calculo_separado
        calculo = round((sum(posicao_total) / sum(custo_total)) - 1,4)
        return calculo

    def peso_da_carteira(self, dolar, acao, lista_caixa):
        lista_posicao = []
        patrimonio = self.patrimonio(dolar)
        for valores in self.portfolio:
            if valores['acao'] == acao:
                posicao = preco_acao(valores['acao'], self.info_portfolio) * valores['qtd']
                if valores['nacional'] == False:
                    posicao = posicao * dolar
                lista_posicao.append(posicao)
        soma_posicao = sum(lista_posicao)
        return round(soma_posicao / patrimonio,5)

    def posicao(self, dolar, acao):
        for valores in self.portfolio:
            if valores['acao'] == acao:
                posicao = preco_acao(valores['acao'], self.info_portfolio) * valores['qtd']
                if valores['nacional'] == False:
                    posicao = posicao * dolar
        return posicao

    def preco_medio(self, acao):
        for valores in self.portfolio:
            if valores['acao'] == acao:
                return valores['preco_medio']

    def media_movel_expodencial(self, acao, tempo=20):
        fechamentos = []
        compra = False
        for valores in self.info_portfolio:
            if acao == valores['acao']:
                for index in range(0,tempo):
                    fechamento = valores['info'][index]['dados']['close']
                    fechamentos.append(fechamento)
        mma = sum(fechamentos) / tempo
        close = fechamentos[0]
        if close < mma:
            compra = True
        dict_mma = {'mma':{'buy':compra}}
        return dict_mma

    def topo_fundo(self, acao, tempo=2):
        contador_max, contador_min = 0,0
        resultado = [x['info'][0]['dados'] for x in self.info_portfolio if x['acao']== acao]
        candle_referencia = {'minima':resultado[0]['min'],'maxima':resultado[0]['max']}
        indicador = {'top':['None',0],'bottom':['None',0]}
        for valores in self.info_portfolio:
            if acao == valores['acao']:
                for dados in valores['info'][::-1]:
                    minimas = dados['dados']['min']
                    maximas = dados['dados']['max']
                    if maximas > candle_referencia['maxima']:
                        if contador_max < 2:
                            contador_max += 1
                        if contador_max >= 2:
                            contador_max += 1
                            contador_min = 0
                            candle_referencia['maxima'] = maximas
                            candle_referencia['minima'] = minimas
                            indicador['top'][0] = True
                            indicador['top'][1] = candle_referencia['maxima']
                            indicador['bottom'][0] = False

                    if minimas < candle_referencia['minima']:
                        if contador_min < 2:
                            contador_min += 1
                        if contador_min >= 2:
                            contador_min += 1
                            contador_max = 0
                            candle_referencia['maxima'] = maximas
                            candle_referencia['minima'] = minimas
                            indicador['top'][0] = False
                            indicador['bottom'][1] = candle_referencia['minima']
                            indicador['bottom'][0] = True
        return indicador

    def indicador_hilo(self,acao, candles=3):
        minimas, maximas =[], []
        fechamento = [x['info'][0]['dados']['close'] for x in self.info_portfolio if x['acao']== acao][0]
        for valores in self.info_portfolio:
            if acao == valores['acao']:
                for index in range(candles):
                    minima = valores['info'][index]['dados']['min']
                    maxima = valores['info'][index]['dados']['max']
                    minimas.append(minima)
                    maximas.append(maxima)

        mma_minima = round(sum(minimas) / 3,2)
        mma_maxima = round(sum(maximas)/3,2)
        dict_hilo = {'hilo':'none'}
        if fechamento < mma_minima:
            dict_hilo['hilo'] = 'buy'
        if fechamento > mma_maxima:
            dict_hilo['hilo'] = 'sell'
        return dict_hilo


    def bandas_de_bolinger(self,acao,tempo=20):
        fechamentos,lista_quadrados = [],[]
        dict_bolinger = {'bollinger':'None',
                         'dados':{'top':0,
                                  'bottom':0}}
        fechamento = [x['info'][0]['dados']['close'] for x in self.info_portfolio if x['acao']== acao][0] 
        for valores in self.info_portfolio:
            if acao == valores['acao']:
                for index in range(0,tempo):
                    fechamento = valores['info'][index]['dados']['close']
                    fechamentos.append(fechamento)
        mma = sum(fechamentos) / tempo
        for x in range(tempo):
            calculo = (mma - fechamentos[x]) ** 2
            lista_quadrados.append(calculo)
        desvio_padrao = (sum(lista_quadrados) / tempo) **0.5
        banda_superior = round(mma + (desvio_padrao * 2),2)
        banda_inferior = round(mma - (desvio_padrao * 2),2)
        if fechamento < banda_inferior:
            dict_bolinger['bollinger'] = 'buy'
        if fechamento > banda_superior:
            dict_bolinger['bollinger'] = 'sell'
        dict_bolinger['dados']['top'] = banda_superior
        dict_bolinger['dados']['bottom'] = banda_inferior
        return dict_bolinger

        #rsi
    def rsi(self,acao, tempo=14, min_ifr=30, max_ifr=70):
        media_ganho, media_perda = [],[]
        for valores in self.info_portfolio:
            if acao == valores['acao']:
                for index in range(0,tempo):
                    fechamento = valores['info'][index]['dados']['close']
                    abertura = valores['info'][index]['dados']['open']
                    calculo = abs(fechamento - abertura)
                    if fechamento > abertura:
                        media_ganho.append(calculo)
                    if fechamento < abertura:
                        media_perda.append(calculo)
        fr = (sum(media_ganho) / tempo) / (sum(media_perda) / tempo)
        ifr = round(100 - (100/(1+fr)),2)
        dict_ifr = {'ifr':ifr,'dados':'none'}
        if ifr < min_ifr:
            dict_ifr['dados'] = 'buy'
        if ifr > max_ifr:
            dict_ifr['dados'] = 'sell'
        return dict_ifr

    def avg_vol(self,acao):
        avg_vol = []
        volume_diario = [x['info'][0]['dados']['volume'] for x in self.info_portfolio if x['acao']== acao][0]
        for valores in self.info_portfolio:
            if acao == valores['acao']:
                for dados in valores['info']:
                    volume = dados['dados']['volume']
                    avg_vol.append(volume)
        volume_medio = int(round(sum(avg_vol)/len(avg_vol),0))
        return calculo_de_volume(volume_medio,volume_diario)
