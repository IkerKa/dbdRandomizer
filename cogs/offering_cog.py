import discord
from discord.ext import commands

import datetime, traceback, asyncio

from services import OfferingService, SurvivorService, KillerService

class OfferingsCog(commands.Cog):

    def __init__(self, bot: commands.Bot):
        """

        """
        self.bot = bot
        self.offeringService = OfferingService()
        self.survivorService = SurvivorService()
        self.killerService = KillerService()

    
    def __getRandOffering(self, isSurv : int, isKiller : int):

        # access the method to get a random Offering
        # Params: True True bc we want to get a random Offering from the survivors and killers
        offering = self.offeringService.randomOffering(isSurv, isKiller)

        print(offering)
        # print(Offering)
        # print(owner)

        offering_name = offering[0]
        offering_description = offering[1]
        offering_image = offering[2]
        # Owner: another query

        # We return the name, description and image of the Offering
        return offering_name, offering_description, offering_image

    # This is not necessary
    def __getOfferingsOf(self,survivorName=None, killerName=None):
    
        if survivorName != None:
            offerings = self.survivorService.get_survivor_offerings(survivorName)
        elif killerName != None:
            offerings = self.killerService.get_killer_offerings(killerName)
        else:
            return None
    
        return offerings

    # self.survivorService.checkName(survivorName) isSurvivor
    async def __getOfferingInfo(self,offeringName):
        # We will call the function to get the Offering
        offering, offering_description, offering_image = self.offeringService.get_offering(offeringName)

        # We return the name, description and image of the Offering
        return offering, offering_description, offering_image
    

    async def __randomOffering(self, ctx, isSurv : int, isKiller : int):
        # Just inline the image of the Offering and the name of the Offering in the same line
        offering_name, _, offering_image = self.__getRandOffering(isSurv, isKiller)

        # Show an embed with the name of the Offering and the image
        embed = discord.Embed(
            color=0xff0000,
            timestamp=datetime.datetime.now(datetime.timezone.utc))

        # Title of the embed bold and centered
        embed.add_field(name="Offering:",
                        value=f"**{offering_name}**",
                        inline=False)
        
        embed.set_image(url=offering_image)

        # We will send the embed
        await ctx.send(embed=embed)


    async def __offerings_group(self, ctx, offeringN):
        """
        Simple random Offering, or detailed Offering given an argument.
        """
        try:
            if offeringN is None:
                await self.__randomOffering(ctx, 1, 1)

            else:
                # Detailed Offering, name is arg1

                # We will call the function to get the Offering
                ok = True
                try:
                    offering, offering_description, offering_image =  await self.__getOfferingInfo(offeringN)
                except:
                    ok = False

                if not ok:
                    # Send an image with the perk not found
                    embed = discord.Embed(
                        # Perk _<perkName>_ not found
                        title=f"offering _{offeringN}_ not found",
                        description="Check the name of the offering and try again.",
                        color=0xff0000,
                        timestamp=datetime.datetime.now(datetime.timezone.utc))
                    
                    
                    embed.set_thumbnail(url="https://static.wikia.nocookie.net/deadbydaylight_gamepedia_en/images/5/56/Atl_Loadout_Icon_Cruelty.png/revision/latest?cb=20210604022641")

                    embed.set_footer(
                        text="Use !dbd offerings for more info",

                    )
                    # We will send the embed
                    await ctx.send(embed=embed)

                else:
                    # We will create the embed
                    # timestamp utc + 2
                    embed = discord.Embed(
                        title=offering,
                        description=offering_description,
                        color=0x00fff0,
                        timestamp=datetime.datetime.now(datetime.timezone.utc))

                    embed.set_thumbnail(url=offering_image)

                    # We will send the embed
                    await ctx.send(embed=embed)

        except Exception as e:
            await ctx.send(f'```{traceback.format_exception(e)}```')

    async def __offerings_survivor(self, ctx):
        try:
            await self.__randomOffering(ctx, 1, 0)
        except Exception as e:
            await ctx.send(f'```{traceback.format_exception(e)}```')

    async def __offerings_killer(self, ctx):
        try:
            await self.__randomOffering(ctx, 0, 1)
        except Exception as e:
            await ctx.send(f'```{traceback.format_exception(e)}```')

    async def __offerings_of(self, ctx, ownerName : str):
        pass

    @commands.group(description="Command group for offerings", invoke_without_command=True, pass_context=True)
    async def offerings(self, ctx, *, arg1 = None):
        await self.__offerings_group(ctx, arg1)

    @offerings.command(description="Subcommand for getting random survivor offering")
    async def survivor(self, ctx):
        await self.__offerings_survivor(ctx)

    @offerings.command(description="Subcommand for getting random killer offering")
    async def killer(self, ctx):
        await self.__offerings_killer(ctx)

async def setup(bot):
    await bot.add_cog(OfferingsCog(bot))