import discord
import asyncio
from discord.ext.commands import Cog
from discord.commands import slash_command

class Meal(Cog):
    def __init__(self, bot):
        self.bot = bot

    @slash_command(name='점메추')
    async def recommend_lunch(self, ctx):
        """점심 메뉴를 추천해줍니다."""
        
        await ctx.respond(discord.Embed(title='점메추', description='요정이 열심히 개발 중...'))
        
    

def setup(bot):
    bot.add_cog(Meal(bot))