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


    def vender(self, acao, pv, qtd, data, nacional=True, dolar=0):
        for valores in self.portfolio:
            if valores['acao'] == acao:
                if valores['qtd'] - qtd >= 0:
                    pm_acao = valores['pm']
                    valores['qtd'] = valores['qtd'] - qtd
                    valores['data_venda'] = data
                    if nacional == False:
                        valores['dolar'] = dolar
                    if valores['qtd'] == 0:
                        self.portfolio.remove(valores)
                else:
                    erro = {'error':f'Quantidade da ação {valores["acao"]} não pode ser menor que 0'}
                    return erro
            elif acao not in [x['acao'] for x in self.portfolio]:
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

    def peso_da_carteira(self, dolar, acao=None, caixa=None, nacional=None):
        dicionario_retorno = []
        dicionario_completo = []
        dicionario_caixa = []
        patrimonio = self.patrimonio()
        calculo_caixa_usa = round((sum(self.caixa_usa) * dolar) / patrimonio,5)
        calculo_caixa_br = round(sum(self.caixa_br) / patrimonio,5)
        calculo_caixa_total = round((sum(self.caixa_br) + (sum(self.caixa_usa)* dolar)) / patrimonio,5)
        if caixa == True:     
            if nacional == True:
                dicionario_caixa.append({'caixa_br':calculo_caixa_br})
                return dicionario_caixa
            if nacional == False:
                dicionario_caixa.append({'caixa_usa':calculo_caixa_usa})
                return dicionario_caixa
            dicionario_caixa.append({'caixa_total':calculo_caixa_total})
            return dicionario_caixa
        for valores in self.portfolio:
            posicao = preco_acao(valores['acao'], self.info_portfolio) * valores['qtd']
            if valores['nacional'] == False:
                posicao = posicao * dolar
            peso = posicao / patrimonio
            retorno = {'acao':valores['acao'],'peso':round(peso,4)}
            dicionario_completo.append(retorno)
            if valores['acao'] == acao:
                dicionario_retorno.append(retorno)     
                return dicionario_retorno
        dicionario_caixa = {'acao':'caixa',
                            'peso':calculo_caixa_total}
        dicionario_completo.append(dicionario_caixa)
        return dicionario_completo

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
