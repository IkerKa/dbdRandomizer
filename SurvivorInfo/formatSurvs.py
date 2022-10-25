#This file will format the json file survivors.json to the sql file survivors.sql

import pandas as pd
import json


#We will use the json file survivors.json

def processedRow(line):

    survName = line['name'].replace("'","''")
    icon = line['img'].replace("'","''")
    desc = line['desc'].replace("'","''")
    perk1 = line['perk_1s'].replace("'","''")
    perk2 = line['perk_2s'].replace("'","''")
    perk3 = line['perk_3s'].replace("'","''")

    return survName, icon, desc, perk1, perk2, perk3






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
            for line in data['Survivors']:
                if line != '':
                    survName, image, desc, perk1,perk2,perk3 = processedRow(line)
                    w.write("INSERT INTO Survivors VALUES(('{}','{}','{}','{}','{}','{}');\n".format(
                        survName, perk1, perk2, perk3, desc, image))



if __name__ == '__main__':
    formatPerks('../resources/survivorsData.json', '../database/inserts/Survivors.sql')