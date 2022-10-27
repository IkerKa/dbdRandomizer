#This script will make an sql file with all the items in the game (now inside the .json file)


import pandas as pd
import json

#INSERT INTO Items VALUES(itemName,itemDescription,itemIcon)




def processedRow(line):
    itemName = line['name'].replace("'","''")
    itemDescription = line['description'].replace("'","''")
    itemIcon = line['image'].replace("'","''")

    return itemName, itemDescription, itemIcon

def formatItems(output : str, sql_file : str):
    with open(output, 'r', encoding='utf-8') as f:
        #We will read the json file
        data = json.load(f)

        #We will write the data to the sql file
        with open(sql_file, 'w', encoding='utf-8', newline='\n') as w:
            #We will write the data to the sql file
            for line in data['items']:
                if line != '':
                    itemName, itemDescription, itemIcon = processedRow(line)
                    w.write("INSERT INTO Items VALUES(('{}','{}','{}');\n".format(
                        itemName, itemDescription, itemIcon))

if __name__ == '__main__':
    formatItems('../resources/items.json', '../database/inserts/Items.sql')