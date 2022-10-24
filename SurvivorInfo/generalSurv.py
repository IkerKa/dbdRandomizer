#This file will be used to get the data from every survivor in the game and write it to a json file
# We will use the json file survivors.json that has the url of every survivor in the game

import requests
from bs4 import BeautifulSoup
import json

#The main url will be
#https://deadbydaylight.fandom.com

#And with the url of the survivors in the json file we will get the data of every survivor in the game we will complete the link with the url of the survivor
#for example: https://deadbydaylight.fandom.com/wiki/Name_of_survivor

#To do this N times, we are going to read every link 
#and complete it with the main url and then get the data from the website

#Open the json file with the urls of the survivors
json_file = open('../resources/survivors.json', 'r')

#Load the json file
json_object = json.load(json_file)

#Url vector 
urls = []

#Combine the main url with the url of the first survivor

for key, val in json_object.items():
    for surv in val:
        #completed url
        urls.append('https://deadbydaylight.fandom.com' + surv['url'])
        
    
#We have all the urls of the survivors in the game

#Now we are going to get the data from every survivor

#This is the json file that I am writing the data to
json_file = open('../resources/survivorsData.json', 'w')

#This is the json object that I am writing to the json file
json_object = {}

#This is the for loop that is going through the table and getting the data


for url in urls:

    try:
        #This is the request to get the data from the website
        page = requests.get(url)

        #This is the soup object that I am using to parse the data
        soup = BeautifulSoup(page.content, 'html.parser')

        #This is the name of the survivor
        survName = soup.find('h1', class_='page-header__title').text.strip()
        #print(survName)

        #This is the image of the survivor (we take the url)
        
        survImg = soup.find('div', class_='floatleft').find('a').get('href')

        if survName == 'Nancy Wheeler':
            survDesc = soup.find('div', class_='mw-parser-output').find_all('p')[8].text
        #This is the description of the survivor (the second <td>)
        elif survName == 'Steve Harrington':
            survDesc = soup.find('div', class_='mw-parser-output').find_all('p')[7].text
        else:
            survDesc = soup.find('table', style='background:transparent').find('tr').find_all('td')[1].text

        
        #t1 = soup.find('table', style='background:transparent')
        #print(t1.prettify())


        #Now we are going to take the 3 perks of the survivor
        #The perks are in the table called wikitable

        #This is the table with the perks
        table = soup.find('table', class_='wikitable')

        #This is the vector with the perks
        perks = []

        #This is the for loop that is going through the table and getting the data
        for tr in table.find_all('tr'):
            #This is the name of the perk 
            perkName = tr.find_all('th')[1].find('a').text

            perks.append(perkName)

        

        #Now we are going to add the data to the json object
        json_object[survName] = {
            'name': survName,
            
            
            'perk_1s': perks[0],
            'perk_2s': perks[1],
            'perk_3s': perks[2],

            'desc': survDesc,
            'img': survImg
        }
    except Exception as e:
        print(f"exception caught at {url}") 


#Now we are going to write the json object to the json file
json.dump(json_object, json_file, indent=4)





