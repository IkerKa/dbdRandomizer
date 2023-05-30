
import requests
from bs4 import BeautifulSoup
import json
import traceback

DEBUG = False
REALM_INFO = False
GET_MAPS = True

#-->The info obtained could be more complete, but it is enough for now (IF WE WANT MORE INFO, WE WILL HAVE TO DO MORE SCRAPPING)

# we will take each realm info from the wiki (we have a json file with the realms names)
json_file = open('../resources/realmsNames.json', 'r')
realmsNames = json.load(json_file)

urls = []
# Take all the urls
for realm in realmsNames['Realms']:
    urls.append(realm['url'])

# Close the json file
json_file.close()

# We will open the json file
json_file = open('../resources/realmsInfo.json', 'w')

# We will create the json object
json_object = {}

json_object['Realms'] = []

# Info: name, lore, image, n_maps, associated killers, location

# We will take the info of each realm

if REALM_INFO:
    for url in urls:

        # Get the html of the page
        try:
            killers = []
            associatedKillers = []

            page = requests.get(url)

            # Print the urls and the name
            if DEBUG:
                print(url)
                print(realmsNames['Realms'][urls.index(url)]['name'])
                print('------------------')

            # Parse the html
            soup = BeautifulSoup(page.content, 'html.parser')

            # -->Principal info
            infoboxtable = soup.find('table', class_='infoboxtable')

            # Tr's of the table
            # Get body
            tbody = infoboxtable.find('tbody')

            # Get all the tr's
            trs = tbody.find_all('tr')

            # If its Autohaven Wreckers
            if DEBUG:
                if realmsNames['Realms'][urls.index(url)]['name'] == 'L\u00e9ry''s Memorial Institute':
                    print('Autohaven Wreckers')
                    print(trs[1].find_all('td')[0].find('a')['href'])
                    killers = trs[3].find_all('a')
                    for killer in killers:
                        # If there are something, we will take it
                        if killer.text.strip() != '':
                            associatedKillers.append('The '+killer.text.strip())

                    print(associatedKillers)
                    print(trs[5].find_all('td')[1].text.strip())
                    print(trs[6].find_all('td')[1].text.strip())

                print(trs[0])

            image = trs[1].find_all('td')[0].find('a')['href']
            # code_name = trs[1].find('td').text.strip()    --> not needed
            # The killers are in the 3rd tr
            killers = trs[3].find_all('a')
            for killer in killers:
                # If there are something, we will take it
                if killer.text.strip() != '':
                    associatedKillers.append('The '+killer.text.strip())

            # -->Lore
            loc = trs[5].find_all('td')[1].text.strip()

            if realmsNames['Realms'][urls.index(url)]['name'] == 'Autohaven Wreckers' or realmsNames['Realms'][urls.index(url)]['name'] == 'Coldwind Farm':

                n_maps = trs[6].find_all('td')[1].text.strip()
            else:
                n_maps = trs[7].find_all('td')[1].text.strip()
            # -->Lore
            # Find an h2 header with the id Lore
            h2 = soup.find('span', id='Lore').parent

            # Find the p after the h2 header
            p = h2.find_next_sibling('p')

            # Find the p's after the first one
            ps = p.find_next_siblings('p')

            # We will take the lore
            lore = p.text.strip()

            # We will take the rest of the lore
            for p in ps:
                lore += p.text.strip()

            # if realmsNames['Realms'][urls.index(url)]['name'] == 'Autohaven Wreckers':
            #     print(lore)

            # Offering ...
            h2 = soup.find('span', id='Offering').parent

            # Find the wiki table and take the name
            offering = h2.find_next_sibling('table').find_all('th')[1].text.strip()




            # --> If its toba landing, we will change the image
            # https://static.wikia.nocookie.net/deadbydaylight_gamepedia_en/images/4/40/IconMap_Uba_Umbralevel01.png/revision/latest/scale-to-width-down/180?cb=20230523155439
            if realmsNames['Realms'][urls.index(url)]['name'] == 'Dvarka Deepwood':
                image = 'https://static.wikia.nocookie.net/deadbydaylight_gamepedia_en/images/4/40/IconMap_Uba_Umbralevel01.png/revision/latest/scale-to-width-down/180?cb=20230523155439'
                lore = 'This Realm does not have a Lore currently.'

            # Store the info in the json object
            json_object['Realms'].append({
                'name': realmsNames['Realms'][urls.index(url)]['name'],
                'image': image,
                'associatedKillers': associatedKillers,
                'location': loc,
                'n_maps': n_maps,
                'lore': lore,
                'offering': offering
            })
        except:
            # Print the name of the realm which has failed
            print(realmsNames['Realms'][urls.index(url)]['name'])
            # Mostrar la traza
            # traceback.print_exc()


    # We will write the json object to the json file
    json.dump(json_object, json_file, indent=4)

    # We will close the json file
    json_file.close()

    # Path: Realms\realmMaps.py

    print('Realms info updated')

if GET_MAPS:
    # We will store in other json all the maps from every realm with its urls to get parsed later
    json_file = open('../resources/realmsMaps.json', 'w')

    json_object = {}
    json_object['Realms'] = []

    # We will take the info of each realm
    for url in urls:
            
            # Get the html of the page
            try:
                page = requests.get(url)

                # print('\n\n')



                soup = BeautifulSoup(page.content, 'html.parser')
    
                # Just for every Realm we are going to get all maps
                # Find the h2 header with the id Map or Maps
                h2 = soup.find('span', id='Lore').parent

                # Take the next h2
                h2 = h2.find_next_sibling('h2')


                mapList = []

                # Just take the map name and generate the url
                # Find the wiki table and take the name
                table = h2.find_next_sibling('table', class_='wikitable')
                tbody = table.find('tbody')
                tds = tbody.find_all('td')
                for td in tds:

                    
                    mapName = td.find('a').text.strip()

                    # We will generate the url
                    mapUrl = 'https://deadbydaylight.fandom.com' + '/wiki/' + mapName.replace(' ', '_')

                    mapList.append({
                        'name': mapName,
                        'url': mapUrl
                    })


                # Store the info in the json object
                json_object['Realms'].append({
                    'name': realmsNames['Realms'][urls.index(url)]['name'],
                    'maps': mapList
                })

                





            except:
                # Print the name of the realm which has failed
                print(realmsNames['Realms'][urls.index(url)]['name'])
                # Mostrar la traza
                # traceback.print_exc()

    # We will write the json object to the json file
    json.dump(json_object, json_file, indent=4)

    # We will close the json file
    json_file.close()

    # Path: Realms\realmMaps.py
    print('Realms maps updated')






