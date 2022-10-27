#This script will make an sql file with all the items in the game (now inside the .json file)


import pandas as pd
import json

#INSERT INTO Offerings VALUES(offerName,description,icon,fromSurvivor,fromKiller)

def processedRow(line):
    offerName = line['name'].replace("'","''")
    description = line['description'].replace("'","''")
    icon = line['icon'].replace("'","''")
    fromSurvivor = line['fromS']
    fromKiller = line['fromK']

    return offerName, description, icon, fromSurvivor, fromKiller

def formatOfferings(output : str, sql_file : str):
    with open(output, 'r', encoding='utf-8') as f:
        #We will read the json file
        data = json.load(f)

        #We will write the data to the sql file
        with open(sql_file, 'w', encoding='utf-8', newline='\n') as w:
            #We will write the data to the sql file
            for line in data['offerings']:
                if line != '':
                    offerName, description, icon, fromSurvivor, fromKiller = processedRow(line)
                    w.write("INSERT INTO Offerings VALUES(('{}','{}','{}',{},{});\n".format(
                        offerName, description, icon, fromSurvivor, fromKiller))

if __name__ == '__main__':
    formatOfferings('../resources/offerings.json', '../database/inserts/Offerings.sql')