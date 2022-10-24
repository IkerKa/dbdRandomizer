#This file is a test to see if I can get the data from the website and put it into a csv file
#I am using the requests library to get the data from the website
#I am using the BeautifulSoup library to parse the data
#I am using the csv library to write the data to a csv file

import requests
from bs4 import BeautifulSoup
import csv


url = 'https://deadbydaylight.fandom.com/wiki/Perks'
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

csv_file = open('killerPerks.csv', 'w')
csv_writer = csv.writer(csv_file)

#The same process as the survivor perks, in the page we have 3 tables called wikitables, 
#we are only interested in the last one, the killer perks table
#WITH ENCODING UTF-8
table = soup.find_all('table', class_='wikitable sortable')[1]
#We put [1] because we have 2 wikitable sortable classes, the first one is the survivor perks table

#Before I start the for loop I need to write the headers to the csv file seperately
csv_writer.writerow(['Perk Name', 'Perk Icon', 'Perk Description', 'fromSurvivor','fromKiller'])

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
    csv_writer.writerow([perkName])
    csv_writer.writerow([perkIcon])
    csv_writer.writerow([perkDesc])
    csv_writer.writerow(['0'])
    csv_writer.writerow(['1'])
    csv_writer.writerow([i])
    i += 1

    csv_writer.writerow([])


csv_file.close()











