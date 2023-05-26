import discord
from discord.ext import commands

import datetime, traceback, asyncio

import services as services
from services import author_service

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

        survName, survImg, perks, mapName = self.__getAuthorInfo(authorName)

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

            await ctx.send(embed=embed)


                            

    



    @commands.group(name="author", aliases=["a"], invoke_without_command=True)
    async def author_group(self, ctx, authorName : str = None):

        await self.__author_group(ctx, authorName)

    # FUTURE: Add the author SUGGESTION


async def setup(bot):
    await bot.add_cog(AuthorCog(bot))



    