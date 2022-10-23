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
csv_file = open('scrapplingTest.csv', 'w')

#This is the csv writer that I am using to write the data to the csv file
csv_writer = csv.writer(csv_file)

#This is the table that I am getting the data from
table = soup.find('table', class_='wikitable')

#This is the for loop that is going through the table and getting the data

#each perk will be a row in the csv file
#colums:
#perk name | perk icon (url) | perk description

#Before I start the for loop I need to write the headers to the csv file seperately
csv_writer.writerow(['Perk Name', 'Perk Icon', 'Perk Description'])




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

    #this is the print statement to test the data
    print(perkName, perkIcon, perkDesc)

    #this is the csv writer to write the data to the csv file
    #csv_writer.writerow([perkName, perkIcon, perkDesc])
    #To check if its working, ill put each data in different rows
    csv_writer.writerow([perkName])
    csv_writer.writerow([perkIcon])
    csv_writer.writerow([perkDesc])

    #empty line to seperate the perks
    csv_writer.writerow([])
    




#This is closing the csv file
csv_file.close()


