import discord
import asyncio
from discord.ext.commands import Cog
from discord.commands import slash_command

class Meal(Cog):
    def __init__(self, bot):
        self.bot = bot

    def recommend_lunch(self, ctx):
        """점심 메뉴를 추천해줍니다."""
        pass
    

def setup(bot):
    bot.add_cog(Meal(bot))