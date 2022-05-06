import discord
import asyncio
from discord.ext.commands import Cog
from discord.commands import slash_command

class Fairy(Cog):
    def __init__(self, bot):
        self.bot = bot

    @slash_command(name='지성이있나요?')
    async def fairy(self, ctx):
        """컬방에 지성이의 유무를 알려줍니다."""
        url = ''

def setup(bot):
    bot.add_cog(Fairy(bot))