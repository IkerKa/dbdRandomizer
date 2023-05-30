
import requests
from bs4 import BeautifulSoup
import json


#we will take the items from the wiki
url = "https://deadbydaylight.fandom.com/wiki/Realms"

#we will take the html of the page
page = requests.get(url)

#we will parse the html
soup = BeautifulSoup(page.content, 'html.parser')

#we will open the json file
json_file = open('../resources/realmsNames.json', 'w')

#we will create the json object
json_object = {}

json_object['Realms'] = []

# In the json file we will store all the realms names to access them later

# The realms are h3 headers after a h2 > span header with Realms_&_Maps id
# The first realm is the 1st h3 header after the h2 header
h2 = soup.find('span', id='Realms_&_Maps').parent

# We will take the first h3 header after the h2 header
h3 = h2.find_next_sibling('h3')

# We will take all the h3 headers after the first one
h3s = h3.find_next_siblings('h3')

# We will take the name of the first realm
realmName = h3.text.strip()

# We will add the name of the first realm to the json object
json_object['Realms'].append({
    'name': realmName,
    'url' : 'https://deadbydaylight.fandom.com/wiki/' + realmName.replace(' ', '_')
})

# We will take the name of the rest of the realms
for h3 in h3s:
    realmName = h3.text.strip()

    # Stop
    if realmName == "Recurrent Structures":
        break

    if realmName == "Léry's Memorial Institute":
        realmName = "Léry's Memorial Institute"
        

    # We will add the name of the realm to the json object
    json_object['Realms'].append({
        'name': realmName,
        'url' : 'https://deadbydaylight.fandom.com/wiki/' + realmName.replace(' ', '_')
    })

    

# We will write the json object to the json file
json.dump(json_object, json_file, indent=4)

# We will close the json file
json_file.close()

print("Realms names taken!")

