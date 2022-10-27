#First there is a reminder:
# We gotta delete the N:M relationship between offerings and Survivors/Killers, bc it's not needed

# This script is for the creation of the offering, we will parse the info from the json file

import json
from bs4 import BeautifulSoup
import requests


url = 'https://deadbydaylight.fandom.com/wiki/Offerings'

page = requests.get(url)
soup = BeautifulSoup(page.text, 'html.parser')

json_file = open('../resources/offerings.json', 'w')

json_object = {}
json_object['offerings'] = []

#offering: name, desc, icon, fromS, fromK

#We will transfer the url info into the json file

#All categories of offerings
table = soup.find_all('table', class_='wikitable')[2]

for tr in table.find_all('tr'):
    #name
    offeringName = tr.find_all('th')[1].find('a').text.strip()

    #desc
    offeringDesc = tr.find('td').text.strip()

    #icon
    offeringIcon = tr.find_all('th')[0].find('a')['href']

    
    #All this offerings are from survs and killers except for one, 
    if offeringName == 'Bound Envelope':
        fromS = 0
        fromK = 1
    else:
        fromS = 1
        fromK = 1

    #We will add the offering to the json object
    json_object['offerings'].append({
        'name': offeringName,
        'description': offeringDesc,
        'icon': offeringIcon,
        'fromS': fromS,
        'fromK': fromK
    })


#Altrusim is in the 3rd table
#Boldness is in the 4th table


for table in soup.find_all('table', class_='wikitable')[3:4]:

    for tr in table.find_all('tr'):
        #name
        offeringName = tr.find_all('th')[1].find('a').text.strip()

        #desc
        offeringDesc = tr.find('td').text.strip()

        #icon
        offeringIcon = tr.find_all('th')[0].find('a')['href']

        
        #All this offerings are from survs and killers except for one, 
       
        fromS = 1
        fromK = 0

        #We will add the offering to the json object
        json_object['offerings'].append({
            'name': offeringName,
            'description': offeringDesc,
            'icon': offeringIcon,
            'fromS': fromS,
            'fromK': fromK
        })


# Brutaality is in the 5th table
# Deviousness is in the 6th table
# Generosity is in the 7th table

for table in soup.find_all('table', class_='wikitable')[5:8]:

    for tr in table.find_all('tr'):
        #name
        offeringName = tr.find_all('th')[1].find('a').text.strip()

        #desc
        offeringDesc = tr.find('td').text.strip()

        #icon
        offeringIcon = tr.find_all('th')[0].find('a')['href']

        
        #All this offerings are from survs and killers except for one, 
       
        fromS = 0
        fromK = 1

        #We will add the offering to the json object
        json_object['offerings'].append({
            'name': offeringName,
            'description': offeringDesc,
            'icon': offeringIcon,
            'fromS': fromS,
            'fromK': fromK
        })


#Objetives

table = soup.find_all('table', class_='wikitable')[8]
for tr in table.find_all('tr'):
    #name
    offeringName = tr.find_all('th')[1].find('a').text.strip()

    #desc
    offeringDesc = tr.find('td').text.strip()

    #icon
    offeringIcon = tr.find_all('th')[0].find('a')['href']

    
    #All this offerings are from survs and killers except for one, 
    
    fromS = 1
    fromK = 0

    #We will add the offering to the json object
    json_object['offerings'].append({
        'name': offeringName,
        'description': offeringDesc,
        'icon': offeringIcon,
        'fromS': fromS,
        'fromK': fromK
    })



table = soup.find_all('table', class_='wikitable')[10]
for tr in table.find_all('tr'):
    #name
    offeringName = tr.find_all('th')[1].find('a').text.strip()

    #desc
    offeringDesc = tr.find('td').text.strip()

    #icon
    offeringIcon = tr.find_all('th')[0].find('a')['href']

    
    #All this offerings are from survs and killers except for one, 
    
    fromS = 0
    fromK = 1

    #We will add the offering to the json object
    json_object['offerings'].append({
        'name': offeringName,
        'description': offeringDesc,
        'icon': offeringIcon,
        'fromS': fromS,
        'fromK': fromK
    })


for table in soup.find_all('table', class_='wikitable')[11:14]:

    for tr in table.find_all('tr'):
        #name
        offeringName = tr.find_all('th')[1].find('a').text.strip()

        #desc
        offeringDesc = tr.find('td').text.strip()

        #icon
        offeringIcon = tr.find_all('th')[0].find('a')['href']

        
        #All this offerings are from survs and killers except for one, 
       
        fromS = 1
        fromK = 1

        #We will add the offering to the json object
        json_object['offerings'].append({
            'name': offeringName,
            'description': offeringDesc,
            'icon': offeringIcon,
            'fromS': fromS,
            'fromK': fromK
        })

for table in soup.find_all('table', class_='wikitable')[14:16]:

    for tr in table.find_all('tr'):
        #name
        offeringName = tr.find_all('th')[1].find('a').text.strip()

        #desc
        offeringDesc = tr.find('td').text.strip()

        #icon
        offeringIcon = tr.find_all('th')[0].find('a')['href']

        
        #All this offerings are from survs and killers except for one, 
       
        fromS = 1
        fromK = 0

        #We will add the offering to the json object
        json_object['offerings'].append({
            'name': offeringName,
            'description': offeringDesc,
            'icon': offeringIcon,
            'fromS': fromS,
            'fromK': fromK
        })

table = soup.find_all('table', class_='wikitable')[16]
for tr in table.find_all('tr'):
    #name
    offeringName = tr.find_all('th')[1].find('a').text.strip()

    #desc
    offeringDesc = tr.find('td').text.strip()

    #icon
    offeringIcon = tr.find_all('th')[0].find('a')['href']

    
    #All this offerings are from survs and killers except for one, 
    
    fromS = 1
    fromK = 1

    #We will add the offering to the json object
    json_object['offerings'].append({
        'name': offeringName,
        'description': offeringDesc,
        'icon': offeringIcon,
        'fromS': fromS,
        'fromK': fromK
    })


table = soup.find_all('table', class_='wikitable')[17]
for tr in table.find_all('tr'):
    #name
    offeringName = tr.find_all('th')[1].find('a').text.strip()

    #desc
    offeringDesc = tr.find('td').text.strip()

    #icon
    offeringIcon = tr.find_all('th')[0].find('a')['href']

    
    #All this offerings are from survs and killers except for one, 
    
    if offeringName == 'Scratched Coin' or offeringName == 'Tarnished Coin':
        fromS = 0
        fromK = 1
    else:
        fromS = 1
        fromK = 0

    #We will add the offering to the json object
    json_object['offerings'].append({
        'name': offeringName,
        'description': offeringDesc,
        'icon': offeringIcon,
        'fromS': fromS,
        'fromK': fromK
    })

table = soup.find_all('table', class_='wikitable')[18]
for tr in table.find_all('tr'):
    #name
    offeringName = tr.find_all('th')[1].find('a').text.strip()

    #desc
    offeringDesc = tr.find('td').text.strip()

    #icon
    offeringIcon = tr.find_all('th')[0].find('a')['href']

    
    #All this offerings are from survs and killers except for one, 
    
   
    fromS = 1
    fromK = 1

    #We will add the offering to the json object
    json_object['offerings'].append({
        'name': offeringName,
        'description': offeringDesc,
        'icon': offeringIcon,
        'fromS': fromS,
        'fromK': fromK
    })

for table in soup.find_all('table', class_='wikitable')[19:20]:

    for tr in table.find_all('tr'):
        #name
        offeringName = tr.find_all('th')[1].find('a').text.strip()

        #desc
        offeringDesc = tr.find('td').text.strip()

        #icon
        offeringIcon = tr.find_all('th')[0].find('a')['href']

        
        #All this offerings are from survs and killers except for one, 
       
        fromS = 1
        fromK = 1

        #We will add the offering to the json object
        json_object['offerings'].append({
            'name': offeringName,
            'description': offeringDesc,
            'icon': offeringIcon,
            'fromS': fromS,
            'fromK': fromK
        })

table = soup.find_all('table', class_='wikitable')[20]
for tr in table.find_all('tr'):
    #name
    offeringName = tr.find_all('th')[1].find('a').text.strip()

    #desc
    offeringDesc = tr.find('td').text.strip()

    #icon
    offeringIcon = tr.find_all('th')[0].find('a')['href']

    
    #All this offerings are from survs and killers except for one, 
    
    if offeringName == 'Petrified Oak':
        fromS = 1
        fromK = 0
    else:
        fromS = 0
        fromK = 1

    #We will add the offering to the json object
    json_object['offerings'].append({
        'name': offeringName,
        'description': offeringDesc,
        'icon': offeringIcon,
        'fromS': fromS,
        'fromK': fromK
    })

table = soup.find_all('table', class_='wikitable')[22]
for tr in table.find_all('tr'):
    #name
    offeringName = tr.find_all('th')[1].find('a').text.strip()

    #desc
    offeringDesc = tr.find('td').text.strip()

    #icon
    offeringIcon = tr.find_all('th')[0].find('a')['href']

    
    #All this offerings are from survs and killers except for one, 
    
    fromS = 0
    fromK = 1

    #We will add the offering to the json object
    json_object['offerings'].append({
        'name': offeringName,
        'description': offeringDesc,
        'icon': offeringIcon,
        'fromS': fromS,
        'fromK': fromK
    })


#starts the pary my dudes 

for table in soup.find_all('table', class_='wikitable')[23:27]:
    tr = table.find_all('tr')[-1]

    #name
    offeringName = tr.find_all('th')[1].find('a').text.strip()

    #desc
    offeringDesc = tr.find('td').text.strip()

    #icon
    offeringIcon = tr.find_all('th')[0].find('a')['href']

    
    #All this offerings are from survs and killers except for one, 
    
    fromS = 1
    fromK = 1

    #We will add the offering to the json object
    json_object['offerings'].append({
        'name': offeringName,
        'description': offeringDesc,
        'icon': offeringIcon,
        'fromS': fromS,
        'fromK': fromK
    })


for table in soup.find_all('table', class_='wikitable')[27:30]:
    for tr in table.find_all('tr'):
        #name
        offeringName = tr.find_all('th')[1].find('a').text.strip()

        #desc
        offeringDesc = tr.find('td').text.strip()

        #icon
        offeringIcon = tr.find_all('th')[0].find('a')['href']

        
        #All this offerings are from survs and killers except for one, 
        
        fromS = 1
        fromK = 1

        #We will add the offering to the json object
        json_object['offerings'].append({
            'name': offeringName,
            'description': offeringDesc,
            'icon': offeringIcon,
            'fromS': fromS,
            'fromK': fromK
        })


table = soup.find_all('table', class_='wikitable')[30]
tr = table.find_all('tr')[-1]

#name
offeringName = tr.find_all('th')[1].find('a').text.strip()

#desc
offeringDesc = tr.find('td').text.strip()

#icon
offeringIcon = tr.find_all('th')[0].find('a')['href']


#All this offerings are from survs and killers except for one, 

fromS = 1
fromK = 1

#We will add the offering to the json object
json_object['offerings'].append({
    'name': offeringName,
    'description': offeringDesc,
    'icon': offeringIcon,
    'fromS': fromS,
    'fromK': fromK
})

for table in soup.find_all('table', class_='wikitable')[32:34]:
    tr = table.find_all('tr')[-1]

    #name
    offeringName = tr.find_all('th')[1].find('a').text.strip()

    #desc
    offeringDesc = tr.find('td').text.strip()

    #icon
    offeringIcon = tr.find_all('th')[0].find('a')['href']


    #All this offerings are from survs and killers except for one, 

    fromS = 1
    fromK = 1

    #We will add the offering to the json object
    json_object['offerings'].append({
        'name': offeringName,
        'description': offeringDesc,
        'icon': offeringIcon,
        'fromS': fromS,
        'fromK': fromK
    })

for table in soup.find_all('table', class_='wikitable')[34:36]:
    for tr in table.find_all('tr'):
        #name
        offeringName = tr.find_all('th')[1].find('a').text.strip()

        #desc
        offeringDesc = tr.find('td').text.strip()

        #icon
        offeringIcon = tr.find_all('th')[0].find('a')['href']

        
        #All this offerings are from survs and killers except for one, 
        
        fromS = 1
        fromK = 1

        #We will add the offering to the json object
        json_object['offerings'].append({
            'name': offeringName,
            'description': offeringDesc,
            'icon': offeringIcon,
            'fromS': fromS,
            'fromK': fromK
        })

table = soup.find_all('table', class_='wikitable')[35]

tr = table.find_all('tr')[-1]
#name
offeringName = tr.find_all('th')[1].find('a').text.strip()

#desc
offeringDesc = tr.find('td').text.strip()

#icon
offeringIcon = tr.find_all('th')[0].find('a')['href']


#All this offerings are from survs and killers except for one, 

fromS = 1
fromK = 1

#We will add the offering to the json object
json_object['offerings'].append({
    'name': offeringName,
    'description': offeringDesc,
    'icon': offeringIcon,
    'fromS': fromS,
    'fromK': fromK
})

for table in soup.find_all('table', class_='wikitable')[36:40]:
    for tr in table.find_all('tr'):
        #name
        offeringName = tr.find_all('th')[1].find('a').text.strip()

        #desc
        offeringDesc = tr.find('td').text.strip()

        #icon
        offeringIcon = tr.find_all('th')[0].find('a')['href']

        
        #All this offerings are from survs and killers except for one, 
        
        fromS = 1
        fromK = 1

        #We will add the offering to the json object
        json_object['offerings'].append({
            'name': offeringName,
            'description': offeringDesc,
            'icon': offeringIcon,
            'fromS': fromS,
            'fromK': fromK
        })

table = soup.find_all('table', class_='wikitable')[40]

for tr in table.find_all('tr'):
    #name
    offeringName = tr.find_all('th')[1].find('a').text.strip()

    #desc
    offeringDesc = tr.find('td').text.strip()

    #icon
    offeringIcon = tr.find_all('th')[0].find('a')['href']

    fromS = 1
    fromK = 1

    #We will add the offering to the json object
    json_object['offerings'].append({
        'name': offeringName,
        'description': offeringDesc,
        'icon': offeringIcon,
        'fromS': fromS,
        'fromK': fromK
    })


table = soup.find_all('table', class_='wikitable')[41]

for tr in table.find_all('tr'):
    #name
    offeringName = tr.find_all('th')[1].find('a').text.strip()

    #desc
    offeringDesc = tr.find('td').text.strip()

    #icon
    offeringIcon = tr.find_all('th')[0].find('a')['href']

    if offeringName == 'Shroud of Separation':
        fromS = 0
        fromK = 1
    else:
        fromS = 1
        fromK = 0

    #We will add the offering to the json object
    json_object['offerings'].append({
        'name': offeringName,
        'description': offeringDesc,
        'icon': offeringIcon,
        'fromS': fromS,
        'fromK': fromK
    })

table = soup.find_all('table', class_='wikitable')[43]

for tr in table.find_all('tr'):

    #the first tr is from every one,
    #the second is from killers
    #the third is from survivors
    
    #name
    offeringName = tr.find_all('th')[1].find('a').text.strip()

    #desc
    offeringDesc = tr.find('td').text.strip()

    #icon
    offeringIcon = tr.find_all('th')[0].find('a')['href']

    if offeringName == 'Sacrificial Ward':
        fromS = 1
        fromK = 1
    elif offeringName == 'Black Ward':
        fromS = 0
        fromK = 1
    else:
        fromS = 1
        fromK = 0

    #We will add the offering to the json object
    json_object['offerings'].append({
        'name': offeringName,
        'description': offeringDesc,
        'icon': offeringIcon,
        'fromS': fromS,
        'fromK': fromK
    })


#my goofy ahh code is done, now we will save the json object to a file

#We will write the json object into the json file
json.dump(json_object, json_file, indent=4)