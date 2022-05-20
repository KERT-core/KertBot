import discord
import asyncio
from discord.ext.commands import Cog
from discord.commands import slash_command

from config import KertColor, KertVer

class Info(Cog):
    def __init__(self, bot):
        self.bot = bot

    @slash_command(name='컬방')
    async def credits(self, ctx):
        """컬방에 대한 정보를 알려줍니다."""
        
        kertEmbed = discord.Embed(title='컬방', description='', color=KertColor)
        kertEmbed.add_field(name='위치', value='중앙도서관 옆 정보화본부(110동) 110호', inline=False)
        kertEmbed.add_field(name='전화번호', value='053-950-6413', inline=False)
        kertEmbed.set_footer(text=KertVer)
        
        await ctx.respond(embed=kertEmbed)
        
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
       
        special_thanks = '''
special thx to
18 양태관, 21 이주형, 22 황지영
       '''
        
        creditEmbed = discord.Embed(title='개발진', description='', color=KertColor)
        creditEmbed.add_field(name=members, value=special_thanks)
        creditEmbed.set_footer(text=KertVer)
        
        await ctx.respond(embed=creditEmbed)

def setup(bot):
    bot.add_cog(Info(bot))