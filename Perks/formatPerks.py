#In this file we will write the data to the sql file from the json file
#We will use the json file genPerks.json
#
#Path: format_genPerks.py

import pandas as pd
import csv
import json


#We will use the csv file genPerks.csv

def processedRow(line):
    #We will process the row
    #We will write the data to the sql file (replacing the ' with '' to avoid errors)
    #We will get the perk name
    perkName = line['perkName'].replace("'","''")

    #We will get the perk icon
    perkIcon = line['perkIcon'].replace("'","''")

    #We will get the perk description
    perkDesc = line['perkDesc'].replace("'","''")

    #We will get the fromSurvivor
    fromSurvivor = line['fromSurvivor']

    #We will get the fromKiller
    fromKiller = line['fromKiller']

    #We will return the processed row
    return perkName, perkIcon, perkDesc, fromSurvivor, fromKiller

def format_perks(output : str, sql_file : str):
    #We will use the json file genPerks.json
    with open(output, 'r', encoding='utf-8') as f:
        #We will read the json file
        data = json.load(f)


        #We will write the data to the sql file
        with open(sql_file, 'w', encoding='utf-8', newline='\n') as w:
            #We will write the data to the sql file
            for line in data['Perks']:
                #We will process the row
                #after a perk theres a blank row so we will skip that

                if line != '':
                    #We have one complete row string in line so we will process it
                    perkName, perkIcon, perkDesc, fromSurvivor, fromKiller = processedRow(line)

                    
                    w.write("INSERT INTO Perks VALUES('{}','{}','{}',{},{});\n".format(
                        perkName, perkIcon, perkDesc, fromSurvivor, fromKiller))


if __name__ == '__main__':
    format_perks('../resources/survPerks.json', '../database/inserts/survPerks.sql')
    format_perks('../resources/genkillerPerks.json', '../database/inserts/killerPerks.sql')