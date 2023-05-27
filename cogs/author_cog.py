import discord
from discord.ext import commands

import datetime, traceback, asyncio

import services as services
from services import author_service
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





class AuthorCog(commands.Cog):


    def __init__(self, bot: commands.Bot):
        """

        """
        self.bot = bot
        self.authorService = author_service.AuthorService()
    
    def __getAuthorInfo(self, authorName):
        """
            Get the author info
        """
        return  self.authorService.author_setup(authorName)

   
    
    async def __author_group(self, ctx, authorName : str = None):

        survName, survImg, perks, perksImages, mapName = self.__getAuthorInfo(authorName)

        if survName == None:
            embed = discord.Embed(
                    color=0xff0000,
                    title="Author not found!",
                    description="You have to write a valid author name!",
                    timestamp=datetime.datetime.now(datetime.timezone.utc)
                )
            
            embed.set_thumbnail(url="https://static.wikia.nocookie.net/deadbydaylight_gamepedia_en/images/9/96/Removed.png/revision/latest?cb=20230327131411")

            embed.add_field(name="The authors are: Iker, Juan & Dario",
                            value="You can check the authors with the command !dbd author"
                            )
            
            embed.set_footer(text="FORMAT: !dbd author <authorName>")

            await ctx.send(embed=embed)

        else:
            embed = discord.Embed(
                    color=0x00ff00,
                    title=survName,
                    description="Here is the author info!",
                    timestamp=datetime.datetime.now(datetime.timezone.utc)
                )
            
            embed.set_author(name="Fav Setup from " + authorName)

            perks = ", ".join(perks) 

            embed.add_field(name="**Favourite Perks:**",
                            value="_"+perks+"_"
                            )
            
            embed.add_field(name="**Favourite Map:**",
                            value="_"+mapName+"_"
                            )
            
            embed.set_thumbnail(url=survImg)

            # print("PERKS: ", perks)
            image_perk1 = Image.open(BytesIO(requests.get(perksImages[0]).content))
            image_perk2 = Image.open(BytesIO(requests.get(perksImages[1]).content))
            image_perk3 = Image.open(BytesIO(requests.get(perksImages[2]).content))
            image_perk4 = Image.open(BytesIO(requests.get(perksImages[3]).content))

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

            await ctx.send(embed=embed, file=dfile)

    @commands.group(name="author", aliases=["a"], invoke_without_command=True)
    async def author_group(self, ctx, authorName : str = None):

        await self.__author_group(ctx, authorName)

    # FUTURE: Add the author SUGGESTION


async def setup(bot):
    await bot.add_cog(AuthorCog(bot))
    