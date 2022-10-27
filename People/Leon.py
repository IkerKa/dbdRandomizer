#This file is a test to see if I can get the data from the website and put it into a csv file
#I am using the requests library to get the data from the website
#I am using the BeautifulSoup library to parse the data
#I am using the csv library to write the data to a csv file

import requests
from bs4 import BeautifulSoup
import csv


#This is the url of the website that I am getting the data from
#Survivor: Leon S. Kennedy

url = 'https://deadbydaylight.fandom.com/wiki/Leon_S._Kennedy'


#This is the request to get the data from the website
page = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')


#Tabla de donde sacamos los nombres de las habilidades

tabla_hablididades = soup.find('table', class_='wikitable')

#Tabla de la que sacamos la descripcion del superviviente
tabla_description = soup.find("table",style ="background:transparent")

#Tabla de la que sacamos el nombre y la imagen del superviviente
tabla_name = soup.find("table",class_="infoboxtable")





name = tabla_name.find('tbody').find_all('tr')[0].find('th').text

perk1 = tabla_hablididades.find("tbody").find_all("tr")[0].find_all("th")[1].find("a")["title"]

perk2 = tabla_hablididades.find("tbody").find_all("tr")[1].find_all("th")[1].find("a")["title"]

perk3 = tabla_hablididades.find("tbody").find_all("tr")[2].find_all("th")[1].find("a")["title"]

description = tabla_description.find('tbody').find_all('tr')[0].find_all("td")[1].text

imagen = tabla_name.find('tbody').find_all('tr')[1].find('th').find('a').find('img').get('data-src')

# Texto que sacamos con todos los atributos

text = "" + name + "\n" + perk1 + "\n" + perk2 + "\n" + perk3 + "\n \n \n" + description +"\n \n"   + imagen


print(text)
































