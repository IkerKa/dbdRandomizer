import os
import discord
#the import below is for the database
import sqlite3
import sys
#the import below is for the api
import requests
import json
import random
# to the environment variables
import dotenv
from dotenv import load_dotenv
# to convert the image to bytes
import io
#modify images
#from PIL import Image



load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

intent = discord.Intents.default()
intent.members = True
intent.message_content = True


# start the dbdRandomizer
client = discord.Client(intents=intent)


# DATABASE??

# text format for the !commands
# parameters: boolean for the command
# return: string with the text
# if boolean is true, we show all the commands
# if boolean is false, we show the command of the parameter
def formatCommands(indv,command):
  #We have all the commands on the readme file
  #We will use the discord markdown to format the text

  #We return a string with bold titles and italic description
  retex_0   =  "**!dbd help** - *Get an introduction to the bot*\n" 
  retex_1   =   "**!dbd commands** - *Get a list of commands*\n"
  retex_2   =   "**!dbd perk survivor** - *Get a random perk from the survivors with the information about it.*\n"
  retex_3   =   "**!dbd perk killer** - *Get a random perk from the killers with the information about it.*\n"
  retex_4   =   "**!dbd addon** - *Get a random add-on with the information about it.*\n"
  retex_5   =   "**!dbd offering** - *Get a random offering with the information about it.*\n"
  retex_6   =   "**!dbd survivor** - *Get a random survivor*\n"
  retex_7   =   "**!dbd killer** - *Get a random killer*\n"
  retex_8   =   "**!dbd survivor <name>** - *Get information about a specific survivor (specific perks) (pending)*\n"
  retex_9   =   "**!dbd killer <name>** - *Get information about the power of a specific killer (pending)*\n"
  retex_10  =   "**!dbd survivorlist**- *Get a list of all survivors*\n"
  retex_11  =   "**!dbd killerlist** - *Get a list of all killers*\n"
  retex_12  =   "**!dbd perkCombo** - *Get a random perk combo of 4 perks to use*\n"
  retex_13  =   "**!dbd preMatch survivor** - *Get a random pre-match lobby setup (including 4 perks (from the survivors), 1 item (with 2 add-ons), 1 offering, and 1 survivor)*\n"
  retex_14  =   "**!dbd preMatch killer** - *Get a random pre-match lobby setup (including 4 perks (from the killers), 1 item (with 2 add-ons), 1 offering, and 1 killer)*\n"
  retex_15  =   "**!dbd item** - *Get a variety-random item (f.e medkit, toolbox, etc.) with the information about it. (pending)*\n"
  retex_16  =   "**!dbd item <color>** - *Get a random item (f.e medkit, toolbox, etc.) with the color you specified (pending)*\n"

   # We concatenate all the strings
  if indv == True:
    retex = retex_0 + retex_1 + retex_2 + retex_3 + retex_4 + retex_5 + retex_6 + retex_7 + retex_8 + retex_9 + retex_10 + retex_11 + retex_12 + retex_13 + retex_14 + retex_15 + retex_16
    return retex
  else:
    if command == "help":
      return retex_0
    elif command == "commands":
      return retex_1
    elif command == "perk survivor":
      return retex_2
    elif command == "perk killer":
      return retex_3
    elif command == "addon":
      return retex_4
    elif command == "offering":
      return retex_5
    elif command == "survivor":
      return retex_6
    elif command == "killer":
      return retex_7
    elif command == "survivorlist":
      return retex_10
    elif command == "killerlist":
      return retex_11
    elif command == "perkCombo":
      return retex_12
    elif command == "preMatch survivor":
      return retex_13
    elif command == "preMatch killer":
      return retex_14
    elif command == "item":
      return retex_15
    else:
      return "Command not found"


# This is to check the API examples
def get_one_random_perk():
    # get a random perk from the api
    response = requests.get("https://dead-by-api.herokuapp.com/api/perks/surv/random")
    # get the json data
    json_data = json.loads(response.text)

    #print(json_data)
   
    # we get the name of the perk
    # {'status': 'success', 'results': 1, 'data': [{'_id': '62d5cf44754ff04cb8ebb4e7', 'id': 18, 'name': 'This Is Not Happening'
    perk_name = json_data['data'][0]['name']
    # we get the description of the perk
    perk_description = json_data['data'][0]['description']
    # we get the icon of the perk
    perk_icon = json_data['data'][0]['icon']

    # We will show the icon of the perk on discord
    # we need to get the image from the url
    # we will use the requests library to get the image
    # we will use the content attribute to get the image
    # we will use the bytes() function to convert the image to bytes
    # we will use the discord.File() function to convert the image to a discord file
    
    # First we got the icon in not bytes so we need to convert it to bytes
    
    perk_icon_bytes = bytes(requests.get(perk_icon).content)

    # We will return perk_icon_bytes

    # We now concatenate the name, description and rarity of the perk
    # With the titles in bold and the description in italic
    # We will use the discord markdown to do that

    perk_info = f"**{perk_name}**\n*{perk_description}*"

    return perk_info, perk_icon_bytes



# Get Juan setup:
# It includes his favurite survivor
# His top 3 perks (from the survivors)
# Favourite item
# Favourite map

def get_juan_setup():
  # We will get the survivor
  # We will get the perks
  # We will get the item
  # We will get the map

  # All of them will be returned in different variables to format them in the embed

  # Survivor: Leon S. Kennedy
  # Perks: Flashbang, Dead Hard, Spine Chill
  # Item: Medkit
  # Map: Coldwind Farm

  Survivor = "Leon S. Kennedy"
  # the perks will be in italics
  Perk1 = "*Flashbang*"
  Perk2 = "*Dead Hard*"
  Perk3 = "*Spine Chill*"
  Item = "Medkit"
  Map = "Coldwind Farm"

  # We have the image of the survivor in the folder so we will use that one

  Surv_image = "Juan/New_Store_Leon.png"

  # We will return all the variables

  return Survivor, Perk1,Perk2,Perk3 , Item, Map, Surv_image

# Get Juan setup:
# It includes his favurite survivor
# His top 3 perks (from the survivors)
# Favourite item
# Favourite map

def get_Iker_setup():
  # Survivor: Jill Valentine / Nea Karlsson / Feng Min / Nancy Wheeler / Meg Thomas 
  # Al azar entre los 5, el survivor seraaaaa..... JILL VALENTINE

  # perks posibles para el top 3: Iron Will, Adrenaline, Botany Knowledge, DS, Borrowed Time, Detective's Hunch,
  # Dance With Me, Windows of Oportunity, Diversion, Autodicact, Head On, Inner Strength, Any Means Necessary, Blood Pact, Soul Guard, Appraisal, 
  # Blast Mine, Wire Trap, Spine Chill, Plunderer's Instinct, Dead Hard, Balanced Landing, Unbreakable, We'll Make It.

  # We will take 3 random perks from the list above:
  # PERK 3:  Inner Strength
  # PERK 2:  Lithe / Blood Pact
  # PERK 1:  Adrenaline


  Survivor = "Jill Valentine"
  # the perks will be in italics
  Perk1 = "*Adrenaline*"
  Perk2 = "*Inner Strength*"
  Perk3 = "*Blood Pact* / *Lithe*"

  Item = "Flashlight"

  Map= "Haddonfield or Hawkins National Laboratory"

  # We have the image of the survivor in the folder so we will use that one

  Surv_image = "Iker/New_Store_Jill.png"

  # We will return all the variables

  return Survivor, Perk1,Perk2,Perk3 , Item, Map, Surv_image


@client.event #async function
async def on_ready(): #when the bot is ready
  print('We have logged in as {0.user}'.format(client))


# When the bot receives a message
@client.event
async def on_message(message):
  # if the message is from the bot user, ignore it
  if message.author == client.user:
    return

  # if the message is !help 
  if message.content.startswith('!dbd help'):
    await message.channel.send('Hello! I am the DBD Randomizer Bot. I can help you to decide your future matches in Dead by Daylight. Just type !commands to get started!')


  # if the message is !commands
  if message.content.startswith('!dbd commands'):
    # we call the function to format this message
    commands = formatCommands(True,"")
    # we send the message
    await message.channel.send(commands)


  # if the message is !dbd help amd the command that the user wants to know more about
  # to read the command we will use the split() function
  if message.content.startswith('!dbd about'):
    # we get the command
    command = message.content.split(' ')[2]
    # we get the description of the command
    description = formatCommands(False,command)
    # we send the message
    await message.channel.send(description)


  # if the message is !dbd Juan 
  # we will put the favorite setup of Juan (such as top 3 perks, top survivor, favourite map, etc.)
  if message.content.startswith('!dbd Juan'):
    # We will call the function to get the setup
    Survivor, Perk1,Perk2,Perk3 , Item, Map, Surv_image = get_juan_setup()

    # We will create the embed
    embed = discord.Embed(title="Juan's setup", description="Juan's Selection", color=0x00ff00)
    embed.set_thumbnail(url="attachment://juanSurv.png")
    embed.add_field(name="Survivor", value=Survivor, inline=False)
    embed.add_field(name="Perk 1", value=Perk1, inline=False)
    embed.add_field(name="Perk 2", value=Perk2, inline=False)
    embed.add_field(name="Perk 3", value=Perk3, inline=False)
    embed.add_field(name="Item", value=Item, inline=False)
    embed.add_field(name="Map", value=Map, inline=False)

    # The perk icon is in the folder so we will use that one
    # We will use the discord.File() function to convert the image to a discord file

    # We will send the embed
    await message.channel.send(file=discord.File(Surv_image, filename="juanSurv.png"), embed=embed)

    # if the message is !dbd Iker 
    # we will put the favorite setup of Iker (such as top 3 perks, top survivor, favourite map, etc.)
  if message.content.startswith('!dbd Iker'):
     # We will call the function to get the setup
    Survivor, Perk1,Perk2,Perk3 , Item, Map, Surv_image = get_Iker_setup()

    # We will add the image of the survivor to the embed (we will increase the size of the image)
    # We will incresa the size of the image by using the discord.File() function

    # increase the size of the image with the function resize_image

    # We will create the embed (purple)
    embed = discord.Embed(title="Iker's setup", description="Iker's Selection", color=0x800080)
    embed.set_thumbnail(url="attachment://ikerSurv.png")
    embed.add_field(name="Survivor", value=Survivor, inline=False)
    embed.add_field(name="Perk 1", value=Perk1, inline=False)
    embed.add_field(name="Perk 2", value=Perk2, inline=False)
    embed.add_field(name="Perk 3", value=Perk3, inline=False)
    embed.add_field(name="Item", value=Item, inline=False)
    embed.add_field(name="Map", value=Map, inline=False)

    
  


    
    # We will send the embed
    await message.channel.send(file=discord.File(Surv_image, filename="ikerSurv.png"), embed=embed)



  # borrador
  if message.content.startswith('!dbd randomPerk'):
    # we take the image and the info from the function
    perk_info, perk_image = get_one_random_perk()

    # we have the image in bytes, we need to have it in utf-8
    # we will use the io.BytesIO() function to convert the image to utf-8
    perk_image_utf8 = io.BytesIO(perk_image)

    # we will use the discord.File() function to convert the image to a discord file
    # And the image will show centered in discord (on the message)
    perk_image_discord_file = discord.File(perk_image_utf8, filename="perk_image.png")

    # we will send the message with the image
    await message.channel.send(perk_info, file=perk_image_discord_file)
    #await message.channel.send(perk_info, file=perk_image)

  
  
  
  # Rest of the commands


# Run the bot
# We have to put the token in an environment variable

# We can also put the token directly in the code but it is not recommended for security reasons
client.run(TOKEN)