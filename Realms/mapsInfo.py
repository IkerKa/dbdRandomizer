
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

                lore = ""

                
                # Associated realm
                associated_realm = trs[3].find_all('td')[1].text.strip()

                mapsLayout = [] #Maybe there are more than one map layout

                  # --> Special cases
                if url == 'https://deadbydaylight.fandom.com/wiki/The_Game' or url== 'https://deadbydaylight.fandom.com/wiki/Midwich_Elementary_School':
                    
                    tile_area = trs[4].find_all('td')[1].text.strip()
                    map_area = trs[5].find_all('td')[1].text.strip()

                    mapsLayout.append(map_layout)

                    # Check if there are more tr's
                    if len(trs) > 9:
                        # We will take the rest of the map layouts
                        for i in range(12, len(trs)):
                            map_layout = trs[i].find('td').find('a')['href']
                            mapsLayout.append(map_layout)

                        
                    # print("MAP LAYOUT: ", mapsLayout)


                elif url=='https://deadbydaylight.fandom.com/wiki/Toba_Landing' or url == 'https://deadbydaylight.fandom.com/wiki/Raccoon_City_Police_Station_East_Wing' or url == 'https://deadbydaylight.fandom.com/wiki/Raccoon_City_Police_Station_West_Wing' or url == 'https://deadbydaylight.fandom.com/wiki/Raccoon_City_Police_Station':
                    
                    if url == 'https://deadbydaylight.fandom.com/wiki/Raccoon_City_Police_Station':
                        # Start lore with the first paragraph
                        lore = "[THIS MAP HAS BEEN SPLIT INTO TWO PARTS AND THIS VERSION IS NO LONGER IN THE GAME: EAST WING AND WEST WING]\n\n"
                    
                    tile_area = "Unknown"
                    map_area = "Unknown"

                    mapsLayout.append(map_layout)

                    # Check if there are more tr's
                    if len(trs) > 9:
                        # We will take the rest of the map layouts
                        for i in range(9, len(trs)):
                            map_layout = trs[i].find('td').find('a')['href']
                            mapsLayout.append(map_layout)

                        
                    # print("MAP LAYOUT: ", mapsLayout)



                else:

                    #-->Map layout
                    tile_area = trs[4].find_all('td')[1].text.strip()
                    map_area = trs[5].find_all('td')[1].text.strip()
                    map_layout = trs[8].find('td').find('a')['href']
                    mapsLayout.append(map_layout)

                    # print("------------------", len(trs))

                    # Check if there are more tr's
                    if len(trs) > 9:
                        # We will take the rest of the map layouts
                        for i in range(11, len(trs)):
                            map_layout = trs[i].find('td').find('a')['href']
                            mapsLayout.append(map_layout)


                # Lore

                try:

                    h2 = soup.find('span', id='Lore').parent

                    # Find the p after the h2 header
                    p = h2.find_next_sibling('p')

                    # Find the p's after the first one
                    ps = p.find_next_siblings('p')

                    # We will take the lore
                    lore += p.text.strip()

                    # We will take the rest of the lore
                    for p in ps:
                        lore += p.text.strip()

                except:


                    contenido = soup.find('div', class_='mw-parser-output')
                    # Buscar la siguiente tabla
                    table = contenido.find('table', style='background:transparent')

                    # Buscar el contenido
                    desc = table.find('tbody').find_all('tr')[0].find_all('td')[1].text.strip()

                    lore = desc


                        



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
                    'map_layout': mapsLayout,
                    'description': lore
                })


                
    
            except:
                print("Error en la url: ", url)
                # print("Error: ", traceback.print_exc())

    # We will write the json object in the json file
    json.dump(json_object, json_file, indent=4)

    # Close the json file
    json_file.close()