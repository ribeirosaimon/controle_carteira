class Imposto_de_renda:
    def isencao_ir(self, lista):
        isencao_do_ir_br = [19999.99, ]
        isencao_do_ir_usa = [34999.99, ]
        for x in lista:
            valor_total = float(x.preco_medio * x.quantidade)
            if x.nacional == True:
                isencao_do_ir_br.append(-valor_total) 
            if x.nacional == False:
                isencao_do_ir_usa.append(-valor_total)
        isencao_br = sum(isencao_do_ir_br)
        isencao_usa = sum(isencao_do_ir_usa)
        if isencao_br < 0:
            isencao_br = 0
        if isencao_usa < 0:
            isencao_usa = 0
        dict_retorno = {'ir_br':isencao_br,
                        'ir_usa':isencao_usa}
        return dict_retorno