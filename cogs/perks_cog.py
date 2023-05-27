import random
import discord
from discord.ext import commands

import datetime, traceback, asyncio

from services import PerkService, SurvivorService, KillerService

import formatter as formatter
from formatter import perk_imager as pi
from PIL import Image
from io import BytesIO
import requests
import os

# OpenCV 
import cv2
import numpy as np
import matplotlib.pyplot as plt


class PerksCog(commands.Cog):

    def __init__(self, bot: commands.Bot):
        """

        """
        self.bot = bot
        self.perkService = PerkService()
        self.survivorService = SurvivorService()
        self.killerService = KillerService()

    def __randomCombo(self, ctx, isSurv : int, isKiller : int, number : input):
        
        return self.perkService.random_combo(isSurv, isKiller, number)

    def __getRandBoonPerk(self, isSurv : int, isKiller : int):
            
            # access the method to get a random perk
            # Params: True True bc we want to get a random perk from the survivors and killers
            perk, owner = self.perkService.randomBoon_perk(isSurv, isKiller)
            # print(perk)
            # print(owner)
    
            perk_name = perk[0]
            perk_description = perk[1]
            perk_image = perk[2]
            # Owner: another query
    
            # We return the name, description and image of the perk
            return perk_name, perk_description, perk_image, owner

    
    def __getRandHexPerk(self, isSurv : int, isKiller : int):
            
            # access the method to get a random perk
            # Params: True True bc we want to get a random perk from the survivors and killers
            perk, owner = self.perkService.randomHex_perk(isSurv, isKiller)
            # print(perk)
            # print(owner)
    
            perk_name = perk[0]
            perk_description = perk[1]
            perk_image = perk[2]
            # Owner: another query
    
            # We return the name, description and image of the perk
            return perk_name, perk_description, perk_image, owner

    def __getRandPerk(self, isSurv : int, isKiller : int):

        # access the method to get a random perk
        # Params: True True bc we want to get a random perk from the survivors and killers
        perk, owner = self.perkService.random_perk(isSurv, isKiller)
        # print(perk)
        # print(owner)

        perk_name = perk[0]
        perk_description = perk[1]
        perk_image = perk[2]
        # Owner: another query

        # We return the name, description and image of the perk
        return perk_name, perk_description, perk_image, owner

    # ---> comando: !dbd perk <perkName>
    def __getPerkInfo(self, perkName):

        # Future update: Can be easily put the same function as the random perk with a flag and dont repeat code :)
        perk, owner = self.perkService.perk_info(perkName)

        if perk == None:
            return None, None, None, None

        perk_name = perk[0]
        perk_description = perk[1]
        perk_image = perk[2]

        return perk_name, perk_description, perk_image, owner

    def __getPerksOf(self,survivorName=None, killerName=None):
    
        if survivorName != None:
            perks = self.survivorService.get_survivor_perks(survivorName)
        elif killerName != None:
            perks = self.killerService.get_killer_perks(killerName)
        else:
            return None
    
        return perks

    async def __randomBoon_perk(self, ctx, isSurv : int, isKiller : int):
        # Just inline the image of the perk and the name of the perk in the same line
        perk_name, perk_image, _, _ = self.__getRandBoonPerk(isSurv, isKiller)


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
        await ctx.send(embed=embed)

    async def __randomHex_perk(self, ctx, isSurv : int, isKiller : int):
        # Just inline the image of the perk and the name of the perk in the same line
        perk_name, perk_image, _, _ = self.__getRandHexPerk(isSurv, isKiller)


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
        await ctx.send(embed=embed)

    async def __random_perk(self, ctx, isSurv : int, isKiller : int):
        # Just inline the image of the perk and the name of the perk in the same line
        perk_name, perk_image, _, _ = self.__getRandPerk(isSurv, isKiller)

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
        await ctx.send(embed=embed)


    async def __perks_group(self, ctx, perkN):
        """
        Simple random perk, or detailed perk given an argument.
        """
        try:
            if perkN is None:
                await self.__random_perk(ctx, 1, 1)

            else:
                # Detailed perk, name is arg1

                # We will call the function to get the perk
                perk_name, perk_image, perk_description, owner = self.__getPerkInfo(perkN)

                if perk_name == None:
                    # Send an image with the perk not found
                    embed = discord.Embed(
                        # Perk _<perkName>_ not found
                        title=f"Perk _{perkN}_ not found",
                        description="Check the name of the perk and try again, or check if it's a Hex. In that case use hex: first.",
                        color=0xff0000,
                        timestamp=datetime.datetime.now(datetime.timezone.utc))
                    
                    
                    embed.set_thumbnail(url="https://static.wikia.nocookie.net/deadbydaylight_gamepedia_en/images/5/56/Atl_Loadout_Icon_Cruelty.png/revision/latest?cb=20210604022641")

                    embed.set_footer(
                        text="Use !dbd perks for more info",

                    )
                    # We will send the embed
                    await ctx.send(embed=embed)

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
                await ctx.send(embed=embed)

        except Exception as e:
            await ctx.send(f'```{traceback.format_exception(e)}```')

    async def __perks_survivor(self, ctx):
        try:
            await self.__random_perk(ctx, 1, 0)
        except Exception as e:
            await ctx.send(f'```{traceback.format_exception(e)}```')

    async def __perks_killer(self, ctx):
        try:
            await self.__random_perk(ctx, 0, 1)
        except Exception as e:
            await ctx.send(f'```{traceback.format_exception(e)}```')

    async def __perks_of(self, ctx, ownerName : str):
        try:
            
            # Check if is a killer or a survivor
            isSurv = self.survivorService.checkName(ownerName.lower())

            fullInfo = None

            if isSurv:
                fullInfo = self.survivorService.get_survivor(ownerName, True)
                # Get the perks of the survivor
                perks = self.__getPerksOf(ownerName,None)

            else:
                fullInfo = self.killerService.get_killer(ownerName, True)

                if fullInfo is None:
                    # error
                    err_embed = discord.Embed(
                        color=0xf0f000,
                        timestamp=datetime.datetime.now(datetime.timezone.utc),
                        title="Whoops!",
                        description="Can't find the survivor/killer. Are you sure you spelled it right?")

                    err_embed.set_thumbnail(url="https://static.wikia.nocookie.net/deadbydaylight_gamepedia_en/images/9/9e/IconStatusEffects_exposed.png/revision/latest?cb=20170620155518")
                    
                    await ctx.send(embed=err_embed)

                    return
                else:
                    # Get the perks of the killer
                    perks = self.__getPerksOf(None,fullInfo[0])

            # Parse the perks 
            # Its an array of tuples
            # Format the tuple to a string
            perk_names = [f"{perk[0]}" for perk in perks]

            image_index = 0

            title_vars = perk_names.copy()
            title_vars[image_index] = f"**{title_vars[image_index]}**"

            # Join with a comma
            names = ", ".join(title_vars)

            # Show an embed with the name of the survivor and the image
            embed = discord.Embed(
                color=0xff0000,
                timestamp=datetime.datetime.now(datetime.timezone.utc),
                description=names)
            
            # Title of the embed bold and centered
            
            # # Add the images
            # # Get the images
            images = [perk[-1] for perk in perks]
            
            
            total_images = len(images)
            current_image = images[image_index]
            embed.set_image(url=current_image)
            embed.set_footer(text=f'Perk: {perk_names[image_index]}')
            embed.set_author(
                name=f"Perks of {fullInfo[0]}",
                icon_url=fullInfo[-1]
            )

            msg = await ctx.send(embed=embed)
            await msg.add_reaction('⬅️')
            await msg.add_reaction('➡️')

            def check(reaction, user):
                return user == ctx.author and str(reaction.emoji) in ['⬅️', '➡️']
            
            while True:
                try:
                    reaction, user = await self.bot.wait_for('reaction_add', timeout=60.0, check=check)

                    if str(reaction.emoji) == '⬅️':
                        image_index -= 1
                        if image_index < 0:
                            image_index = total_images - 1
                    elif str(reaction.emoji) == '➡️':
                        image_index += 1
                        if image_index >= total_images:
                            image_index = 0
                    
                    title_vars = perk_names.copy()
                    title_vars[image_index] = f"**{title_vars[image_index]}**"
                    names = ", ".join(title_vars)

                    embed = discord.Embed(
                        color=0xff0000,
                        timestamp=datetime.datetime.now(datetime.timezone.utc),
                        description=names)
                    embed.set_footer(text=f'Perk: {perk_names[image_index]}')
                    embed.set_author(
                        name=f"Perks of {fullInfo[0]}",
                        icon_url=fullInfo[-1]
                    )
                    current_image = images[image_index]
                    embed.set_image(url=current_image)

                    await msg.edit(embed=embed)
                    await msg.remove_reaction(reaction, user)
                except asyncio.TimeoutError:
                    break

        except Exception as e:
            await ctx.send(f'```{traceback.format_exception(e)}```')

    async def __perks_hex(self, ctx, perkN):
        # Just add the hex to the perkN
        if perkN is None:
            # print("No perkN")
            await self.__randomHex_perk(ctx, 0, 1)
        else:
            perkN = f"Hex: {perkN.lower()}"
            # Call perk group
            await self.__perks_group(ctx, perkN)

    async def __perks_boon(self, ctx, perkN):
        # Just add the hex to the perkN
        if perkN is None:
            # print("No perkN")
            await self.__randomBoon_perk(ctx, 1,0)
        else:
            perkN = f"Boon: {perkN.lower()}"
            # Call perk group
            await self.__perks_group(ctx, perkN)


    async def __perkCombo_group(self,ctx, character, number):

        # Loading embed
        loading_embed = discord.Embed(
            color=0xf0f000,
            timestamp=datetime.datetime.now(datetime.timezone.utc),
            title="Loading...",
            description="Wait fellas!, Your perk combo is baking ʕ••ʔ")

        msg = await ctx.send(embed=loading_embed)

        
        if character is not None:
            character = character.lower()
        
        # If the character is killer
        if character is None:
            # Just a randomCombo
            randInteger = random.randint(0,1)
            if randInteger == 0:
                perks = self.__randomCombo(ctx,0,1, number)
                character = "killer"
            else:
                perks = self.__randomCombo(ctx,1,0, number)
                character = "survivor"
        
        if character == "killer":
            perks = self.__randomCombo(ctx,0,1, number)
        elif character == "survivor":
            perks = self.__randomCombo(ctx,1,0, number)
        # else:
        #     embed = discord.Embed(
        #         color=0xf0f000,
        #         timestamp=datetime.datetime.now(datetime.timezone.utc),
        #         title="Whoops!",
        #         description="Invalid command. Just !dbd perkcombo killer/survivor")
            
        #     embed.set_thumbnail(url="https://static.wikia.nocookie.net/deadbydaylight_gamepedia_en/images/f/f0/IconHelp_exitGates.png/revision/latest?cb=20170907140953")
            
        #     await ctx.send(embed=embed)


        # Parse the perks
        # Make an embed

        # print("PERKS: ", perks)

        ps = [f"{perk[0]}" for perk in perks]
        # Get the first 4
        ps = ps[:4]

        # Join with comma the first 4
        names = ", ".join(ps)




        embed = discord.Embed(
            title=f"Your perk combo is ready!",
            color=0xf0f000,
            timestamp=datetime.datetime.now(datetime.timezone.utc),
            description=names)


        embed.set_footer(text="Perk Combo")
        # print("PERKS: ", perks)

        perksImages = [perk[1] for perk in perks]

        if len(perksImages) < 4:
            while(len(perksImages) < 4):
                perksImages.append(None)

        # Print formatted string
        # print("PERKS IMAGES: ", perksImages)

        
        image_perk = []
        for perk in perksImages:
            if perk is not None:
                image_perk.append(Image.open(BytesIO(requests.get(perk).content)))
            else:
                image_perk.append(None)

        if character == "killer":
            embed.set_thumbnail(url="https://static.wikia.nocookie.net/deadbydaylight_gamepedia_en/images/0/06/IconHelpLoading_killer.png/revision/latest?cb=20220324212743")
        elif character == "survivor":
            embed.set_thumbnail(url="https://static.wikia.nocookie.net/deadbydaylight_gamepedia_en/images/b/b3/IconHelpLoading_survivor.png/revision/latest?cb=20220324212914")

        # Create a perk display object
        # 4 arguments passed as
        pdisp = pi.perk_display(
            up=image_perk[0],
            left=image_perk[1],
            right=image_perk[2],
            down=image_perk[3],
            size=(512, 512)
        )

        bytes_img = BytesIO()
        pdisp.save(bytes_img, format="PNG")
        bytes_img.seek(0)
        dfile = discord.File(bytes_img, filename="image.png")

        embed.set_image(url="attachment://image.png")

        # Delete the loading message
        await msg.delete()
        

        # Substitution for the message
        await ctx.send(embed=embed, file=dfile)


    @commands.group(description="Command group for Perks", invoke_without_command=True, pass_context=True)
    async def perks(self, ctx, *, arg1 = None):
        await self.__perks_group(ctx, arg1)

    @perks.command(description="Subcommand for getting random survivor perk")
    async def survivor(self, ctx):
        await self.__perks_survivor(ctx)

    @perks.command(description="Subcommand for getting random killer perk")
    async def killer(self, ctx):
        await self.__perks_killer(ctx)

    @perks.command(name="of", description="Subcommand for getting random killer perk")
    async def perks_of(self, ctx, *, arg1):
        await self.__perks_of(ctx, arg1)
    
    @perks.command(name="hex", description="(QoL)Subcommand for getting random hex perk or a specific one")
    async def perks_hex(self, ctx, *, arg1 = None):
        await self.__perks_hex(ctx, arg1)

    @perks.command(name="boon", description="(QoL)Subcommand for getting random boon perk or a specific one")
    async def perks_boon(self, ctx, *, arg1 = None):
        await self.__perks_boon(ctx, arg1)

    # New group for getting a list of perks
    @commands.group(description="Command group for Perks", invoke_without_command=True, pass_context=True)
    async def perkcombo(self, ctx, arg1 = None, arg2 = None):
        # arg1 could be survivor or killer
        if arg1 is None:
            await self.__perkCombo_group(ctx, character=None, number=4)
        elif arg1.isnumeric():
            await self.__perkCombo_group(ctx, character=None, number=int(arg1))
        else:
            if arg2 is None:
                await self.__perkCombo_group(ctx, character=arg1, number=4)
            elif arg2.isnumeric():
                await self.__perkCombo_group(ctx, character=arg1, number=int(arg2))
            else:
                await ctx.send("Invalid command. Just !dbd perkcombo killer/survivor <number>")


    # Same, survivor,killer ...





    # @perks.command(name="list", description="Subcommand for getting a list of perks")

async def setup(bot):
    await bot.add_cog(PerksCog(bot))