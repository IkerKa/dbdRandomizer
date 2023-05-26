import discord
from discord.ext import commands

import services as services
from services import killer_service

import datetime, traceback
import asyncio

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
        return self.killerService.get_killer_addons(killerName)



    async def __killer_group(self, ctx, kName : str = None):
      
        try:
            
            killer = self.__getKillerInfo(kName)
            if killer == None:
                # Error:
                # Send an imagen with the killer not found
                embed = discord.Embed(
                        color=0xff0000,
                        title="Killer not found!",
                        description="You have to write a valid killer name!",
                        timestamp=datetime.datetime.now(datetime.timezone.utc))
                    
                embed.set_thumbnail(url="https://static.wikia.nocookie.net/deadbydaylight_gamepedia_en/images/9/9e/IconStatusEffects_exposed.png/revision/latest?cb=20170620155518")
                
                embed.add_field(name="Here is a list of killers you can check:",
                                value="Trapper, Shape, Singularity..."
                                )
                
                embed.set_footer(text="FORMAT: !dbd killer addons PSEUDONAME")
                

                await ctx.send(embed=embed)

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
                    

    async def __killer_addons(self, ctx, kName : str = None):

        if kName == None:
            await ctx.send("You need to specify a killer name, FORMAT: !dbd killer addons PSEUDONAME")

        # Get the addons of the killer
        addons = self.__getKillerAddons(kName)

        # Get the killer info
        killer = self.__getKillerInfo(kName)
        killerName, _,_,_,_, killerImage = killer

        if  killerName == None:
            # Error:
            # Send an imagen with the killer not found
            embed = discord.Embed(
                        color=0xff0000,
                        title="Killer not found!",
                        description="You have to write a valid killer name!",
                        timestamp=datetime.datetime.now(datetime.timezone.utc))
                    
            embed.set_thumbnail(url="https://static.wikia.nocookie.net/deadbydaylight_gamepedia_en/images/9/9e/IconStatusEffects_exposed.png/revision/latest?cb=20170620155518")
            
            embed.add_field(name="Here is a list of killers you can check:",
                            value="Trapper, Shape, Singularity..."
                            )
            
            embed.set_footer(text="FORMAT: !dbd killer addons PSEUDONAME")
            

            await ctx.send(embed=embed)

            return
        
        # Show the addons
        # Add the item that has the addons
        else:

            # Its an array of tuples
            # Format the tuple to a string
            names = [f"{add[0]}" for add in addons]
            # Join with a comma
            names = ", ".join(names)

            # Put addon[0] in bald
            names = names.replace(addons[0][0], f"**{addons[0][0]}**")

            # Show an embed with the name of the survivor and the image
            embed = discord.Embed(
                color=0xff0000,
                timestamp=datetime.datetime.now(datetime.timezone.utc))
            
            embed.set_author(name=f"From {killer[0]}", icon_url=killer[-1])
            
            # Title of the embed bold and centered
            embed.add_field(name=f"Power addons:",
                            value=f"_{names}_",
                            inline=False)
            
            # # Add the images
            # # Get the images
            images = [add[-1] for add in addons]
            
            image_index = 0
            total_images = len(images)
            current_image = images[image_index]
            embed.set_image(url=current_image)
            perkName = addons[image_index][0]
            embed.set_footer(text=f'Addon: {perkName}')

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
                    perkName = addons[image_index][0]
                    # Edit, rechange the addon into normal, and focus in bald the new one
                    names = [f"{add[0]}" for add in addons]
                    # Join with a comma
                    names = ", ".join(names)

                    # Put the new addon in bold
                    names = names.replace(addons[image_index][0], f"**{addons[image_index][0]}**")

                    embed.set_field_at(0, name=f"Addons:",
                            value=f"_{names}_",
                            inline=False)
                    

                    embed.set_image(url=current_image)
                    embed.set_footer(text=f'Addon: {perkName}')
                    await msg.edit(embed=embed)
                    await msg.remove_reaction(reaction, user)
                except asyncio.TimeoutError:
                    break

        
        
        

        

           






    # Group of commands
    @commands.group(name="killer", aliases=["k"], invoke_without_command=True) #, case_insensitive=True)
    async def killer(self, ctx, *, killerName : str = None):
        """
        Shows information about a killer or a random killer
        """
        
        await self.__killer_group(ctx, killerName)

    @killer.command(name="addons", aliases=["a"])
    async def killer_addons(self, ctx, *, killerName : str = None):
        """
        Shows the addons of a killer or a random killer
        """
        await self.__killer_addons(ctx, killerName)


async def setup(bot: commands.Bot):
    await bot.add_cog(KillerCog(bot))