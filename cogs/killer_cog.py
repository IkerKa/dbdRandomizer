import discord
from discord.ext import commands

import services as services
from services import killer_service

import datetime, traceback

class KillerCog(commands.Cog):

    def __init__(self, bot: commands.Bot):
        """
        Constructor of the class
        """
        self.bot = bot
        self.killerService = killer_service.KillerService()

    # Private methods
    # ---> comando: !dbd killer (no name)
    def __getKillerInfo(self, killerName):

        if killerName == None:
            killer = self.killerService.get_killer(None,False)
        else:
            killer = self.killerService.get_killer(killerName,True)

        return killer
    
    # ---> comando: !dbd killer addons <killerName>
    def __getKillerAddons(self, killerName):
        pass

    async def __killer_group(self, ctx, kName : str = None):
      
        try:
            
            killer = self.__getKillerInfo(kName)
            if killer == None:
                # Error:
                # Send an imagen with the killer not found
                await ctx.send("https://static.wikia.nocookie.net/deadbydaylight_gamepedia_en/images/9/9e/IconStatusEffects_exposed.png/revision/latest?cb=20170620155518")
                # Message saying that the killer was not found, centerered and in bold
                await ctx.send(f"**{kName}**, you sure you wrote it correctly? (case sensitive), FORMAT: !dbd killer PSEUDONAME")
                await ctx.send("For example: !dbd killer Trapper")

                # Show the list of killers
                await ctx.send("Here is a list of killers you can check:")
                await ctx.send("https://deadbydaylight.fandom.com/wiki/Killers")

                return
            
            # If the name is None, it will be a random killer
            if kName == None:
                # Random one
                killer_name = killer[0]
                killer_image = killer[-1]

                # Show an embed with the name of the killer and the image
                embed = discord.Embed(
                    color=0xff0000,
                    title=f"**{killer_name}**",
                    description="",
                    timestamp=datetime.datetime.utcnow()
                )
                embed.set_image(url=killer_image)
                embed.set_footer(text="Random killer")

                await ctx.send(embed=embed)
                return
            
            # If the name is not None, it will be a specific killer
            if kName != None:
                
                killerName, killerPerk1, killerPerk2, killerPerk3, killerPower, killerImage = killer

                # Show an embed with the name of the killer and the image
                embed = discord.Embed(
                    color=0xff0000,
                    title=f"**{killerName}**",
                    description=killerPower,
                    timestamp=datetime.datetime.utcnow()
                )
                embed.add_field(name="**Perks**", value=f"_{killerPerk1}_\n_{killerPerk2}_\n_{killerPerk3}_", inline=False)
                embed.set_image(url=killerImage)

                await ctx.send(embed=embed)

                


            
        except Exception as e:
            await ctx.send(f'```{traceback.format_exception(e)}```')
                    

            
           






    # Group of commands
    @commands.group(name="killer", aliases=["k"], invoke_without_command=True) #, case_insensitive=True)
    async def killer(self, ctx, *, killerName : str = None):
        """
        Shows information about a killer or a random killer
        """
        
        await self.__killer_group(ctx, killerName)

    

    # @killer.command(name="addons", aliases=["a"])


async def setup(bot: commands.Bot):
    await bot.add_cog(KillerCog(bot))