import pandas as pd
from datetime import datetime
from AnnualVariation import AnnualVarition

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
AnnualVarition()
dataAnual = pd.DataFrame()
dataAnual['Data'] = AnnualVarition.datas
dataAnual['Total de Mortes'] = AnnualVarition.mortesTotal
dataAnual['Novas Mortes no Dia'] = AnnualVarition.mortesDia
dataAnual.to_csv("./files/dataAnual.csv",  index=False)
