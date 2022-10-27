#This script will take all killers addons and put them in one json file

#schema 
#{
#    "name": "name of addon",
#    "killerName": "name of killer",
#    "description": "description of addon",
#    "icon": "icon of addon",


import requests
from bs4 import BeautifulSoup
import json


#First we need to have all the killers urls
json_file = open('../resources/killers.json', 'r')

json_object = json.load(json_file)

urls = []

for key, val in json_object.items():
    for killer in val:
        urls.append('https://deadbydaylight.fandom.com' + killer['url'])


#And from every killer we need to get the addons
json_file = open('../resources/killersAddons.json', 'w')

json_object = {}

json_object['powerAddons'] = []

#All the killer addons are inside a table with the class wikitable
for url in urls:

    try:

        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')

        #This is the name of the killer
        #It needs to be the same as the killersData primary key, so we do the same code part to take the name + ( alias )
        killerName = soup.find('h1', class_='page-header__title').text.strip()
        #<table class="infobox-table">
        #   <tbody>
        #       <tr>
        #           <th>Nickname</th>
        #       </tr>

        table = soup.find('table', class_='infoboxtable')
        nickname = table.find('th').text.strip()
        comboName = killerName + ' (' + nickname + ')'

        #Killers whose addons are in a different table
        if comboName == 'Michael Myers (The  Shape)' or comboName == 'Amanda Young (The  Pig)' or comboName == 'Caleb Quinn (The  Deathslinger)' or comboName == 'Elliot Spencer alias Pinhead (The  Cenobite)':

            table = soup.find_all('table', class_='wikitable')[2]

            for tr in table.find_all('tr')[1:]:
                addonName = tr.find_all('th')[1].find('a').text.strip()
                addonDesc = tr.find('td').text.strip()
                addonIcon = tr.find_all('th')[0].find('a')['href']

                json_object['powerAddons'].append({
                    'name': addonName,
                    'killerName': comboName,
                    'description': addonDesc,
                    'icon': addonIcon
                })
        else:
            table = soup.find_all('table', class_='wikitable')[1]

            for tr in table.find_all('tr')[1:]:
                addonName = tr.find_all('th')[1].find('a').text.strip()
                addonDesc = tr.find('td').text.strip()
                addonIcon = tr.find_all('th')[0].find('a')['href']

                json_object['powerAddons'].append({
                    'name': addonName,
                    'killerName': comboName,
                    'description': addonDesc,
                    'icon': addonIcon
                })

    except Exception as e:
        print('Error with ' + killerName)

json.dump(json_object, json_file, indent=4)
        





