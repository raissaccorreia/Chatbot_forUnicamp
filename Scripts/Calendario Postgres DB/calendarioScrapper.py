from bs4 import BeautifulSoup
import requests
import re
import csv
from unidecode import unidecode
import json

from entities import entities

calFile = open('calendario2018-2.csv', 'w')

calWriter = csv.writer(calFile)

calWriter.writerow(['dataInicio', 'dataFim', 'entidade', 'info'])

url = 'https://www.dac.unicamp.br/portal/calendario/2018/graduacao'

# url = 'https://www.dac.unicamp.br/portal/calendario/2018/pos-graduacao'
# url = 'https://www.dac.unicamp.br/portal/calendario/2018/medicina'

filename = 'calendario.sql'

source = requests.get(url).text
mesDict = {'Janeiro': '01', 'Fevereiro': '02', 'Março': '03', 'Abril': '04', 'Maio': '05', 'Junho': '06', 'Julho': '07', 'Agosto': '08', 'Setembro': '09', 'Outubro': '10', 'Novembro': '11', 'Dezembro': '12'}

page = BeautifulSoup(source, 'lxml')
tabela = page.find(id='conteudo').find('table')

with open(filename, 'w') as f:
    pass

inicioAntigo = ''
fimAntigo = ''
mesAtual = ''
anoAtual = ''

d = {}

for key, value in entities.items():
    k = unidecode(key).lower()
    if isinstance(value, list):
        for item in value:
            i = unidecode(item).lower()
            if i not in d:
                d[i] = k
    else:
        v = unidecode(value).lower()
        if v not in d:
            d[v] = k

# print(json.dumps(d, indent=4, sort_keys=True))

for tr in tabela.findAll('tr'):

    p = tr.findAll('td')

    tam = len(p)

    if tam is 3:

        data = p[0].text.strip()

        splitted = re.split(' a | e ', data)

        if splitted[0] is '':
            splitted[0] = '-'

        dataInicio = splitted[0] + '/' + mesAtual + '/' + anoAtual
        dataFim = dataInicio

        if len(splitted) is 2:

            fim = splitted[1].split('.')
            if len(fim) is 2:
                dataFim = (fim[0]) + '/' + fim[1] + '/' + anoAtual
            else:
                dataFim = fim[0] + '/' + mesAtual + '/' + anoAtual

        entidade = p[1].text.strip()
        info = p[2].text.strip()

        inicioAntigo = dataInicio
        fimAntigo = dataFim

        if '-' in dataInicio:
            dataInicio = '01' + dataInicio[1:]
        
        if '-' in dataFim:
            dataFim = '01' + dataFim[1:]

        semestre = 1 if int(dataInicio[3:5]) < 7 else 2

        # print(dataInicio, dataFim, entidade.encode('utf-8'), info.encode('utf-8'))
        calWriter.writerow([dataInicio, dataFim, entidade.encode('utf-8'), info.encode('utf-8')])

        entidade = unidecode(entidade.lower())
        
        with open(filename, 'a+') as f:
            f.write("INSERT INTO CALENDAR (YEAR_INTEGER, SEMESTER_INTEGER, ENTITY_STR, DESCRIPTION_STR, INITIAL_DATE, END_DATE, URI_STR) VALUES (%s, %s, '%s', '%s', '%s', '%s', '%s');\n" %
                (dataInicio[-4:], semestre, d[entidade], info, dataInicio, dataFim, url))
        calWriter.writerow([dataInicio, dataFim, entidade, info])

    elif tam is 2:

        dataInicio = inicioAntigo
        dataFim = fimAntigo
        entidade = p[0].text.strip()
        info = p[1].text.strip()

        # print(dataInicio, dataFim, entidade.encode('utf-8'), info.encode('utf-8'))
        # calWriter.writerow([dataInicio, dataFim, entidade.encode('utf-8'), info.encode('utf-8')])
        calWriter.writerow([dataInicio, dataFim, entidade, info])

    elif tam is 1:
        m = p[0].text.strip().split(' de ')

        # print(m)

        if m[0] in mesDict.keys():
            mesAtual = mesDict[m[0]]
            anoAtual = m[1]

        # print('mes atual ', mesAtual, anoAtual)
