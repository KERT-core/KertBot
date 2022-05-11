# 조은정, 정경호
# 컬방 열렸나요?
# 컬방 열어주세요!

import discord
import asyncio
from discord.ext.commands import Cog
from discord.commands import slash_command, Option

is_open = False

class Isopen(Cog):
    def __init__(self,bot):
        self.bot = bot
    
    @slash_command(name='열렸나요')
    async def open(self,ctx):
        """컬방이 열려있는지 알려줍니다."""
        if is_open:
            await ctx.respond('열렸어요')
        else:
            await ctx.respond('닫혔어요')

def setup(bot):
    bot.add_cog(Isopen(bot))
