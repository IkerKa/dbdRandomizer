#This will return all the survivors in the game (their url)

import requests
from bs4 import BeautifulSoup
import json

#This is the url of the website that I am getting the data from
url = 'https://deadbydaylight.fandom.com/wiki/Category:Survivors'

#This is the request to get the data from the website
page = requests.get(url)

#This is the soup object that I am using to parse the data
soup = BeautifulSoup(page.content, 'html.parser')

#This is the json file that I am writing the data to
json_file = open('../resources/survivors.json', 'w')

#This is the json object that I am writing to the json file
json_object = {}

#the survivors are inside a <div> tag with the id "mw-pages"
#All survivor is inside a <div> tag with the class "mw-category" 
#Each survivor is inside a <div> tag with the class "mw-category-group"
    #Inside every <div> tag with the class "mw-category-group" there is a <h3> tag with the letter of the survivor (first one)


#The url is inside an <a> tag inside the <li> tag of the <ul> tag marked with the href "/wiki/Name_of_survivor"

#This is the for loop that is going through the table and getting the data

#schema:
#<div>
#   <h3>Letter</h3>
#   <ul>
#       <li>
#           <a href="/wiki/Name_of_survivor">Name of survivor</a>
#       </li>
#   </ul>
#</div>

#This is the for loop that is going through the table and getting the data
for div in soup.find_all('div', class_='mw-category-group'):
    #This is the letter of the survivor
    letter = div.find('h3').text

    #This is the list of survivors
    ul = div.find('ul')

    #This is the list of survivors
    json_object[letter] = []

    #This is the for loop that is going through the list of survivors
    for li in ul.find_all('li'):
        #This is the name of the survivor
        name = li.find('a').text

        #This is the url of the survivor
        url = li.find('a').get('href')

        #This is the dictionary that will be added to the json object
        survivor = {
            'name': name,
            'url': url
        }

        #This is the list of survivors
        json_object[letter].append(survivor)

#This is the json dump
json.dump(json_object, json_file, indent=4)
