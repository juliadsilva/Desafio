import pandas as pd

data = pd.read_excel("./files/owid-covid-data.xlsx")

# BRA iso code lines
dataBRA = data[data['iso_code'].str.contains('BRA')]

# Extract specific columns
dataBRA = dataBRA[['date', 'total_deaths', 'new_deaths']]

# Rename columns
dataBRA = dataBRA.rename(columns={'date': 'Data', 'total_deaths': 'Total de Morte', 'new_deaths': 'Novas Mortes no Dia'})

# Change date format
dataBRA['Data'] = pd.to_datetime(dataBRA['Data'])
dataBRA['Data'] = dataBRA['Data'].dt.strftime('%d/%m/%Y')

# Delete empty lines
dataBRA = dataBRA.dropna()

# Save CVS
dataBRA.to_csv("./files/dataBRA.csv", index=False)

# Calculation of annual variation
datas = []
mortesTotal = []
mortesDia = []

dataInicial = int(dataBRA[dataBRA['Data'].str.contains('17/03/2021')].index.values)
dataFinal = int(dataBRA.iloc[[-1]].index.values)
dataComparacao = int(dataBRA[dataBRA['Data'].str.contains('17/03/2020')].index.values)

while dataInicial <= dataFinal:
    dado_ano_atual = dataBRA.loc[[dataInicial]]
    dado_ano_anterior = dataBRA.loc[[dataComparacao]]

    datas.append(dado_ano_atual['Data'].values)

    mortesTotal.append(
        ((dado_ano_atual['Total de Morte'].values / dado_ano_anterior['Total de Morte'].values) - 1) * 100)

    mortesDia.append(
        ((dado_ano_atual['Novas Mortes no Dia'].values / dado_ano_anterior['Novas Mortes no Dia'].values) - 1) * 100)

    dataInicial += 1
    dataComparacao += 1

dataAnual = pd.DataFrame()
dataAnual['Data'] = datas
dataAnual['Total de Mortes'] = mortesTotal
dataAnual['Novas Mortes no Dia'] = mortesDia
dataAnual.to_csv("./files/dataAnual.csv",  index=False)

print('Fim da execução')