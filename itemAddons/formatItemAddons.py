#This script will make an sql file with all the items in the game (now inside the .json file)


import pandas as pd
import json

#INSERT INTO Item_Addons VALUES(addonName,itemName,addonDescription,addonIcon)

def processedRow(line):
    addonName = line['name'].replace("'","''")
    itemName = line['item'].replace("'","''")
    addonDescription = line['description'].replace("'","''")
    addonIcon = line['image'].replace("'","''")

    return addonName, itemName, addonDescription, addonIcon

def formatItemAddons(output : str, sql_file : str):
    with open(output, 'r', encoding='utf-8') as f:
        #We will read the json file
        data = json.load(f)

        #We will write the data to the sql file
        with open(sql_file, 'w', encoding='utf-8', newline='\n') as w:
            #We will write the data to the sql file
            for line in data['addons']:
                if line != '':
                    addonName, itemName, addonDescription, addonIcon = processedRow(line)
                    w.write("INSERT INTO Item_Addons VALUES(('{}','{}','{}','{}');\n".format(
                        addonName, itemName, addonDescription, addonIcon))

if __name__ == '__main__':
    formatItemAddons('../resources/addonsRwrk.json', '../database/inserts/Item_Addons.sql')
