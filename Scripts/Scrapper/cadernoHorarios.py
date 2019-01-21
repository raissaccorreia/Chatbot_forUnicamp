from bs4 import BeautifulSoup
import requests
import csv
import time


def createLink(ano, semestre, tipo, instituto, materia):

    link = 'https://www.dac.unicamp.br/portal/caderno-de-horarios/'

    # formato do link link/ano/semestre/S/tipo/instituto/materia
    return link + '/' + ano + '/' + semestre + '/' + 'S' + '/' + tipo + '/' + instituto + '/' + materia


def pegarSiglaPeloLink(link):

    siglaInst = link.split('/')
    return str(siglaInst[-1])


def parseHorario(tabela):
    horarioList = []

    horarios = tabela.find('ul', class_='horariosFormatado')

    if horarios is not None:

        for horario in horarios.findAll('li'):

            formato = horario.findAll('span')
            diaSemana = formato[0].text.encode('utf-8')
            horarios = formato[1].text.encode('utf-8')
            salaAula = formato[2].text.encode('utf-8')
            horarioTuple = (diaSemana, horarios, salaAula)
            horarioList.append(horarioTuple)

    return horarioList


def parseReservas(tabela):
    reservas = []

    todasReservas = tabela.find('ul', class_='reservas')

    if todasReservas is not None:

        for reserva in todasReservas.findAll('li'):
            reservas.append(reserva.text.strip().encode('utf-8'))

    return reservas


def parseTurma(tabela):
    try:
        turma = tabela.h3.span.text.strip()
    except:
        turma = '-'
    return turma


def parseVagas(tabela):
    try:
        vagas = tabela.find(class_='pull-right').span.text.strip()
    except:
        vagas = '-'
    return vagas


def parsenMatriculados(tabela):
    # print(tabela.encode('utf-8'))
    nMatriculadosText = tabela.find(class_='panel-body').p.span
    if nMatriculadosText is None:
        return "0"

    return nMatriculadosText.text.strip()


def parseDocente(tabela):
    try:
        docente = tabela.find('ul', class_='docentes').li.text.strip()
    except:
        docente = '-'
    return docente


def parseMateria(tabela):
    turma = parseTurma(tabela).encode('utf-8')
    vagas = parseVagas(tabela).encode('utf-8')
    nMat = parsenMatriculados(tabela).encode('utf-8')
    horarios = parseHorario(tabela)
    docente = parseDocente(tabela).encode('utf-8')
    reservas = parseReservas(tabela)

    # print((turma,nMat,horarios,vagas,docente,reservas))
    return (turma, nMat, horarios, vagas, docente, reservas)


def pegarLinksInstitutos(ano, semestre, tipo):

    link = 'https://www.dac.unicamp.br/portal/caderno-de-horarios/'
    sourceLink = link + ano + '/' + semestre + '/S/' + tipo  # criar link para materias do ano e semestre para graduacao

    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'}

    # r = requests.get(sourceLink).text
    r = requests.get(sourceLink, headers=headers).text

    soup = BeautifulSoup(r, 'lxml')

    listaOferecimentos = soup.find(class_='lista-oferecimento')

    # print(soup.prettify())

    listaLinksInstitutos = []

    for instituto in listaOferecimentos.findAll('a'):

        listaLinksInstitutos.append(instituto['href'].strip())
        # print(instituto['href'])

    return listaLinksInstitutos


def pegarDisciplinas(link):

    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'}

    r = requests.get(link, headers=headers).text
    # r = requests.get(link).text

    source = BeautifulSoup(r, 'lxml')

    todasDisciplinas = source.find(class_='disciplinas-horario').findAll('a')

    disciplinas = []

    for disciplina in todasDisciplinas:

        link = disciplina['href']
        sigla = pegarSiglaPeloLink(link)
        disciplinas.append(sigla)
        # print(disciplina['href'])

    return disciplinas


def pegarTodasDisciplinas(linksInstitutos):

    materiasDict = {}

    for link in linksInstitutos:

        sigla = pegarSiglaPeloLink(link)

        todasDisciplinas = pegarDisciplinas(link)

        materiasDict[sigla] = todasDisciplinas

    return materiasDict


def pegarInfoDisciplina(ano, semestre, tipo, instituto, materia):
    link = createLink(ano, semestre, tipo, instituto, materia)

    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'}

    r = requests.get(link, headers=headers).text
    # r = requests.get(link).text

    soup = BeautifulSoup(r, 'lxml')

    nomeMateria = soup.head.title.text

    tabelas = soup.body.findAll('div', class_='turma col-md-6')

    todasTurmas = []

    for tabela in tabelas:

        if not tabela is None:
            (turma, nMat, horarios, vagas, docente, reservas) = parseMateria(tabela)

            todasTurmas.append((turma, nMat, horarios, vagas, docente, reservas))
            # print(turma,nMat,horarios,vagas,docente,reservas)
            # print('#############')

    return todasTurmas


def salvarDiscEmCSV(ano, semestre, tipo, todasDisc):

    instFile = open('Institutos.csv', 'a')
    instWriter = csv.writer(instFile)
    instWriter.writerow(['instituto', 'materias', 'ano', 'semestre', 'tipo'])

    for inst in todasDisc.keys():

        for disc in todasDisc[inst]:

            instWriter.writerow([inst, disc, ano, semestre, tipo])

    instFile.close()


# Web scraper para pegar informações das materias no site da dac.


# infos teste
ano = '2018'
semestre = '2'
tipo = 'G'
#

print('Comecando a pegar materias')

linksTodosInstitutos = pegarLinksInstitutos(ano, semestre, tipo)

print('Todas disciplinas pegas')
print('Comecando a pegar informacoes das materias')
todasDisc = pegarTodasDisciplinas(linksTodosInstitutos)

# salvarDiscEmCSV(ano,semestre,tipo,todasDisc)

for inst in todasDisc.keys():

    for disc in todasDisc[inst]:

        # todasTurmas = pegarInfoDisciplina(ano, semestre, tipo, inst, disc)
        # print(disc + ':')
        # print(todasTurmas)
        link = createLink(ano, semestre, tipo, inst, disc)

        page = ''

        while page is '':
            try:
                page = requests.get(link).text
                sigla = pegarSiglaPeloLink(link)
                print(sigla)
                break
            except:
                # print("Connection refused by the server..")
                # print("Let me sleep for 5 seconds")
                # print("ZZzzzz...")
                time.sleep(5)
                # print("Was a nice sleep, now let me continue...")
                continue

        soup = BeautifulSoup(page, 'lxml')

        nomeMateria = soup.head.title.text

        tabelas = soup.body.findAll('div', class_='turma col-md-6')

        todasTurmas = []

        for tabela in tabelas:

            if not tabela is None:
                (turma, nMat, horarios, vagas, docente, reservas) = parseMateria(tabela)

                todasTurmas.append((turma, nMat, horarios, vagas, docente, reservas))
                # print(turma,nMat,horarios,vagas,docente,reservas)
                # print('#############')

        # print(todasTurmas)
