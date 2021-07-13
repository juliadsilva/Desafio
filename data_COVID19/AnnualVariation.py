import pandas as pd

class AnnualVarition:

    dataBRA = pd.read_csv("./files/dataBRA.csv")
    datas = []
    mortesTotal = []
    mortesDia = []

    dataInicial = int(dataBRA[dataBRA['Data'].str.contains('17/03/2021')].index.values)
    dataFinal = int(dataBRA[dataBRA['Data'].str.contains('11/07/2021')].index.values)

    i = 0
    while dataInicial <= dataFinal:
        dado_ano_atual = dataBRA.loc[[dataInicial]]
        dado_ano_anterior = dataBRA.loc[[i]]

        datas.append(dado_ano_atual['Data'].values)
        mortesTotal.append(
            ((dado_ano_atual['Total de Morte'].values / dado_ano_anterior['Total de Morte'].values) - 1) * 100)
        mortesDia.append(
            ((dado_ano_atual['Novas Mortes no Dia'].values / dado_ano_anterior['Novas Mortes no Dia'].values) - 1) * 100)

        i += 1
        dataInicial +=1








