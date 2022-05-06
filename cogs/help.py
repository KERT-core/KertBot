import discord
import asyncio
from discord.ext.commands import Cog
from discord.commands import slash_command, OptionV

class Help(Cog):
    def __init__(self, bot):
        self.bot = bot

    @slash_command()
    async def help(self, ctx):
        """명령어들의 종류를 크게 구분해서 보여줄게요."""

def setup(bot):
    bot.add_cog(Help(bot))