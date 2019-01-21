from bs4 import BeautifulSoup
import requests
import re

url = 'https://www.dac.unicamp.br/portal/graduacao/regimento-geral'
source = requests.get(url).text

soup = BeautifulSoup(source, 'lxml')

conteudo = soup.find(id='conteudo')
artigos = []
artigo = ''.encode('utf-8')
for c in conteudo.findAll(['p', 'table']):

    tipo = c.name
    alinhamento = ''
    if 'align' in c.attrs:
        alinhamento = c['align']

        # print(alinhamento)

    if tipo is 'p':
        texto = c.text

        if 'Art.' in texto:
            artigos.append(artigo)
            artigo = texto.encode('utf-8')
            # print(texto.encode('utf-8'))

        elif alinhamento is 'justify':
            artigo = artigo + texto.encode('utf-8')

        else:
            artigos.append(texto.encode('utf-8'))

    else:
        header = c.find('thead').text.rstrip()
        header = re.sub('\xa0+', '', header)
        header = re.sub('\n+', '', header)
        header = re.sub('\t+', '', header)
        header = header.split('\r')
        # print(header)

        for tr in c.find('tbody').findAll('tr'):
            row = []
            for td in tr.findAll('td'):
                row.append(td.text.strip().encode('utf-8'))

            # print(header, row)
    # print(c.prettify().encode('utf-8'))
    # print(c.name.encode('utf-8'))

print(artigos)
