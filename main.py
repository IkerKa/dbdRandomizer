import os
import discord
# the import below is for the database
import sqlite3
import sys
# the import below is for the api
import requests
import json
import random
# to the environment variables
import dotenv
from dotenv import load_dotenv
# to convert the image to bytes
import io
# modify images
# from PIL import Image
import services
import traceback
import datetime

import asyncio


from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

intent = discord.Intents.default()
intent.members = True
intent.message_content = True

# Bot activity
activity = discord.Activity(type=discord.ActivityType.watching, name="Looping n' chilling ☕")

# start the dbdRandomizer
client = discord.Client(intents=intent, activity=activity)

bot = commands.Bot(command_prefix='!dbd', intents=intent)

# text format for the !commands
# parameters: boolean for the command
# return: string with the text
# if boolean is true, we show all the commands
# if boolean is false, we show the command of the parameter --> NEEDS TO BE FIXED THIS FUNCTION
def formatCommands(indv, command):
    # We have all the commands on the readme file
    # We will use the discord markdown to format the text

    # We return a string with bold titles and italic description
    retex_0 = "**!dbd help** - *Get an introduction to the bot*\n"
    retex_1 = "**!dbd commands** - *Get a list of commands*\n"
    retex_2 = "**!dbd perk survivor** - *Get a random perk from the survivors with the information about it.*\n"
    retex_3 = "**!dbd perk killer** - *Get a random perk from the killers with the information about it.*\n"
    retex_4 = "**!dbd addon** - *Get a random add-on with the information about it.*\n"
    retex_5 = "**!dbd offering** - *Get a random offering with the information about it.*\n"
    retex_6 = "**!dbd survivor** - *Get a random survivor*\n"
    retex_7 = "**!dbd killer** - *Get a random killer*\n"
    retex_8 = "**!dbd survivor <name>** - *Get information about a specific survivor (specific perks) (pending)*\n"
    retex_9 = "**!dbd killer <name>** - *Get information about the power of a specific killer (pending)*\n"
    retex_10 = "**!dbd survivorlist**- *Get a list of all survivors*\n"
    retex_11 = "**!dbd killerlist** - *Get a list of all killers*\n"
    retex_12 = "**!dbd perkCombo** - *Get a random perk combo of 4 perks to use*\n"
    retex_13 = "**!dbd preMatch survivor** - *Get a random pre-match lobby setup (including 4 perks (from the survivors), 1 item (with 2 add-ons), 1 offering, and 1 survivor)*\n"
    retex_14 = "**!dbd preMatch killer** - *Get a random pre-match lobby setup (including 4 perks (from the killers), 1 item (with 2 add-ons), 1 offering, and 1 killer)*\n"
    retex_15 = "**!dbd item** - *Get a variety-random item (f.e medkit, toolbox, etc.) with the information about it. (pending)*\n"
    retex_16 = "**!dbd item <color>** - *Get a random item (f.e medkit, toolbox, etc.) with the color you specified (pending)*\n"

    # We concatenate all the strings
    if indv == True:
        retex = retex_0 + retex_1 + retex_2 + retex_3 + retex_4 + retex_5 + retex_6 + retex_7 + \
            retex_8 + retex_9 + retex_10 + retex_11 + retex_12 + \
            retex_13 + retex_14 + retex_15 + retex_16
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

@bot.command(name='randomPerk')
async def _randomPerk(ctx, *args):
    print("bot command")
    await ctx.send(args[0])

# ---> comando: !dbd randomPerk
def getRandPerk():

    # Instance the perk class
    perkService = services.PerkService()

    # access the method to get a random perk
    # Params: True True bc we want to get a random perk from the survivors and killers
    perk, owner = perkService.random_perk(1, 1)
    # print(perk)
    # print(owner)

    perk_name = perk[0]
    perk_description = perk[1]
    perk_image = perk[2]
    # Owner: another query

    # We return the name, description and image of the perk
    return perk_name, perk_description, perk_image, owner


# ---> comando: !dbd perk <perkName>
def getPerkInfo(perkName):
    perkService = services.PerkService()

    # Future update: Can be easily put the same function as the random perk with a flag and dont repeat code :)
    perk, owner = perkService.perk_info(perkName)

    if perk == None:
        return None, None, None, None

    perk_name = perk[0]
    perk_description = perk[1]
    perk_image = perk[2]

    return perk_name, perk_description, perk_image, owner


# ---> comando: !dbd randomAddon
def getRandAddon():
    addonService = services.AddOnService()

    addon, itemImage = addonService.random_addOn()

    addon_name = addon[0]
    addon_belongsTo = addon[1]
    addon_description = addon[2]
    addon_image = addon[3]

    return addon_name, addon_belongsTo, addon_description, addon_image, itemImage
    

# ---> comando: !dbd addon <addonName>
def getAddonInfo(addonName):
    addonService = services.AddOnService()

    addon, items, generalName = addonService.get_addOn(addonName)

    if addon == None:
        return None, None, None, None, None, None

    addon_name = addon[0]
    addon_belongsTo = addon[1]
    addon_description = addon[2]
    addon_image = addon[3]

    return addon_name, addon_belongsTo, addon_description, addon_image, items, generalName


#---> comando: !dbd survivor <survivorName>
def getSurvivorInfo(survivorName):

    survivorService = services.SurvivorService()
    # If is None
    if survivorName == None:
        survivor = survivorService.get_survivor(survivorName=None, specific=False)
    else:
        survivor = survivorService.get_survivor(survivorName=survivorName, specific=True)

    return survivor

# ---> comando: !dbd perksof <survivorName>/<killerName>
def getPerksOf(survivorName=None, killerName=None):
    
        survivorService = services.SurvivorService()
    
        if survivorName != None:
            perks = survivorService.get_survivor_perks(survivorName=survivorName)
        elif killerName != None:
            perks = survivorService.get_killer_perks(survivorName=None, killerName=killerName)
        else:
            return None
    
        return perks

def isSurvivor(survivorName):
    survivorService = services.SurvivorService()

    return survivorService.checkName(survivorName)


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

    Surv_image = "devsSelection/Juan/New_Store_Leon.png"

    # We will return all the variables

    return Survivor, Perk1, Perk2, Perk3, Item, Map, Surv_image

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
    Perk2 = "*Dance With Me*"
    Perk3 = "*Lithe*"

    Item = "Flashlight"

    Map = "Haddonfield or Hawkins National Laboratory"

    # We have the image of the survivor in the folder so we will use that one

    Surv_image = "devsSelection/Iker/New_Store_Jill.png"

    # We will return all the variables

    return Survivor, Perk1, Perk2, Perk3, Item, Map, Surv_image


@client.event  # async function
async def on_ready():  # when the bot is ready
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
        commands = formatCommands(True, "")
        # we send the message
        await message.channel.send(commands)

    # if the message is !dbd help amd the command that the user wants to know more about
    # to read the command we will use the split() function
    if message.content.startswith('!dbd about'):
        # we get the command
        command = message.content.split(' ')[2]
        # we get the description of the command
        description = formatCommands(False, command)
        # we send the message
        await message.channel.send(description)

    # if the message is !dbd Juan
    # we will put the favorite setup of Juan (such as top 3 perks, top survivor, favourite map, etc.)
    if message.content.startswith('!dbd Juan'):
        # We will call the function to get the setup
        Survivor, Perk1, Perk2, Perk3, Item, Map, Surv_image = get_juan_setup()

        # We will create the embed
        embed = discord.Embed(title="Juan's setup",
                              description="Juan's Selection", color=0x00ff00)
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
        Survivor, Perk1, Perk2, Perk3, Item, Map, Surv_image = get_Iker_setup()

        # We will add the image of the survivor to the embed (we will increase the size of the image)
        # We will incresa the size of the image by using the discord.File() function

        # increase the size of the image with the function resize_image

        # We will create the embed (purple)
        embed = discord.Embed(title="Iker's setup",
                              description="Iker's Selection", color=0x800080)
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
    # --NO LONGER AVAILABLE (api no longer available)--
    if message.content.startswith('!dbd randomPerk'):
        # we take the image and the info from the function

        try:
            perk_name, perk_image, perk_description, owner = getRandPerk()
            # print(owner)

            if owner == None:
                owner = ("No pertenece a nadie (:",
                         "https://i.imgur.com/Od372kM_d.webp?maxwidth=760&fidelity=grand")

            # We will create the embed
            # timestamp utc + 2
            embed = discord.Embed(
                title=perk_name,
                description=perk_description,
                color=0x00ff00,
                timestamp=datetime.datetime.now(datetime.timezone.utc))

            # embed.set_footer(
            #     text=f"Owner: {owner[0]}",
            #     icon_url=owner[-1],
            # )
            # Try author instead of footer
            embed.set_author(
                name=f"Owner: {owner[0]}",
                icon_url=owner[-1],
            )

            embed.set_thumbnail(url=perk_image)

            # We will send the embed
            await message.channel.send(embed=embed)

        except Exception as e:
            await message.channel.send(f'```{traceback.format_exception(e)}```')

    # if the message is !dbd perk <perk name>
    if message.content.startswith('!dbd perk'):
        #  Take perks name (it can be with spaces)

        try:

            perkN = message.content[10:]

            # We will call the function to get the perk
            perk_name, perk_image, perk_description, owner = getPerkInfo(
                perkN)

            if perk_name == None:
                # Send an image with the perk not found
                # url: https://static.wikia.nocookie.net/deadbydaylight_gamepedia_en/images/5/56/Atl_Loadout_Icon_Cruelty.png/revision/latest?cb=20210604022641
                await message.channel.send("https://static.wikia.nocookie.net/deadbydaylight_gamepedia_en/images/5/56/Atl_Loadout_Icon_Cruelty.png/revision/latest?cb=20210604022641")
                # Message saying that the perk was not found, centerered and in bold
                await message.channel.send(f"**{perkN}** was not found (case sensitive)")

                # Show the list of perks
                await message.channel.send("Here is a list of perks you can check:")
                await message.channel.send("https://deadbydaylight.fandom.com/wiki/Perks")
                await message.channel.send("Or you can use the command **!dbd randomPerk** to get a random perk")

                return

            if owner == None:
                owner = ("No pertenece a nadie (:",
                        "https://i.imgur.com/Od372kM_d.webp?maxwidth=760&fidelity=grand")

            # We will create the embed
            # timestamp utc + 2
            embed = discord.Embed(
                title=perk_name,
                description=perk_description,
                color=0x00fff0,
                timestamp=datetime.datetime.now(datetime.timezone.utc))

            # embed.set_footer(
            #     text=f"Owner: {owner[0]}",
            #     icon_url=owner[-1],
            # )
            # Try author instead of footer
            embed.set_author(
                name=f"Owner: {owner[0]}",
                icon_url=owner[-1],
            )

            embed.set_thumbnail(url=perk_image)

            # We will send the embed
            await message.channel.send(embed=embed)
        except Exception as e:
            await message.channel.send(f'```{traceback.format_exception(e)}```')

    # if the message is !dbd simplePerk
    if message.content.startswith('!dbd simplePerk'):
        # Just inline the image of the perk and the name of the perk in the same line
        try:
            perk_name, perk_image, _, _ = getRandPerk()

            # Show an embed with the name of the perk and the image
            embed = discord.Embed(
                color=0xff0000,
                timestamp=datetime.datetime.now(datetime.timezone.utc))

            # Title of the embed bold and centered
            embed.add_field(name="Perk:",
                            value=f"**{perk_name}**",
                            inline=False)
            
            embed.set_image(url=perk_image)

            # We will send the embed
            await message.channel.send(embed=embed)




        except Exception as e:
            await message.channel.send(f'```{traceback.format_exception(e)}```')


    # if the message is !dbd randomAddon
    if message.content.startswith('!dbd randomAddon'):
        try:
            # We will call the function to get the addon
            addon_name, addon_belongTo, addon_description, addon_image, itemImage = getRandAddon()

            # [Warning] It should be always an item 
            embed = discord.Embed(
                title=addon_name,
                description=addon_description,
                color=0x00ff00,
                timestamp=datetime.datetime.now(datetime.timezone.utc))

            # embed.set_footer(
            #     text=f"Owner: {owner[0]}",
            #     icon_url=owner[-1],
            # )
            # Try author instead of footer
            embed.set_author(
                name=f"From: {addon_belongTo}",
                icon_url=itemImage,
            )

            embed.set_thumbnail(url=addon_image)

            # We will send the embed
            await message.channel.send(embed=embed)



        except Exception as e:
            await message.channel.send(f'```{traceback.format_exception(e)}```')

    # Info about a specific addon
    if message.content.startswith('!dbd addon'):

        try:
            # We get the name of the addon
            addonN = message.content[11:]

            # We will call the function to get the addon
            addon_name, addon_belongTo, addon_description, addon_image, items, generalName = getAddonInfo(addonN)

            # Check if the addon was found
            if addon_name == None:
                # Send an imagen with the addon not found
                await message.channel.send("https://static.wikia.nocookie.net/deadbydaylight_gamepedia_en/images/e/e5/Unknown_QuestionMark.png/revision/latest?cb=20210929093312")
                # Message saying that the addon was not found, centerered and in bold
                await message.channel.send(f"**{addonN}**, you sure you wrote it correctly? (case sensitive)")

                # Show the list of addons
                await message.channel.send("Here is a list of addons you can check:")
                await message.channel.send("https://deadbydaylight.fandom.com/wiki/Add-ons")
                await message.channel.send("Or you can use the command **!dbd randomAddon** to get a random addon")

                return
            
            # [Warning] It should be always an item
            embed = discord.Embed(
                title=addon_name,
                description=addon_description,
                color=0x0000ff,
                timestamp=datetime.datetime.now(datetime.timezone.utc))
            
            # embed.set_footer(
            #     text=f"Owner: {owner[0]}",
            #     icon_url=owner[-1],

            # )

            # Try author instead of footer
            embed.set_author(
                name=f"From: {generalName}"
            )

            embed.set_thumbnail(url=addon_image)

            # Add a field with the item list
            # Parse the items list
            # Format the tuple to a string
            items = [f"**{item[0]}**" for item in items]
            # Join with a comma
            items = ", ".join(items)
            embed.add_field(name="Items that can use this addon:",
                            value=items,
                            inline=False)
            
            # We will send the embed
            await message.channel.send(embed=embed)

        except Exception as e:
            await message.channel.send(f'```{traceback.format_exception(e)}```')

        
    # if the message is !dbd survivor <name?>
    if message.content.startswith('!dbd survivor'):
        # Check if it has a name 
        try:
            # Check if the command has a name or not
            survivorN = message.content[14:]
            

            # If it has a name
            if survivorN == "" or survivorN == " ":
                survivorN = None


            # If it has no name, it will be a random survivor
            survivor = getSurvivorInfo(survivorN)
            if survivor == None:
                    # Send an imagen with the survivor not found
                    await message.channel.send("https://static.wikia.nocookie.net/deadbydaylight_gamepedia_en/images/9/9e/IconStatusEffects_exposed.png/revision/latest?cb=20170620155518")
                    # Message saying that the survivor was not found, centerered and in bold
                    await message.channel.send(f"**{survivorN}**, you sure you wrote it correctly? (case sensitive)")

                    # Show the list of survivors
                    await message.channel.send("Here is a list of survivors you can check:")
                    await message.channel.send("https://deadbydaylight.fandom.com/wiki/Survivors")
                    await message.channel.send("Or you can use the command **!dbd survivor** to get a random survivor")

                    return

            # Depends on the name, we will show a different embed
            # If the name is None, it will be a random survivor
            if survivorN == None:
                # Just take the name and the image
                survivor_name = survivor[0]
                survivor_image = survivor[-1]

                # Show an embed with the name of the survivor and the image
                embed = discord.Embed(
                    color=0xff0000,
                    timestamp=datetime.datetime.now(datetime.timezone.utc))
                
                # Title of the embed bold and centered
                embed.add_field(name="Survivor:",
                                value=f"**{survivor_name}**",
                                inline=False)
                
                embed.set_image(url=survivor_image)

                # We will send the embed
                await message.channel.send(embed=embed)

            # If the name is not None, it will be a specific survivor
            else:

                # Take all the info: name, perk1,perk2,perk3, bio, image
                survivor_name, survivor_perk1, survivor_perk2, survivor_perk3, survivor_bio, survivor_image = survivor


                # Show an embed with the name of the survivor and the image
                embed = discord.Embed(
                    color=0xff0000,
                    timestamp=datetime.datetime.now(datetime.timezone.utc))
                
                # Title of the embed bold and centered
                embed.add_field(name="Survivor:",
                                value=f"**{survivor_name}**",
                                inline=False)
                
                embed.set_image(url=survivor_image)

                # Add the perks
                embed.add_field(name="**Perks:**",
                                value=f"_{survivor_perk1}_\n_{survivor_perk2}_\n_{survivor_perk3}_",
                                inline=False)
                
                # Add the bio
                embed.add_field(name="**Bio:**",
                                value=f"{survivor_bio}",
                                inline=False)
                
                # We will send the embed
                await message.channel.send(embed=embed)





        except Exception as e:
            await message.channel.send(f'```{traceback.format_exception(e)}```')

    # if the message is !dbd perksof <name?>
    if message.content.startswith('!dbd getperksof'):
        try:
            # Take the name
            ownerName = message.content[16:]

            # Check if is a killer or a survivor
            isSurv = isSurvivor(ownerName)

            if isSurv:
                # Get the perks of the survivor
                perks = getPerksOf(ownerName,None)

            else:
                # Get the perks of the killer
                perks = getPerksOf(None,ownerName)

            # Parse the perks 
            # Its an array of tuples
            # Format the tuple to a string
            names = [f"**{perk[0]}**" for perk in perks]
            # Join with a comma
            names = ", ".join(names)

            # Show an embed with the name of the survivor and the image
            embed = discord.Embed(
                color=0xff0000,
                timestamp=datetime.datetime.now(datetime.timezone.utc))
            
            # Title of the embed bold and centered
            embed.add_field(name=f"Perks of {ownerName}:",
                            value=f"{names}",
                            inline=False)
            
            # # Add the images
            # # Get the images
            images = [perk[-1] for perk in perks]
            
            image_index = 0
            total_images = len(images)
            current_image = images[image_index]
            embed.set_image(url=current_image)
            perkName = perks[image_index][0]
            embed.set_footer(text=f'Perk: {perkName}')

            msg = await message.channel.send(embed=embed)
            await msg.add_reaction('⬅️')
            await msg.add_reaction('➡️')

            def check(reaction, user):
                return user == message.author and str(reaction.emoji) in ['⬅️', '➡️']
            
            while True:
                try:
                    reaction, user = await client.wait_for('reaction_add', timeout=30.0, check=check)

                    if str(reaction.emoji) == '⬅️':
                        image_index -= 1
                        if image_index < 0:
                            image_index = total_images - 1
                    elif str(reaction.emoji) == '➡️':
                        image_index += 1
                        if image_index >= total_images:
                            image_index = 0

                    current_image = images[image_index]
                    perkName = perks[image_index][0]
                    embed.set_image(url=current_image)
                    embed.set_footer(text=f'Perk: {perkName}')
                    await msg.edit(embed=embed)
                    await msg.remove_reaction(reaction, user)
                except asyncio.TimeoutError:
                    break




        except Exception as e:
            await message.channel.send(f'```{traceback.format_exception(e)}```')
        








    





    


# Run the bot
# We have to put the token in an environment variable

# We can also put the token directly in the code but it is not recommended for security reasons

client.run(TOKEN)

