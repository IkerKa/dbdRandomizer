#This file is the official general perks file to parse directly into a json file
import requests
from bs4 import BeautifulSoup
import csv
import json

url = 'https://deadbydaylight.fandom.com/wiki/Perks'
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser', from_encoding='utf-8')
#csv_file = open('genPerks.csv', 'w', encoding='utf-8', newline='\n')
#csv_writer = csv.writer(csv_file, delimiter='*')

#creates the json file
json_file = open('genPerks.json', 'w', encoding='utf-8')

#creates the json object
json_object = {}

table = soup.find('table', class_='wikitable')

#This is the for loop that is going through the table and getting the data

#each perk will be a row in the csv file
#colums:
#perk name | perk icon (url) | perk description

#Before I start the for loop Ill write the header in the json file
json_object['Perks'] = []

#each perk will be a row in the csv file
#colums:
#perk name | perk icon (url) | perk description
#each <tr> is a row (perk)
#to test it I am just going to get the first 3 perks

#this is the for loop that is going through the table and getting the data
for tr in table.find_all('tr'):
    #each tr has 2 <th> and 1 <td>
    #the first <th> is the perk icon
    #the second <th> is the perk name
    #the <td> is the perk description

    #this is the perk icon is inside the first <th>/<a>/<img>
    #The url is inside the <a> in the tag href
    perkIcon = tr.find_all('th')[0].find('a')['href']

    #this is the perk name is inside the second <th>/<a>
    perkName = tr.find_all('th')[1].find('a').text

    #this is the perk description is inside the <td> in the third <div> it is all the desc
    perkDesc = tr.find_all('td')[0].find_all('div')[2].text

    #this is the csv writer to write the data to the json file (separator bteween columns is a *)
    #csv_writer.writerow([perkName, perkIcon, perkDesc])
    json_object['Perks'].append({
        'perkName': perkName,
        'perkIcon': perkIcon,
        'perkDescription': perkDesc,
        'fromSurvivor': 1,
        'fromKiller': 0
    })

# Write json_object into the json_file
json.dump(json_object, json_file, indent=4)


#This is closing the csv file
#csv_file.close()


