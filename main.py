import os
import discord
#the import below is for the database
import sqlite3
#the import below is for the api
import requests
import json
import random
# to the environment variables
import dotenv
from dotenv import load_dotenv
# to convert the image to bytes
import io


load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

intent = discord.Intents.default()
intent.members = True
intent.message_content = True


# start the dbdRandomizer
client = discord.Client(intents=intent)


# DATABASE??

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
  if message.content.startswith('!help'):
    await message.channel.send('Hello! I am the DBD Randomizer Bot. I can help you to decide your future matches in Dead by Daylight. Just type !commands to get started!')

  # borrador
  if message.content.startswith('!randomPerk'):
    # we take the image and the info from the function
    perk_info, perk_image = get_one_random_perk()

    # we have the image in bytes, we need to have it in utf-8
    # we will use the io.BytesIO() function to convert the image to utf-8
    perk_image_utf8 = io.BytesIO(perk_image)

    # we will use the discord.File() function to convert the image to a discord file
    perk_image_discord_file = discord.File(perk_image_utf8, filename="perk_image.png")

    # we will send the message with the image
    await message.channel.send(perk_info, file=perk_image_discord_file)
    #await message.channel.send(perk_info, file=perk_image)
  
  
  # Rest of the commands


# Run the bot
# We have to put the token in an environment variable

# We can also put the token directly in the code but it is not recommended for security reasons
client.run(TOKEN)






