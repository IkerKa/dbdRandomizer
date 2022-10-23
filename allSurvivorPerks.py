#This file is a test to see if I can get the data from the website and put it into a csv file
#I am using the requests library to get the data from the website
#I am using the BeautifulSoup library to parse the data
#I am using the csv library to write the data to a csv file

import requests
from bs4 import BeautifulSoup
import csv

#This is the url of the website that I am getting the data from
url = 'https://deadbydaylight.fandom.com/wiki/Perks'

#This is the request to get the data from the website
page = requests.get(url)

#This is the soup object that I am using to parse the data
soup = BeautifulSoup(page.content, 'html.parser')

#This is the csv file that I am writing the data to
csv_file = open('survPerks.csv', 'w')

#This is the csv writer that I am using to write the data to the csv file
csv_writer = csv.writer(csv_file)

#We will take the table that is the survivor perks table and its after a h3 tag
#The table is the first table after the h3 tag 
#the id before the table is the id of the h3 tag (Survivor_Perks_(113))

#This is the table that I am getting the data from
table = soup.find('h3', id='Survivor_Perks_(113)').find_next('table')

print(table)



#This is the table that I am getting the data from
table = soup.find('table', class_='wikitable')



#This is the for loop that is going through the table and getting the data

#each perk will be a row in the csv file
#colums:
#perk name | perk icon (url) | perk description

#Before I start the for loop I need to write the headers to the csv file seperately
csv_writer.writerow(['Perk Name', 'Perk Icon', 'Perk Description', 'fromSurvivor','fromKiller'])

#the last 2 columns are for if the perk is from the survivor or killer
#As we take this perk, we already know it is from the survivor, so we will put a 1 in the survivor column
#and a 0 in the killer column

#each perk will be a row in the csv file
#colums:
#perk name | perk icon (url) | perk description
#each <tr> is a row (perk)

#the table starts with a <thead> and after that is a <tbody> (thats where the perks are) and ends with a <tfoot>
#the <thead> and <tfoot> are not needed so I am going to skip them

#to test it I am just going to get the first 3 perks

#this is the for loop that is going through the table and getting the data

#Skip the <thead> part:
#the <thead> is the first <tr> in the <table>
#so I am going to skip the first <tr> in the <table>

#to skip the first <tr> I am going to use the next() function
#the next() function will skip the first <tr> in the <table>



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

    #this is the print statement to test the data
    #print(perkName, perkIcon, perkDesc)

    #this is the csv writer to write the data to the csv file
    #csv_writer.writerow([perkName, perkIcon, perkDesc])
    #To check if its working, ill put each data in different rows
    csv_writer.writerow([perkName])
    csv_writer.writerow([perkIcon])
    csv_writer.writerow([perkDesc])
    csv_writer.writerow(['1'])
    csv_writer.writerow(['0'])

    #empty line to seperate the perks
    csv_writer.writerow([])
    






#This is closing the csv file
csv_file.close()