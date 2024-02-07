import pandas
import requests

chave = '197990f2-3434-43cb-8aeb-c9020c7042c5'

from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
import pandas as pd



'''res = requests.get("https://sandbox-api.coinmarketcap.com/v1/cryptocurrency/listings/latest").json()

headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': '197990f2-3434-43cb-8aeb-c9020c7042c5',
}

session = requests.Session()
session.headers.update()



print(res)

df = pd.DataFrame(res)

print(df)'''

url = 'https://sandbox-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
parameters = {
  'start':'1',
  'limit':'5000',
  'convert':'USD'
}
headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': '197990f2-3434-43cb-8aeb-c9020c7042c5',
}

session = Session()
session.headers.update(headers)

try:
  response = session.get(url, params=parameters)
  data = json.loads(response.text)
  print(response)
  print(data)
  df = pd.Series(response.json())
  print(df)
  res = pd.DataFrame(df)
  print(res)
  res.to_excel('teste.xlsx', 'w')
except (ConnectionError, Timeout, TooManyRedirects) as e:
  print(e)

url1 = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/map'
response1 = session.get(url1, params=parameters)
print(response1)