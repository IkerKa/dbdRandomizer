
import sys
import requests
from bs4 import BeautifulSoup
import json
import traceback

DEBUG = False
MAP_INFO = True

#-->The info obtained could be more complete, but it is enough for now (IF WE WANT MORE INFO, WE WILL HAVE TO DO MORE SCRAPPING)

# --->PENDING FILE.

# First we will take the map names and its realm associated
json_file = open('../resources/realmsMaps.json', 'r')
realmsMaps = json.load(json_file)

# Close the json file
json_file.close()

# We will open the json file
json_file = open('../resources/mapsInfo.json', 'w')

# We will create the json object
json_object = {}

json_object['Maps'] = []

# Info: name, lore, image, map_layout, associated_realm, area, (tile area?)

# Get maps urls
urls = []
for realm in realmsMaps['Realms']:
    for map in realm['maps']:
        urls.append(map['url'])



# We will take the info of each map
print("MAPS INFO")
if MAP_INFO:
    
    for url in urls:
            
            # Get the html of the page
            try:

                page = requests.get(url)
    
                # Print the urls and the name
                if DEBUG:
                    print(url)
                    print('------------------')
                    print('\n\n')
    
                # Parse the html
                soup = BeautifulSoup(page.content, 'html.parser')
    
                # -->Principal info
                infoboxtable = soup.find('table', class_='infoboxtable')
    
                # Tr's of the table
                # Get body
                tbody = infoboxtable.find('tbody')
    
                # Get all tr's
                trs = tbody.find_all('tr')
    
                # Name
                name = trs[0].find('td').text.strip()

                # Image
                image = trs[1].find('a')['href']

                
                # Associated realm
                associated_realm = trs[3].find_all('td')[1].text.strip()


                #-->Map layout
                tile_area = trs[4].find_all('td')[1].text.strip()
                map_area = trs[5].find_all('td')[1].text.strip()
                map_layout = trs[8].find('td').find('a')['href']

                # Lore
                h2 = soup.find('span', id='Lore').parent

                # Si no tiene lore
                if h2 == None:
                    contenido = soup.find('div', id='mw-parser-output')
                    # Buscar la siguiente tabla
                    table = contenido.find('table')
                    # Buscar el contenido
                    desc = table.find('tbody').find_all('tr')[0].find_all('td')[1].text.strip()
                    lore = desc

                else:   
                    # Find the p after the h2 header
                    p = h2.find_next_sibling('p')

                    # Find the p's after the first one
                    ps = p.find_next_siblings('p')

                    # We will take the lore
                    lore = p.text.strip()

                # We will take the rest of the lore
                for p in ps:
                    lore += p.text.strip()
                    



                if DEBUG:
                    print("Name: ", name)
                    print("Image: ", image)
                    print("Tile Area: ", tile_area)
                    print("Map Area: ", map_area)
                    print("Map Layout: ", map_layout)
                    # print("Lore: ", lore)


                # We will create the json object
                json_object['Maps'].append({
                    'name': name,
                    'image': image,
                    'associated_realm':  associated_realm,
                    'tile_area': tile_area,
                    'map_area': map_area,
                    'map_layout': map_layout,
                    'lore': "a"
                })


                
    
            except:
                print("Error en la url: ", url)
                # print("Error: ", traceback.print_exc())

    # We will write the json object in the json file
    json.dump(json_object, json_file, indent=4)

    # Close the json file
    json_file.close()