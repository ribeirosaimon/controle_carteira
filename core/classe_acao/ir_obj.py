class Imposto_de_renda:
    def isencao_ir(self, lista,dolar):
        isencao_do_ir_br = [19999.99, ]
        isencao_do_ir_usa = [34999.99, ]
        isento_br, isento_usa = True, True
        for x in lista:
            valor_total = float(x.preco_venda * x.quantidade)
            if x.nacional == True:
                isencao_do_ir_br.append(-valor_total) 
            if x.nacional == False:
                valor_total = valor_total*dolar
                isencao_do_ir_usa.append(-valor_total)

        isencao_br = round(sum(isencao_do_ir_br),2)
        isencao_usa = round(sum(isencao_do_ir_usa),2)
        if isencao_br < 0:
            isencao_br = 0
            isento_br = False
        if isencao_usa < 0:
            isencao_usa = 0
            isento_usa = False
        dict_retorno = {'vendas_isento':[{'isento_br':isento_br,'isento_usa':isento_usa},{'isencao_br':isencao_br,'isencao_usa':isencao_usa}]}
        return dict_retorno


    def ir_devido(self, relatorio_vendas):
        lucro_br, lucro_usa = [],[]
        for vendas in relatorio_vendas:
            dolar = vendas['dolar']
            lucro = (vendas['preco_venda'] - vendas['preco_medio']) * vendas['qtd']
            if vendas['nacional'] == False:
                lucro = lucro * dolar
                lucro_usa.append(lucro)
            if vendas['nacional'] == True:
                lucro_br.append(lucro)
            ir_br = round(sum(lucro_br) * 0.15,2)
            ir_usa = round(sum(lucro_usa)*0.15,2)
            dict_lucro = {'ir_br':ir_br,
                          'ir_usa':ir_usa}
        return dict_lucro
