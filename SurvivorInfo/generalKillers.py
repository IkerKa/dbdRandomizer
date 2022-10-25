#This script will take all the urls and parse every killer and get the data from the killer and put it in a json file

#It does the same as generalSurv.py but it does it for the killers

import requests
from bs4 import BeautifulSoup
import json

#Open the json file with the urls of the survivors
json_file = open('../resources/killers.json', 'r')

#Load the json file
json_object = json.load(json_file)

#Url vector 
urls = []

#Combine the main url with the url of the first survivor

for key, val in json_object.items():
    for killer in val:
        #completed url
        urls.append('https://deadbydaylight.fandom.com' + killer['url'])
        

json_file = open('../resources/killersData.json', 'w')
json_object = {}
json_object['Killers'] = []

for url in urls:
    try:
        #We try to enter into the combined url
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')
        #This is the name of the killer
        killerName = soup.find('h1', class_='page-header__title').text.strip()
        #<table class="infobox-table">
        #   <tbody>
        #       <tr>
        #           <th>Nickname</th>
        #       </tr>

        table = soup.find('table', class_='infoboxtable')
        nickname = table.find('th').text.strip()
        comboName = killerName + ' (' + nickname + ')'
        
        killerIcon = soup.find('div', class_='floatleft').find('a').get('href')

        #The three initial killers of the game are the only ones that have a different layout
        if killerName == 'Evan MacMillan' or killerName == 'Max Thompson Jr.' or killerName == 'Philip Ojomo':
            killerDesc = soup.find_all('table', style='background:transparent')[1].find('tr').find_all('td')[1].text
        else:
            killerDesc = soup.find('table', style='background:transparent').find('tr').find_all('td')[1].text

        table = soup.find('table', class_='wikitable')

        perks = []

        for tr in table.find_all('tr'):
            perkName = tr.find_all('th')[1].find('a').text
            perks.append(perkName)

        
        #Finally we add the data to the json object
        json_object['Killers'].append({
            'name': comboName,
            'perk_1k': perks[0],
            'perk_2k': perks[1],
            'perk_3k': perks[2],
            'mainHability': killerDesc,
            'image_k': killerIcon })

    except Exception as e: 
        print('Error in the url: ' + url)


#We write the json object to the json file
json.dump(json_object, json_file, indent=4)


