import requests
import json
import pandas as pd
import numpy as np
import openpyxl

cotacoes = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL").json()

df = pd.DataFrame(cotacoes)
serie_np = pd.Series(cotacoes)

df.to_excel('Registros.xlsx', 'w')
serie_np.to_excel('Registro2.xlsx', 'w')

print(df)


# https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL
