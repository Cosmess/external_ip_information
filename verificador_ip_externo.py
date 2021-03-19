#caso necessario:
# pip install re
# pip install json
# pip install urllib


import re
import json
from  urllib.request import urlopen

url = 'https://ipinfo.io/json'

resposta = urlopen(url)

dados = json.load(resposta)

ip = dados['ip']
org = dados['org']
cid = dados['city']
pais = dados['country']
regiao = dados['region']
zona = dados['timezone']


print('Detalhes Do IP Externo:\n')
print('IP: {4}\nRegião: {1}\nPais: {2}\nCidade: {3}\nOrganização: {0}\nZona:  {5}'.format(org,regiao,pais,cid,ip,zona))