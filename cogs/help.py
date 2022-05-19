import discord
import asyncio
from discord.ext.commands import Cog
from discord.commands import slash_command, Option

from config import KertColor, KertVer

class Help(Cog):
    def __init__(self, bot):
        self.bot = bot

    @slash_command()
    async def help(self, ctx):
        """컬트봇의 사용 방법을 알려줍니다."""
        
        helpEmbed = discord.Embed(title='도움말', description='여기서 사용할 수 있는 명령어 모음입니다.', color=KertColor)
        helpEmbed.add_field(name='`/help`', value='컬트봇의 사용 방법을 알려줍니다.', inline=True)
        helpEmbed.add_field(name='`/열렸나요`', value='컬방이 열려있는지 알려줍니다.', inline=True)
        helpEmbed.add_field(name='`/열어주세요`', value='컬방 안의 사람들이 문을 열어주도록 합니다.', inline=True)
        helpEmbed.add_field(name='`/지성이있나요`', value='컬방에 요정이 있는지 알려줍니다.', inline=True)
        helpEmbed.add_field(name='`/컬방`', value='컬방에 대한 정보를 알려줍니다.', inline=True)
        helpEmbed.add_field(name='`/개발진`', value='컬트봇의 개발진들을 보여줍니다.', inline=True)
        helpEmbed.set_footer(text=KertVer)
        
        await ctx.respond(embed=helpEmbed)

def setup(bot):
    bot.add_cog(Help(bot))