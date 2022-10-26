#To take the addons in other script we will take the common name of the item and add its addons

#for example:

# We have 3 types of flashlights: Flashlight, Sport flashlight and Utility flashlight

# All of them have the same common name: Flashlight, and all of them have the same type of addons for them

# So the json file will look like this:
# Flashlight: {
    # addons: {
        #...

# Maybe I will repeat all the addons for the different type of flashlights

#FIRECRACKERS ADDONS DOESN'T HAVE ANY ADDONS


import requests
from bs4 import BeautifulSoup
import json

#we will take the addons with this source url
url = "https://deadbydaylight.fandom.com/wiki/Items"

#We will take the url of every type of item that brings us to the addons of that item

urls = []

#The same method as in the items script
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

#The url is inside the <th> tag inside the <h3> tag inside the <span> tag with the class "mw-headline"  and its the text of the <a> tag
#schema
#<h3>
#   <span>
#       <a>
#       </a>
#   </span>
#</h3>


#flashlights
urls.append(soup.find_all('h3')[6].find('span').find('a')['href'])

#keys
urls.append(soup.find_all('h3')[7].find('span').find('a')['href'])

#maps
urls.append(soup.find_all('h3')[8].find('span').find('a')['href'])

#medkits
urls.append(soup.find_all('h3')[9].find('span').find('a')['href'])

#toolboxes
urls.append(soup.find_all('h3')[10].find('span').find('a')['href'])


#And now we are going to generate the complete url of the addons of every item
#The complete url is the url of the item + urls[i]

mainUrl = "https://deadbydaylight.fandom.com"

for i in range(len(urls)):
    urls[i] = mainUrl + urls[i]


#Now we will take the addons of every item

#We will open the json file
json_file = open('../resources/addons.json', 'w')

#We will create the json object
json_object = {}

json_object['addons'] = []

#We will take the addons of every item
for i in range(len(urls)):

    #We will take the name of the item
    itemName = urls[i].split('/')[-1]
    
    #We open the page
    page = requests.get(urls[i])
    soup = BeautifulSoup(page.content, 'html.parser')

    if itemName == 'Keys' or itemName == 'Maps':
        #the addons are in the 4th table with the class "wikitable"
        table = soup.find_all('table', class_='wikitable')[2]

        for tr in table.find_all('tr')[1:]:
            #The name of the addon is inside the <th> tag
            addonName = tr.find_all('th')[1].find('a').text.strip()

            #The description of the addon is inside the <td> tag
            addonDescription = tr.find('td').text.strip()

            #The image of the addon is inside the <img> tag with the class "image-thumbnail"
            addonImage = tr.find_all('th')[0].find('a')['href']

            #We will add the addon to the json object
            json_object['addons'].append({
                'name': addonName,
                'item': itemName,
                'description': addonDescription,
                'image': addonImage
            })
    else:
        #the addons are in the 4th table with the class "wikitable"
        table = soup.find_all('table', class_='wikitable')[3]

        for tr in table.find_all('tr')[1:]:
            #The name of the addon is inside the <th> tag
            addonName = tr.find_all('th')[1].find('a').text.strip()

            #The description of the addon is inside the <td> tag
            addonDescription = tr.find('td').text.strip()

            #The image of the addon is inside the <img> tag with the class "image-thumbnail"
            addonImage = tr.find_all('th')[0].find('a')['href']

            #We will add the addon to the json object
            json_object['addons'].append({
                'name': addonName,
                'item': itemName,
                'description': addonDescription,
                'image': addonImage
            })

#We will write the json object to the json file
json.dump(json_object, json_file, indent=4)

    










