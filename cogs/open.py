# 조은정, 정경호
# 컬방 열렸나요?
# 컬방 열어주세요!

import discord
import asyncio
from discord.ext.commands import Cog
from discord.commands import slash_command, Option

import RPI.GPIO as GPIO
import time

is_open = False

class Open(Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @slash_command(name='열렸나요')
    async def isopen(self, ctx):
        """컬방이 열려있는지 알려줍니다."""
        
        if is_open:
            await ctx.respond('열렸어요')
        else:
            await ctx.respond('닫혔어요')
            
    @slash_command(name='열어주세요')
    async def openplz(self, ctx):
        """컬방 안의 사람들이 문을 열어주도록 합니다."""
        
        buzzer = 13
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(buzzer, GPIO.OUT)
        GPIO.setwarnings(False)
        
        PWM = GPIO.PWM(buzzer, 262)
        PWM.start(50.0)
        time.sleep(3)
        
        PWM.stop()
        GPIO.cleanup()

def setup(bot):
    bot.add_cog(Open(bot))