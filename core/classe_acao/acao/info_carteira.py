from core.classe_acao.acao_obj import Carteira

def info_carteira(portfolio, dolar, caixa):
    carteira = portfolio.portfolio_carteira()
    info_portfolio = []
    for acao in carteira:
        retorno_acao = portfolio.retorno(dolar,acao['acao'])
        lucro_acao = portfolio.lucro_carteira(dolar,acao['acao'],acao['nacional'])
        posicao_na_carteira = round(portfolio.posicao(dolar,acao['acao']),2)
        peso_acao = portfolio.peso_da_carteira(dolar, acao['acao'], caixa)
        media_movel = portfolio.media_movel_expodencial(acao['acao'])
        topo_fundo_acao = portfolio.topo_fundo(acao['acao'])
        indicador_hilo_acao = portfolio.indicador_hilo(acao['acao'])
        bandas_de_bolinger_acao = portfolio.bandas_de_bolinger(acao['acao'])
        rsi_acao = portfolio.rsi(acao['acao'])
        avg_vol_acao = portfolio.avg_vol(acao['acao'])
        dict_info = {'acao':acao,
                    'info':{
                        'lucro':lucro_acao,
                        'retorno':retorno_acao,
                        'posicao':posicao_na_carteira,
                        'peso':peso_acao},
                    'technical_analysis':{
                        'mma':media_movel,
                        'topo_fundo':topo_fundo_acao,
                        'hilo':indicador_hilo_acao,
                        'bollinger':bandas_de_bolinger_acao,
                        'rsi':rsi_acao,
                        'avg_vol':avg_vol_acao
                        }
                    }
        info_portfolio.append(dict_info)
    return info_portfolio
    #lucro que eu tenho na carteira no br e fora

    #previa do ir que eu teria que pagar