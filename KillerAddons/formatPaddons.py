#This script will make an sql file with all the items in the game (now inside the .json file)


import pandas as pd
import json

#INSERT INTO Power_Addons VALUES(powerAddName,killerName,powerAddDescription,powerAddIcon)

def processedRow(line):
    powerAddName = line['name'].replace("'","''")
    killerName = line['killerName'].replace("'","''")
    powerAddDescription = line['description'].replace("'","''")
    powerAddIcon = line['icon'].replace("'","''")

    return powerAddName, killerName, powerAddDescription, powerAddIcon

def formatPowerAddons(output : str, sql_file : str):
    with open(output, 'r', encoding='utf-8') as f:
        #We will read the json file
        data = json.load(f)

        #We will write the data to the sql file
        with open(sql_file, 'w', encoding='utf-8', newline='\n') as w:
            #We will write the data to the sql file
            for line in data['powerAddons']:
                if line != '':
                    powerAddName, killerName, powerAddDescription, powerAddIcon = processedRow(line)
                    w.write("INSERT INTO Power_Addons VALUES(('{}','{}','{}','{}');\n".format(
                        powerAddName, killerName, powerAddDescription, powerAddIcon))

if __name__ == '__main__':
    formatPowerAddons('../resources/killersAddons.json', '../database/inserts/Power_Addons.sql')