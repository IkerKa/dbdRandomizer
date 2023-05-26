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

    
    