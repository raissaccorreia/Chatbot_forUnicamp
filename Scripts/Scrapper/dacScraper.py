from bs4 import BeautifulSoup
import requests
import csv

sourceLink = "https://www.dac.unicamp.br/portal/formularios"
dacLink = 'https://www.dac.unicamp.br'

csv_file = open('Formularios.csv', 'w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['tipo', 'referencia', 'link'])

source = requests.get(sourceLink).text

soup = BeautifulSoup(source, 'lxml')

# print(soup.prettify())

allForms = soup.find('table', class_='table')
# print(allForms.prettify())

forms = allForms.findAll('td')
for form in forms:

    tipo = form.h3.text
    links = form.findAll('li')

    for link in links:

        formLink = link.a['href']
        if dacLink not in formLink:
            formLink = (dacLink + link.a['href'])

        formRef = link.a.text

        csv_writer.writerow([tipo.encode('utf-8'), formRef.encode('utf-8'), formLink.encode('utf-8')])
