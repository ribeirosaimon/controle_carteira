from core.classe_acao.acao_obj import Carteira

def info_carteira(portfolio, dolar, caixa):
    carteira = portfolio.portfolio_carteira()
    info_portfolio = []
    for acao in carteira:
        retorno_acao = portfolio.retorno(dolar,acao['acao'])
        lucro_acao = portfolio.lucro_carteira(dolar,acao['acao'],acao['nacional'])
        posicao_na_carteira = round(portfolio.posicao(dolar,acao['acao']),2)
        peso_acao = portfolio.peso_da_carteira(dolar, acao=acao['acao'],caixa)
        dict_info = {'acao':acao['acao'],
                    'info':{
                        'lucro':lucro_acao,
                        'retorno':retorno_acao,
                        'posicao':posicao_na_carteira,
                        'peso':peso_acao
                        }
                    }
        info_portfolio.append(dict_info)
    return info_portfolio
    #lucro que eu tenho na carteira no br e fora

    #previa do ir que eu teria que pagar