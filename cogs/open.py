import discord
import asyncio
from discord.ext.commands import Cog
from discord.commands import slash_command, Option

import RPi.GPIO as GPIO
import time
import pygame

class Open(Cog):
    def __init__(self, bot):
        self.bot = bot
        pygame.mixer.init()
        pygame.mixer.music.load('alarm.mp3')
    
    @slash_command(name='열렸나요')
    async def isopen(self, ctx):
        """컬방이 열려있는지 알려줍니다."""
        
        circuit = 7
        cnt = 0
        
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(circuit, GPIO.OUT)
        GPIO.output(circuit, GPIO.LOW)
        
        time.sleep(0.1)
        GPIO.setup(circuit, GPIO.IN)
        
        while GPIO.input(circuit) == GPIO.LOW and cnt < 11000:
            cnt += 1
        
        if cnt < 10000:
            await ctx.respond('열렸습니다!')
        else:
            await ctx.respond('닫혔어요ㅠㅠ')
            
    @slash_command(name='열어주세요')
    async def openplz(self, ctx):
        """컬방 안의 사람들이 문을 열어주도록 합니다."""
        
        circuit = 7
        cnt = 0
        
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(circuit, GPIO.OUT)
        GPIO.output(circuit, GPIO.LOW)
        
        time.sleep(0.1)
        GPIO.setup(circuit, GPIO.IN)
        
        while GPIO.input(circuit) == GPIO.LOW and cnt < 11000:
            cnt += 1
            
        if cnt < 10000:
            pygame.mixer.music.play()
            await ctx.respond('컬방에 알림음을 울렸습니다.')
        else:
            await ctx.respond('열어줄 사람이 없어요ㅠㅠ')
        
def setup(bot):
    bot.add_cog(Open(bot))