#With this script we will take all the items from the wiki and put then into a json file

#we will take:

# - the name of the item
# - the description of the item
# - the image of the item

# We will have a distinction between the item rarity, we will put them all

#the craftable-limited wont be included




#POSSIBLE UPDATES: QUIT THE SPECIAL-EVENT ITEMS BC THEY ARE NOT IN THE GAME OR THE PLAYERS CANT GET THEM


import requests
from bs4 import BeautifulSoup
import json


#we will take the items from the wiki
url = "https://deadbydaylight.fandom.com/wiki/Items"

#we will take the html of the page
page = requests.get(url)

#we will parse the html
soup = BeautifulSoup(page.content, 'html.parser')

#we will open the json file
json_file = open('../resources/items.json', 'w')

#we will create the json object
json_object = {}

json_object['items'] = []

#To make an easier way to get the items we will take the items for category
#All the items are inside a table with the class "wikitable"

#The items are inside a <tr> tag (except someones that represent the header of the item-category)


#First we have the firecrackers


#They start in the 10th row and ends in the 13th row
#print("Taking the firecrackers...")
for tr in soup.find_all('table', class_='wikitable')[1].find_all('tr')[10:13]:
    #The name of the item is inside a <th> tag
    itemName = tr.find_all('th')[1].find('a').text.strip()
    #The description of the item is inside a <td> tag (except the first <b>)
    itemDescription = tr.find('td').text.strip()

    #The image of the item is inside a <img> tag with the class "image-thumbnail"
    itemImage = tr.find_all('th')[0].find('a')['href']
    

    #We will add the item to the json object
    json_object['items'].append({
        'name': itemName,
        'description': itemDescription,
        'image': itemImage
    })


#print("Firecrackers taken!")
#print("Taking the flashlights...")

for tr in soup.find_all('table', class_='wikitable')[1].find_all('tr')[15:21]:

    itemName = tr.find_all('th')[1].find('a').text.strip()
    itemDescription = tr.find('td').text.strip()
    itemImage = tr.find_all('th')[0].find('a')['href']

    json_object['items'].append({
        'name': itemName,
        'description': itemDescription,
        'image': itemImage
    })

#print("Flashlights taken!")
#print("Taking the keys...")

for tr in soup.find_all('table', class_='wikitable')[1].find_all('tr')[23:26]:

    itemName = tr.find_all('th')[1].find('a').text.strip()
    itemDescription = tr.find('td').text.strip()
    itemImage = tr.find_all('th')[0].find('a')['href']

    json_object['items'].append({
        'name': itemName,
        'description': itemDescription,
        'image': itemImage
    })

#print("Keys taken!")
#print("Taking the maps...")

for tr in soup.find_all('table', class_='wikitable')[1].find_all('tr')[28:30]:

    itemName = tr.find_all('th')[1].find('a').text.strip()
    itemDescription = tr.find('td').text.strip()
    itemImage = tr.find_all('th')[0].find('a')['href']

    json_object['items'].append({
        'name': itemName,
        'description': itemDescription,
        'image': itemImage
    })

#print("Maps taken!")
#print("Taking the medkits...")

for tr in soup.find_all('table', class_='wikitable')[1].find_all('tr')[32:39]:

    itemName = tr.find_all('th')[1].find('a').text.strip()
    itemDescription = tr.find('td').text.strip()
    itemImage = tr.find_all('th')[0].find('a')['href']

    json_object['items'].append({
        'name': itemName,
        'description': itemDescription,
        'image': itemImage
    })

#print("Medkits taken!")
#print("Taking the toolBoxes...")

for tr in soup.find_all('table', class_='wikitable')[1].find_all('tr')[41:50]:

    itemName = tr.find_all('th')[1].find('a').text.strip()
    itemDescription = tr.find('td').text.strip()
    itemImage = tr.find_all('th')[0].find('a')['href']

    json_object['items'].append({
        'name': itemName,
        'description': itemDescription,
        'image': itemImage
    })

#print("Toolboxes taken!")

#dump the json object into the json file
json.dump(json_object, json_file, indent=4)








