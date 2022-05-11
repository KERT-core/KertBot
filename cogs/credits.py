import discord
import asyncio
from discord.ext.commands import Cog
from discord.commands import slash_command

from config import KertColor, KertVer

class Credits(Cog):
    def __init__(self, bot):
        self.bot = bot

    @slash_command(name='개발진')
    async def credits(self, ctx):
        """컬트봇의 개발진들을 보여줍니다."""
        
        members = '''
19 김다훈
21 김기홍
22 이지성
22 정경호
22 조은정
       '''
        
        creditEmbed = discord.Embed(title='개발진', description='', color=KertColor)
        creditEmbed.add_field(name=members, value='special thx to 22 황지영')
        creditEmbed.set_footer(text=KertVer)
        
        await ctx.respond(embed=creditEmbed)

def setup(bot):
    bot.add_cog(Credits(bot))