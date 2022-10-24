#This file is a test to see if I can get the data from the website and put it into a csv file
#I am using the requests library to get the data from the website
#I am using the BeautifulSoup library to parse the data
#I am using the csv library to write the data to a csv file

import requests
from bs4 import BeautifulSoup
import json


url = 'https://deadbydaylight.fandom.com/wiki/Perks'
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

#creates the json file
json_file = open('../resources/genKillerPerks.json', 'w', encoding='utf-8')

#creates the json object
json_object = {}

#The same process as the survivor perks, in the page we have 3 tables called wikitables, 
#we are only interested in the last one, the killer perks table
#WITH ENCODING UTF-8
table = soup.find_all('table', class_='wikitable sortable')[1]
#We put [1] because we have 2 wikitable sortable classes, the first one is the survivor perks table

json_object['Perks'] = []

#The same process as the survivor perks, the last 2 columns are for if the perk is from the survivor or killer
#As we take this perk, we already know it is from the killer, so we will put a 0 in the survivor column and
#a 1 in the killer column

#Loop
i = 0   #This is the counter for the perks
for tr in table.find_all('tr')[1:]:
    #they have the same format as the survivor perks, so we can use the same code
        #The url is inside the <a> in the tag href
    perkIcon = tr.find_all('th')[0].find('a')['href']
    perkName = tr.find_all('th')[1].find('a').text
    #if the perk name is 'Eruption' we have to skip the strange character at the first line of the description
    if perkName == 'Eruption':
        #this is the perk description is inside the <td>
        #we need to skip the second word in the description
        #The second word has a strange character, so we will skip the word and concat both texts
        perkDesc1 = tr.find_all('td')[0].find_all('div')[2].text[0:3]
        perkDesc2 = tr.find_all('td')[0].find_all('div')[2].text[8:]

        #concat the 2 texts
        perkDesc = perkDesc1 + perkDesc2

    else:
        perkDesc = tr.find_all('td')[0].find_all('div')[2].text

    #At this time we will print them in separate lines to check if them are correct

    json_object['Perks'].append({
        'perkName' : perkName,
        'perkIcon' : perkIcon,
        'perkDesc' : perkDesc,
        'fromSurvivor' : 0,
        'fromKiller' : 1
    })

    i += 1

# Write json_object into the json_file
json.dump(json_object, json_file, indent=4)











