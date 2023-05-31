
import sys
import requests
from bs4 import BeautifulSoup
import json
import traceback

DEBUG = False
URL = 'https://deadbydaylight.fandom.com/wiki/Shrine_of_Secrets'

# --->Function that access the bot to get the perk names and the time when it refreshes
def get_current_sos():
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')

    pp = soup.find('div', class_='mw-parser-output')
    table = pp.find('table', class_='sosTable')
    inside = table.find_all('tr')[1].find('div')

    # Get the divs with "sosPerk sosPerk1", "sosPerk sosPerk2", "sosPerk sosPerk3", "sosPerk sosPerk4"
    divs = inside.find_all('div', class_='sosPerk')

    if DEBUG:
        print(len(divs))

    # From the second div to the last one, get the perks
    perks = []

    for div in divs:

        # Find first <a> and get the title
        title = div.find('a')['title']
        # There's inside a img with the src
        img = div.find('img')['data-src']

        perks.append({'title': title, 'img': img})

    # Get the time when it refreshes (last tr)

    time = table.find_all('tr')[-1].find('th', class_='sosHeader').find('span').text.strip()

    return {'perks': perks, 'time': time}


def main():
    sos = get_current_sos()

    print(sos)

if __name__ == '__main__':
    main()






