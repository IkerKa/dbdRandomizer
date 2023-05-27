<h1 align="center">
  <br>
  <a><img src="https://static.wikia.nocookie.net/shipping/images/2/24/Dead_by_Daylight_-_Logo.png/revision/latest?cb=20210916200805&path-prefix=es" alt="Proyecto 1" width="200"></a>
    <br>
    🤖Dead by Daylight Randomizer🤖
    <br>
    A fanBot of Dead by Daylight by NopeIsDope ( Iker )
</h1>

<h4 align="center" >
A randomizer for the game Dead By Daylight (DBD) that allows you to play with random perks, add-ons, offerings, and more!
The name of the proyect its provisional, it can change in the future.
</h4>

<h2 align="center">This bot is currently in development and is not yet ready for use!!!.</h2>

## **Table of Contents📋**
<!--ts-->
   * [Table of Contents📋](#table-of-contents)
   * [About📖](#about)
   * [Getting Started🚀](#getting-started)
      * [Prerequisites📋](#prerequisites)
      * [Installing🔧](#installing)
   * [Commands⚙️](#Commands)
   * [Deployment📦](#deployment)
   * [Built With🛠️](#built-with)
   * [Contributing🖇️](#contributing)
   * [Versioning📌](#versioning)
   * [Authors✒️](#authors)
   * [License📄](#license)
   * [Acknowledgments🎁](#acknowledgments)


## **About📖**


## **Getting Started🚀**

1. When the bot is added to your server, type `!dbd` to get a list of commands of all the features of the bot.
2. Type `!dbd help` to get a list of commands.
3. Type `!dbd help <command>` to get more information about a specific command.
4. Type `!dbd <command>` to use a command.

### **Prerequisites📋**
To run the bot in its final version you will need to have installed Discord. You can download it from the following link: https://discord.com/download

But, if you want to check the bot in its development phase (its in Github free to admire 🫣) you will need to have installed:
* [Node.js](https://nodejs.org/es/download/)
* [Visual Studio Code](https://code.visualstudio.com/download)
* [Python](https://www.python.org/downloads/)
  * [BeautifulSoup](https://pypi.org/project/beautifulsoup4/)
  * [Requests](https://pypi.org/project/requests/)
  * [Pandas](https://pypi.org/project/pandas/)
  * [Numpy](https://pypi.org/project/numpy/)
  * [Discord.py](https://pypi.org/project/discord.py/)
  * [json](https://pypi.org/project/json/)
*[Docker-Compose](https://docs.docker.com/compose/install/)

Reminder: Its under license, so you can't use it for commercial purposes. And its a personal project, so it can be changed or deleted at any time. If you suggest something, I will be happy to listen to you but its the author's decision to accept or not the suggestion.

### **Installing🔧**
To install the bot you will need to download the files from the repository. You can do it by downloading the zip file or by cloning the repository with the following command:
```
git clone
```

Reminder: As said before, you can download to see and test by yourself the bot, but you can't redistribute it or use it for commercial purposes.

## **Commands⌨️**
ALL OF THEM STARTS WITH `!dbd <command>`

### **General**

- `help` - Get a list of commands or more information about a specific command.
- `dbd about <command>` - Get information about a command. (Commands with a second argument aren't available at the moment.) 

- `help` - Get an introduction to the bot
- `commands` - Get a list of commands
- `randomPerk` - Get a random perk info with its owner                                                          *(completed)*
- `perk <name>` - Get information about a specific perk                                                         *(completed)*
- `simplePerk` - Get a random perk name and image                                                               *(completed)*
- `randomAddOn` - Get a random add-on                                                                           *(completed)*
- `addon <addonName>` - Get information about a specific add-on                                                 *(completed)*
- `survivor` - Get a random survivor                                                                            *(completed)*
- `survivor <name>` - Get information about a specific survivor                                                 *(completed)*
- `offering <name>?` - Get information about a specific offering                                                *(completed)*
- `perksof <survivor/killer>` - Get the 3 perks of a survivor or killer                                         *(completed)*
- `item <itemName?>` - Get a variety-random item (f.e medkit, toolbox, etc.) with the information about it.     *(completed)*
    for example: `!dbd item` : green toolbox and its information
- `killer` - Get a random killer                                                                                *(completed)*
- `killer <name>` - Get information about a specific killer (pending)
- `perkCombos survivor` - Get a random perk combo of 4 perks to use on a survivor                               *(completed)*
- `perkCombos killer` - Get a random perk combo of 4 perks to use on a killer                                   *(completed)*
- `preMatch survivor` - Get a random pre-match lobby setup (including 4 perks (from the survivors), 1 item (with 2 add-ons), 1 offering, and 1 survivor)
- `preMatch killer` - Get a random pre-match lobby setup (including 4 perks (from the killers), 1 item (with 2 add-ons), 1 offering, and 1 killer)

--coming soon--

- `authors` - Get a list of all authors of the bot with its favorite perk, survivor, killer, item and its github link
- `sugestedPerkCombos` - Get a random sugested perk combo of 4 perks to use
- `randomObjetive` - Get a random objetive to do in the match
        -Example: `!dbd randomObjetive` : "do 4 beamer saves in a match" (easy to do in the tutorial of discord bot (inspirational messages))
- `randomMap` - Get a random map
- `map <name>` - Get information about a specific map
- `maplist` - Get a list of all maps
- `shrine` - Get the current shrine of secrets

--Future updates--
- `bingo` - Get a list of objectives. Two players can enter a room, first to complete a line wins.
- `quizz game` - Get a list of questions. Two players can enter a room, first to complete the quizz wins.
  p.e: "What is the name of the killer that has a chainsaw?" (answer: Leatherface/Hillbilly) or "Perk that allows you to see the aura of the killer when you are hooked?" (answer: Kindred)
  -The question can be filtered by category (perks, killers, survivors, items, etc.)
- Verify/format commands to make them more user-friendly (case insensitive, spaces, etc.)

- `hallOfFame` - Get a list of the best players of the bot (with the most points) 
- `points` - Get the points of a player
- `leaderboard` - Get a list of the best players of the bot (with the most points)
- `mostPlayed` - Get a list of the most played killers, survivors, perks, items, etc.
- `mostPlayed <killer/survivor/perk/item>` - random killer/survivor/perk/item that is the most played
- `mostPlayed <killer/survivor/perk/item> <name>` - Get a list of the most played killers, survivors, perks, items, etc.
- `mostSearched` - Get a list of the most searched killers, survivors, perks, items, etc.

- `<sth> list` - Get a list of N <sth> (killer, survivor, perk, item, etc.)

- `promoCodes` - Get a list of promo codes (to earn BP, shards, etc.)

- `randomBuild` - Get a random build (killer or survivor)

- `randomPerkBuild` - Get a random perk build (killer or survivor)





## **Entity Relationalship Diagram (ERD)📊**
#### *Final Version*
![ERD](Images/dbdRandomizerER.jpg)

## **Support📞**
<details>
  <summary>Click to expand!</summary>
  
  If you need help with the bot, you can contact me on Discord: `NopeIsDope#0001`

  You can also join the support server: [Click here](https://discord.gg/4Z7Z9Z9)

  I'm also open to suggestions, so if you have any, you can contact me on Discord or join the support server and tell me there.

  You can contact with the other authors of the bot on Discord (click on the authors command to get their Discord tag).

</details>


## **Credits📝**
- [DeadByDaylight](https://deadbydaylight.com/) - The game Dead By Daylight
- [DeadByDaylight Wiki](https://deadbydaylight.gamepedia.com/Dead_by_Daylight_Wiki) - The wiki for the game Dead By Daylight
- [DeadByDaylight API]() - The API for the game Dead By Daylight    

## **Authors👨‍💻**
- [Iker Morán](https://github.com/IkerKa) - The main author of the bot
### **Contributors**
- [Juan Carrasquer](https://github.com/fortaleza2001) - (pending)
- [Darío Marcos](//gitlink) - (pending)

## **License📜**
This project is under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
If you want to use this code, please give credits to the authors. Thanks! :) 


## **Disclaimer⚠️**
This bot is not affiliated with Dead By Daylight or Behaviour Interactive in any way. All trademarks are the property of their respective owners.
At this moment the bot will be for personal use.

## **Changelog📝**
<details>
  <summary>Click to expand!</summary>
  
### **vPre-0.0.0**
Brainstorming and planning the project.

### **vPre-0.0.1**
Created the repository and the README.md file.

### **vPre-0.0.2**
Created the ERD and added it to the README.md file.
SQL database created.

### **vPre-0.0.1.2**
Added the license to the README.md file.
Programmed the commands `!dbd about <command>` and `!dbd help <command>`.
At the moment commands with a second argument aren't available.

### **vPre-0.0.2**
Programmed the commands `!dbd help` and `!dbd commands`.
Added new commands ideas to the README.md file.

### **vPre-0.0.3**
Added Iker and Juan selected setup command

### **vPre-0.0.4**
First commit to the repository.
Added the bot to the support server.
Added the github link to the README.md file.

### **vPre-0.0.5**
Brainstorming to take the data from the wiki.

### **vPre-0.0.6**
Start scraping the wiki.

### **vPre-0.1.0**
Scraped all perks data from the wiki.

### **vPre-0.1.0.1**
Scraped all add-ons data from the wiki.
Scraped all offerings data from the wiki.
Scraped all the items data from the wiki.
Scraped all the people data from the wiki.

### **vPre-0.1.1**
All data scrapped from the wiki.

### **vPre-0.2.0**
Sql files created.
Formatted the files and making the workspace structured.

### **vPre-0.2.1**
Checking the sql inserts (1st check: SQL number of entries is correct)

### **vPre-0.2.1.1**
Checking the sql inserts (order of insertion as the creation of the tables in progress..)


</details>

## **To-Do List📝**
<details>
  <summary>Click to expand!</summary>

- [x] Create the repository and the README.md file.
- [x] Create the ERD and add it to the README.md file.
- [x] SQL database created.
- [x] Add the license to the README.md file.
- [x] Programmed the commands `!dbd about <command>` and `!dbd help <command>`.
- [x] At the moment commands with a second argument aren't available.
- [x] Programmed the commands `!dbd help` and `!dbd commands`.
- [x] Added new commands ideas to the README.md file.
- [x] Added Iker and Juan selected setup command
- [x] First commit to the repository.
- [x] Added the bot to the support server.
- [x] Added the github link to the README.md file.
- [x] Brainstorming to take the data from the wiki.
- [x] Start scraping the wiki.
- [x] Scraped all perks data from the wiki.
- [x] Scraped all add-ons data from the wiki.
- [x] Scraped all offerings data from the wiki.
- [x] Scraped all the items data from the wiki.
- [x] Scraped all the people data from the wiki.
- [x] All data scrapped from the wiki.
- [x] Sql files created.
- [x] Formatted the files and making the workspace structured.
- [x] Checking the sql inserts (1st check: SQL number of entries is correct)
- [x] Checking the sql inserts (order of insertion as the creation of the tables in progress..)
- [ ] Checking the sql inserts (2nd check: SQL number of entries is correct)
- [...] 

</details>

## **Contributing🤝**
This is actually a non-profit project and also a private project, so currently I'm not accepting contributions 😢.


## **Donate🤑**
**No!** This is a non-profit project and also a private project, so we don't accept any donations.

## **Acknowledgments🎁**