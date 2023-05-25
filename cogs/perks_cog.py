import discord
from discord.ext import commands

import datetime, traceback, asyncio

from services import PerkService, SurvivorService

class PerksCog(commands.Cog):

    def __init__(self, bot: commands.Bot):
        """

        """
        self.bot = bot
        self.perkService = PerkService()
        self.survivorService = SurvivorService()

    
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
            perks = self.survivorService.get_survivor_perks(survivorName=survivorName)
        elif killerName != None:
            perks = self.survivorService.get_killer_perks(survivorName=None, killerName=killerName)
        else:
            return None
    
        return perks

    # self.survivorService.checkName(survivorName) isSurvivor

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
                    # url: https://static.wikia.nocookie.net/deadbydaylight_gamepedia_en/images/5/56/Atl_Loadout_Icon_Cruelty.png/revision/latest?cb=20210604022641
                    await ctx.send("https://static.wikia.nocookie.net/deadbydaylight_gamepedia_en/images/5/56/Atl_Loadout_Icon_Cruelty.png/revision/latest?cb=20210604022641")
                    # Message saying that the perk was not found, centerered and in bold
                    await ctx.send(f"**{perkN}** was not found (case sensitive)")

                    # Show the list of perks
                    await ctx.send("Here is a list of perks you can check:")
                    await ctx.send("https://deadbydaylight.fandom.com/wiki/Perks")
                    await ctx.send("Or you can use the command **!dbd randomPerk** to get a random perk")

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

    async def __perks_of(self, ctx, ownerName):
        try:

            # Check if is a killer or a survivor
            isSurv = self.survivorService.checkName(ownerName)

            if isSurv:
                # Get the perks of the survivor
                perks = self.__getPerksOf(ownerName,None)

            else:
                # Get the perks of the killer
                perks = self.__getPerksOf(None,ownerName)

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
                    perkName = perks[image_index][0]
                    embed.set_image(url=current_image)
                    embed.set_footer(text=f'Perk: {perkName}')
                    await msg.edit(embed=embed)
                    await msg.remove_reaction(reaction, user)
                except asyncio.TimeoutError:
                    break

        except Exception as e:
            await ctx.send(f'```{traceback.format_exception(e)}```')

    @commands.group(description="Command group for Perks", invoke_without_command=True, pass_context=True)
    async def perks(self, ctx, *, arg1 = None):
        await self.__perks_group(ctx, arg1)

    @perks.command(description="Subcommand for getting random survivor perk")
    async def survivor(self, ctx):
        await self.__perks_survivor(ctx)

    @perks.command(description="Subcommand for getting random killer perk")
    async def killer(self, ctx):
        await self.__perks_killer(ctx)

    @perks.command(name="of", description="Find perks that belong to a certain killer or survivor.")
    async def perks_of(self, ctx, *, arg1):
        await self.__perks_of(ctx, arg1)

async def setup(bot):
    await bot.add_cog(PerksCog(bot))