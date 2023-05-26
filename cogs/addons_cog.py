import discord
from discord.ext import commands

import services as services
from services import addOn_service

import datetime, traceback

class AddOnCog(commands.Cog):

    def __init__(self, bot: commands.Bot):
        """
        Constructor of the class
        """
        self.bot = bot
        self.addOnService = addOn_service.AddOnService()

    # Private methods
    # ---> comando: !dbd randomAddon
    def __getRandAddon(self):
        addonService = services.AddOnService()

        addon, itemImage = addonService.random_addOn()

        addon_name = addon[0]
        addon_belongsTo = addon[1]
        addon_description = addon[2]
        addon_image = addon[3]

        return addon_name, addon_belongsTo, addon_description, addon_image, itemImage
        

    # ---> comando: !dbd addon <addonName>
    def __getAddonInfo(self,addonName):
        addonService = services.AddOnService()

        isOnDB = addonService.check_name(addonName)

        if isOnDB == False:
            return None, None, None, None, None, None, None

        addon, info, generalName, isPower = addonService.get_addOn(addonName)

        if addon == None:
            return None, None, None, None, None, None

        addon_name = addon[0]
        addon_belongsTo = addon[1]
        addon_description = addon[2]
        addon_image = addon[3]

        return addon_name, addon_belongsTo, addon_description, addon_image, info, generalName, isPower
    
    async def __addon_group(self, ctx, adName : str):
        """
            Simple random addon, or detailed addon given an argument.
        """

        

        # If the argument is None, we just want a random addon
        if adName is None:
            # Just inline the image of the addon and the name of the addon in the same line
            try:
                # We will call the function to get the addon
                addon_name, addon_belongTo, addon_description, addon_image, itemImage = self.__getRandAddon()


                # [Warning] It should be always an item 
                embed = discord.Embed(
                    title=addon_name,
                    description=addon_description,
                    color=0x00ff00,
                    timestamp=datetime.datetime.now(datetime.timezone.utc)
                )

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
                await ctx.send(embed=embed)



            except Exception as e:
                await ctx.send(f'```{traceback.format_exception(e)}```')

        # If the argument is not None, we want a detailed addon
        else:

            try:
                addon_name, addon_belongsTo, addon_description, addon_image, info, generalName, isPower = self.__getAddonInfo(adName)

                # Check if the addon was found
                if addon_name == None:
                    # Send an imagen with the addon not found
                    embed = discord.Embed(
                        title="Addon not found :(",
                        description="You sure that addon exists?",
                        color=0xff0000,
                        timestamp=datetime.datetime.now(datetime.timezone.utc))
                    
                    embed.set_thumbnail(url="https://static.wikia.nocookie.net/deadbydaylight_gamepedia_en/images/e/e5/Unknown_QuestionMark.png/revision/latest?cb=20210929093312")
                    
                    # We will send the embed
                    await ctx.send(embed=embed)
                    return
                
                if not isPower:
                
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
                    items = [f"**{item[0]}**" for item in info]
                    # Join with a comma
                    items = ", ".join(items)
                    embed.add_field(name="Items that can use this addon:",
                                    value=items,
                                    inline=False)
                    
                    # We will send the embed
                    await ctx.send(embed=embed)
                
                else:

                    # print(info)

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
                        name=f"From: {generalName}",
                        icon_url=info[-1]
                    )

                    embed.set_thumbnail(url=addon_image)

                    await ctx.send(embed=embed)


            except Exception as e:
                await ctx.send(f'```{traceback.format_exception(e)}```')


    # Commands
    # ---> comando: !dbd randomAddon
    @commands.command(name="addon", aliases=["randAddon", "randAddOn", "randomAddOn"])
    async def random_addon(self, ctx, *, adName =None):
        """
            Simple random addon, or detailed addon given an argument.
        """
        await self.__addon_group(ctx, adName)



async def setup(bot):
    await bot.add_cog(AddOnCog(bot))



