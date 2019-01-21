from bs4 import BeautifulSoup
import requests
import re
import csv

calFile = open('calendario2018-2.csv', 'w')

calWriter = csv.writer(calFile)

calWriter.writerow(['dataInicio', 'dataFim', 'entidade', 'info'])

url = 'https://www.dac.unicamp.br/portal/calendario/2018/graduacao'

# url = 'https://www.dac.unicamp.br/portal/calendario/2018/pos-graduacao'
# url = 'https://www.dac.unicamp.br/portal/calendario/2018/medicina'

source = requests.get(url).text
mesDict = {'Janeiro': '01', 'Fevereiro': '02', 'Março': '03', 'Abril': '04', 'Maio': '05', 'Junho': '06', 'Julho': '07', 'Agosto': '08', 'Setembro': '09', 'Outubro': '10', 'Novembro': '11', 'Dezembro': '12'}

page = BeautifulSoup(source, 'lxml')
tabela = page.find(id='conteudo').find('table')

inicioAntigo = ''
fimAntigo = ''
mesAtual = ''
anoAtual = ''
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

        # print(dataInicio, dataFim, entidade.encode('utf-8'), info.encode('utf-8'))
        # calWriter.writerow([dataInicio, dataFim, entidade.encode('utf-8'), info.encode('utf-8')])
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
