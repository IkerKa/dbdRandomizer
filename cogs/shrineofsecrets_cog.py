import discord
from discord.ext import commands

import datetime, traceback, asyncio

import services as services
# Module from shrine folder
import shrine
from shrine import currentSoS as sos
from services import perk_service
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





class ShrineofsecretsCog(commands.Cog):


    def __init__(self, bot: commands.Bot):
        """

        """
        self.bot = bot
        self.perkService = perk_service.PerkService()
        
    
    def __getShrineInfo(self):
        """
            Get the shrine info (atm perks and time)
        """
        return  sos.get_current_sos()
    
    def __getSosImages(self):
        pass
        
    
    async def __sos_group(self, ctx, detailed):

        perks,time = self.__getShrineInfo()


        embed = discord.Embed(
            color=0xffff00,
            title="Shrine of Secrets",
            description="The shrine of secrets is a special store that can be found in the in-game store tab. It refreshes every week with 4 new perks.",
            timestamp=datetime.datetime.now(datetime.timezone.utc)
        )

        embed.set_thumbnail(url="https://static.wikia.nocookie.net/deadbydaylight_gamepedia_en/images/1/14/IconHelp_shrineOfSecrets.png/revision/latest?cb=20171021115817")

        
        # Perks is an array of dictionaries
        names = [perk['title'] for perk in perks]
        images = [perk['img'] for perk in perks]

        
        
        if not detailed:

            # Join the names with a comma
            names = ", ".join(names)

            embed.add_field(name="Perks:", value=f"_{names}_", inline=False)
            
            embed.set_author(name=f"Time when it refreshes: {time}", icon_url='https://static.wikia.nocookie.net/deadbydaylight_gamepedia_en/images/a/a2/IconHelp_alarmClock.png/revision/latest?cb=20220910215206')

            # No reaction to change the image, just the formatted one
            # We have all the urls so:
            image_perk1 = Image.open(BytesIO(requests.get(images[0]).content))
            image_perk2 = Image.open(BytesIO(requests.get(images[1]).content))
            image_perk3 = Image.open(BytesIO(requests.get(images[2]).content))
            image_perk4 = Image.open(BytesIO(requests.get(images[3]).content))

            # Create a perk display object
            # 4 arguments passed as
            pdisp = pi.perk_display(
                up=image_perk1,
                left=image_perk2,
                right=image_perk3,
                down=image_perk4,
                size=(512, 512)
            )

            bytes_img = BytesIO()
            pdisp.save(bytes_img, format="PNG")
            bytes_img.seek(0)
            dfile = discord.File(bytes_img, filename="image.png")

            embed.set_image(url="attachment://image.png")
            embed.set_footer(text=f'Cost: 2000(I)/4000(II)/6000(III) Iridescent Shards')

            await ctx.send(embed=embed, file=dfile)
        

        else:

            # Detailed version, so we are going to bold the perk name whose image is being displayed
            # and with reactions we will change the image and the bolded perk name

            image_index = 0
            total_images = len(images)
        
            names = ", ".join(names)

            # Bold the first perk
            names = names.replace(perks[image_index].get('title'), f"**{perks[image_index].get('title')}**")
            
           
            embed.set_field_at(0, name=f"Perks:",
                            value=f"_{names}_",
                            inline=False)
            
            embed.set_author(name=f"Time when it refreshes: {time}", icon_url='https://static.wikia.nocookie.net/deadbydaylight_gamepedia_en/images/a/a2/IconHelp_alarmClock.png/revision/latest?cb=20220910215206')
            

            
            
            current_image = images[image_index]
            embed.set_image(url=current_image)
            perkName = perks[image_index].get('title')
            embed.set_footer(text=f'Perk: {perkName}')

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

                    current_image = images[image_index]
                    perkName = perks[image_index].get('title')
                    # Edit, rechange the addon into normal, and focus in bald the new one
                    names = [perk['title'] for perk in perks]
                    # Join with a comma
                    names = ", ".join(names)

                    # Put the new addon in bold
                    names = names.replace(perks[image_index].get('title'), f"**{perks[image_index].get('title')}**")

                    embed.set_field_at(0, name=f"Perks:",
                            value=f"_{names}_",
                            inline=False)
                    

                    embed.set_image(url=current_image)
                    embed.set_footer(text=f'Perk: {perkName}')
                    await msg.edit(embed=embed)
                    await msg.remove_reaction(reaction, user)
                except asyncio.TimeoutError:
                    break



            await ctx.send(embed=embed)







    @commands.group(name="sos", aliases=["shrine"], invoke_without_command=True)
    async def sos(self, ctx, detailed=False):
        """
            Group of commands related to the shrine of secrets
        """
        await self.__sos_group(ctx, detailed)

    # FUTURE: Add the detailed option


async def setup(bot):
    await bot.add_cog(ShrineofsecretsCog(bot))
    