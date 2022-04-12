'''importação dos modulos'''
import locale
from time import sleep
import requests
import datetime
import bs4

cont = 0
data = datetime.datetime.now()
locale.setlocale(locale.LC_ALL,'pt_BR.UTF-8')

'''criando um dicionario para fazer uma busca'''
headers = {'user-Agent':'Mozilla/5.0'}

'''requisição para acessar o site'''
resposta = requests.post('https://br.investing.com/equities/',headers=headers)
soup = bs4.BeautifulSoup(resposta.text,'html.parser')
linhas = soup.find(id="cross_rate_markets_stocks_1").find('tbody').find_all('tr')
'''fazendo busca entre cada linha e coluna da tebela'''
for linha in linhas:
       dados_bolsa = linha.find_all('td')
       nome = ( dados_bolsa[1].text)
       ultimo = (dados_bolsa[2].text)
       maxima = (dados_bolsa[3].text)
       variacao = (dados_bolsa[4].text)
       valor =  (dados_bolsa[7].text)
       t = str(dados_bolsa)
       '''criando um arquivo com nome de cada ação com seus dados'''
       for c in dados_bolsa:
              with open(f'{nome}.txt','w') as arquivo:
                     arquivo.write(f"nome:{nome}+'\n"
                                   f"utima:{ultimo}"+'\n'
                                   f'maxima:{maxima}'+'\n'
                                   f"variacao:{variacao}"+'\n'
                                   f"valor:{valor}"'\n')




print('programa finalizado')



