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

#Now we are going to do 5 arrays to take all the different item names from the item.json file

#flashlights
Flashlights = []
#keys
keys = []
#maps
maps = []
#medkits
MedKits = []
#toolboxes
Toolboxes = []

#Firecrackers doesn't have any addons

#We will take the name of the item from the item.json file
with open('../resources/items.json') as json_file:
    data = json.load(json_file)
    for p in data['items'][3:9]:
        Flashlights.append(p['name'])
    for p in data['items'][9:12]:
        keys.append(p['name'])
    for p in data['items'][12:14]:
        maps.append(p['name'])
    for p in data['items'][14:21]:
        MedKits.append(p['name'])
    for p in data['items'][21:28]:
        Toolboxes.append(p['name'])
        


        

#print(flashlights)
#print(keys)
#print(maps)
#print(medkits)
#print(toolboxes)


#And we put them in an array of arrays
items = [Flashlights, keys, maps, MedKits, Toolboxes]

#to index the items array:
#flashlights = 0
#keys = 1
#maps = 2
#medkits = 3
#toolboxes = 4



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
json_file = open('../resources/addonsRwrk.json', 'w')

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

            #We will add the same addon to the json object for every item that has that addon
            if itemName == 'Keys':
                #We will make a for to add the addon to every key
                for key in keys:
                    json_object['addons'].append({
                        'name': addonName,
                        'item': key,
                        'description': addonDescription,
                        'image': addonImage
                    })
            else:
                for map in maps:
                    json_object['addons'].append({
                        'name': addonName,
                        'item': map,
                        'description': addonDescription,
                        'image': addonImage
                    })
    elif itemName == 'Toolboxes':
        #the addons are in the 4th table with the class "wikitable"
        table = soup.find_all('table', class_='wikitable')[3]


        for tr in table.find_all('tr')[1:]:
            #The name of the addon is inside the <th> tag
            addonName = tr.find_all('th')[1].find('a').text.strip()

            #The description of the addon is inside the <td> tag
            addonDescription = tr.find('td').text.strip()

            #The image of the addon is inside the <img> tag with the class "image-thumbnail"
            addonImage = tr.find_all('th')[0].find('a')['href']

            for tb in Toolboxes:
                json_object['addons'].append({
                    'name': addonName,
                    'item': tb,
                    'description': addonDescription,
                    'image': addonImage
                })

    else:

        #the addons are in the 4th table with the class "wikitable"
        table = soup.find_all('table', class_='wikitable')[4]

        for tr in table.find_all('tr')[1:]:

            #The name of the addon is inside the <th> tag
            addonName = tr.find_all('th')[1].find('a').text.strip()

            #The description of the addon is inside the <td> tag
            addonDescription = tr.find('td').text.strip()

            #The image of the addon is inside the <img> tag with the class "image-thumbnail"
            addonImage = tr.find_all('th')[0].find('a')['href']

            #We will add the addon to the json object
            #We will add the same addon to the json object for every item that has that addon
            #f.e if the itemName is Flashlight
            #We will put the same addon with the name of every flashlight that is inside of items[Flashlights]
            if itemName == 'Flashlights':
                for flashlight in Flashlights:
                    json_object['addons'].append({
                        'name': addonName,
                        'item': flashlight,
                        'description': addonDescription,
                        'image': addonImage
                    })
            else: #itemName == 'Med-Kits':
                for medkit in MedKits:
                    json_object['addons'].append({
                        'name': addonName,
                        'item': medkit,
                        'description': addonDescription,
                        'image': addonImage
                    })




#We will write the json object to the json file
json.dump(json_object, json_file, indent=4)

    










