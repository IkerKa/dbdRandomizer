import discord
from discord.ext import commands

import services as services
from services import survivor_service

import datetime, traceback

class SurvivorCog(commands.Cog):
    # Constructor
    def __init__(self, bot: commands.Bot):
        """
        Constructor of the class
        """
        self.bot = bot
        self.survivorService = survivor_service.SurvivorService()

    # Private methods
    def __getSurvivorInfo(self, survivorName):

        survivorService = services.SurvivorService()
        # If is None
        if survivorName == None:
            survivor = survivorService.get_survivor(survivorName=None, specific=False)
        else:
            survivor = survivorService.get_survivor(survivorName=survivorName, specific=True)

        return survivor
    
    async def __survivor_group(self, ctx, survivorN):
        try:

            # if survivorN == "" or survivorN == " ":
            #     survivorN = None

            # If it has no name, it will be a random survivor
            survivor = self.__getSurvivorInfo(survivorN)
            if survivor == None:
                    # Send an imagen with the survivor not found message
                    embed = discord.Embed(
                        color=0xff0000,
                        title="Survivor not found!",
                        description="You have to write a valid survivor name!",
                        timestamp=datetime.datetime.now(datetime.timezone.utc))
                    
                    embed.set_thumbnail(url="https://static.wikia.nocookie.net/deadbydaylight_gamepedia_en/images/9/9e/IconStatusEffects_exposed.png/revision/latest?cb=20170620155518")
                    

                    embed.add_field(name="Here is a list of survivors you can check:",
                                    value="Jill Valentine, Nancy Wheeler, Nea Karlsson..."
                                    )
                    
                    embed.set_footer(text="FORMAT: !dbd survivor NAME")


                    await ctx.send(embed=embed)

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
                await ctx.send(embed=embed)

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
                await ctx.send(embed=embed)





        except Exception as e:
            await ctx.send(f'```{traceback.format_exception(e)}```')

    
    
    # --->DEFINICIONES DE COMANDOS<---
    # father command !dbd survivor
    @commands.group(name="survivor", description="Command group for Survivors")
    # To take the name with spaces we need to use *, if not, it will take only the first word
    async def survivor(self, ctx, *, survN = None):
        await self.__survivor_group(ctx, survN)

    # if there's a subcommand, it will be called here
    
async def setup(bot: commands.Bot):
    await bot.add_cog(SurvivorCog(bot))

    


    

