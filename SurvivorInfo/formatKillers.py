#This file will format the json file killersData.json to the sql file killers.sql
import pandas as pd
import json

def processedRow(line):

    killerName = line['name'].replace("'","''")
    icon = line['image_k'].replace("'","''")
    desc = line['mainHability'].replace("'","''")
    perk1 = line['perk_1k'].replace("'","''")
    perk2 = line['perk_2k'].replace("'","''")
    perk3 = line['perk_3k'].replace("'","''")

    return killerName, icon, desc, perk1, perk2, perk3






"""

The insert statement will be:

(survName, perk1,perk2,perk3,desc,image)

file: survivorsData.sql

"""

def formatPerks(output : str, sql_file : str):
    with open(output, 'r', encoding='utf-8') as f:
        #We will read the json file
        data = json.load(f)

        #We will write the data to the sql file
        with open(sql_file, 'w', encoding='utf-8', newline='\n') as w:
            #We will write the data to the sql file
            for line in data['Killers']:
                if line != '':
                    killerName, image, desc, perk1,perk2,perk3 = processedRow(line)
                    w.write("INSERT INTO Killers VALUES(('{}','{}','{}','{}','{}','{}');\n".format(
                        killerName, perk1, perk2, perk3, desc, image))



if __name__ == '__main__':
    formatPerks('../resources/killersData.json', '../database/inserts/Killers.sql')