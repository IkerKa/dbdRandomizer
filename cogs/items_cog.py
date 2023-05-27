
import datetime
import traceback
import asyncio

import discord
from discord.ext import commands

import services as services
from services import item_service

class ItemCog(commands.Cog):
     
    def __init__(self, bot: commands.Bot):
         """
         Constructor of the class
         """
         self.bot = bot
         self.itemService = item_service.ItemService()


    # Private methods
    # ---> comando: !dbd item (no name)
    def __getRandItem(self):

        item = self.itemService.get_item(None,False)

        itemName = item[0]
        # itemDescription = item[1]
        itemImage = item[2]

        return itemName, itemImage
    
    # ---> comando: !dbd item <itemName>
    def __getItemInfo(self,itemName):
        item = self.itemService.get_item(itemName,True)

        if item == None:
            return None, None, None, None

        itemName = item[0]
        itemDescription = item[1]
        itemImage = item[2]

        return itemName, itemDescription, itemImage, None
    
    # ---> comando: !dbd item addons <itemName>
    def __getItemAddons(self,iName):
        return self.itemService.get_addons(iName)


    async def __item_group(self, ctx, iName : str):
        """
            Simple random item, or detailed item given an argument.
        """

        # If the argument is None, we just want a random item
        if iName is None:
            # Just inline the image of the item and the name of the item in the same line
            try:
                # We will call the function to get the item
                itemName, itemImage = self.__getRandItem()

                # We will create the embed
                embed = discord.Embed(
                    title=itemName,
                    description="",
                    colour=discord.Colour.dark_red()
                )

                # We will add the image of the item
                embed.set_image(url=itemImage)

                # We will send the embed
                await ctx.send(embed=embed)

            except Exception as e:
                # We will send the error message
                await ctx.send("WHOOOOPSIES :o, there is no item in the database")

        else:
            # Detailed item
            try:
                # We will call the function to get the item
                itemName, itemDescription, itemImage, _ = self.__getItemInfo(iName)
                
                # If the item is None, we will send an error message
                if itemName is None:
                    # We will send the error  message
                    embed = discord.Embed(
                        title="Ou nou...",
                        description="The item you are looking {} doesn't exist".format(iName),
                        colour=discord.Colour.dark_red()
                    )

                    # We will add the image of the item
                    embed.set_thumbnail(url="https://static.wikia.nocookie.net/deadbydaylight_gamepedia_en/images/b/b4/IconHelp_movementSpeed.png/revision/latest?cb=20201111211324")
                    embed.set_footer(text="You sure you wrote it correctly?")
                    # We will send the embed
                    await ctx.send(embed=embed)

                    return

                else:

                    # We will create the embed
                    embed = discord.Embed(
                        title=itemName,
                        description=itemDescription,
                        colour=discord.Colour.dark_gold()
                    )

                    # We will add the image of the item
                    embed.set_image(url=itemImage)

                    # We will send the embed
                    await ctx.send(embed=embed)

            except Exception as e:
                # traceback.print_exc()
                await ctx.send(f'```{traceback.format_exception(e)}```')

    async def __item_addons(self, ctx, iName : str):

        item, addons = self.__getItemAddons(iName)

        if item is None:
            # We will send the error  message
            embed = discord.Embed(
                title="Ou nou...",
                description="The item you are looking {} doesn't exist".format(iName),
                colour=discord.Colour.dark_red()
            )

            # We will add the image of the item
            embed.set_thumbnail(url="https://static.wikia.nocookie.net/deadbydaylight_gamepedia_en/images/b/b4/IconHelp_movementSpeed.png/revision/latest?cb=20201111211324")
            embed.set_footer(text="You sure you wrote it correctly?")

            # We will send the embed
            await ctx.send(embed=embed)

            return

        
        elif addons is None:
            await ctx.send(f"**{iName}** doesn't have any addons")

        else:

            # Add the item that has the addons
            

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
            
            embed.set_author(name=f"For the item: {item[0]}", icon_url=item[-1])
            
            # Title of the embed bold and centered
            embed.add_field(name=f"Addons:",
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
                    embed.set_footer(text=f'Perk: {perkName}')
                    await msg.edit(embed=embed)
                    await msg.remove_reaction(reaction, user)
                except asyncio.TimeoutError:
                    break

    # Commands
    # ---> comando: !dbd item (no name)
    @commands.group(name="item", description="Item commands.", invoke_without_command=True, aliases=["i"])
    async def item(self, ctx, *, itemName: str = None):
        """
            Simple random item, or detailed item given an argument.
        """
        await self.__item_group(ctx, itemName)

    # ---> comando: !dbd item addons <itemName>
    @item.command(name="addons", description="Addons from a given item.")
    async def addons(self, ctx, *, itemName):
        """
            Detailed item with addons given an argument.
        """
        # await self.__item_group(ctx, itemName)
        await self.__item_addons(ctx, itemName)

async def setup(bot: commands.Bot):
    await bot.add_cog(ItemCog(bot))
