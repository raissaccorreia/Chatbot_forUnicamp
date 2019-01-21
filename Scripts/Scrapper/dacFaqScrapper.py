from bs4 import BeautifulSoup
from bs4 import UnicodeDammit
import requests
import csv


def printFAQ(pergDic, respDic):
    for key in pergDic:
        print(pergDic[key].encode('utf-8'))
        print('---------------------------------------')
        print(respDic[key].encode('utf-8'))
        print('---------------------------------------')


def salvaNoCSV(nomeArq,pergDic, respDic):
    nomeArq += '.csv'
    faqFile = open(nomeArq, 'w')
    faqWriter = csv.writer(faqFile)

    faqWriter.writerow(['pergunta', 'resposta'])

    for key in pergDic:
        faqWriter.writerow([pergDic[key].encode('utf-8'), respDic[key].encode('utf-8')])


def nextElem(p):

    nextElem = p.next_element

    if nextElem is not None:
        while nextElem.name not in ['p', 'ul']:
            nextElem = nextElem.next_element

    return nextElem


def pegarNumPerguntas(final):

    n = final.find_previous('a')['name']

    return ("".join([s for s in n if s.isdigit()]))


def pegarFAQ(url):
    source = requests.get(url).text

    soup = BeautifulSoup(source, 'lxml')
    conteudo = soup.find(id='conteudo')

    final = conteudo.find('div', class_='hidden-print')

    nPerg = pegarNumPerguntas(final)
    respDic = {}
    pergDic = {}

    for i in range(1, int(nPerg) + 1):

        # print(i)
        resp = ''
        # per
        perg = 'pergunta' + str(i)
        nextPerg = 'pergunta' + str(i + 1)

        if i is int(nPerg):
            proxPerg = final
        else:
            proxPerg = conteudo.find('a', {'name': nextPerg}).parent

        pergunta = conteudo.find('a', {'name': perg})
        pergDic[perg] = pergunta.text

        for p in pergunta.find_all_next():

            # print(p.text.encode('utf-8'))
            resp = resp + p.text
            # print(p.name)

            if proxPerg.name is final.name:
                nextP = p.next_sibling
            else:
                nextP = nextElem(p)
            # print(nextP.encode('utf-8'))
            # print(nextP.name)
            if nextP is proxPerg:
                break

        respDic[perg] = resp

    return (pergDic,respDic)


# url = 'http://www.dac.unicamp.br/portal/duvidas-frequentes/duvidas-frequentes-graduacao' 
url = 'https://www.dac.unicamp.br/portal/duvidas-frequentes/perguntas-frequentes-pos-graduacao'

pergDic,respDic = pegarFAQ(url)
# salvaNoCSV('grad-faq',pergDic, respDic)
salvaNoCSV('pos-faq',pergDic, respDic)
printFAQ(pergDic,respDic)