import discord
import asyncio
from discord.ext.commands import Cog, has_permissions
from discord.commands import slash_command, Option

from config import *

import requests
import json

bot = discord.Bot()

if __name__ == '__main__':
    for extension in EXTENSIONS:
        try:
            bot.load_extension(extension)
        except Exception as e:
            print('cannot be loaded {}\n{}'.format(extension, e))

@bot.event
async def on_ready():
    print('Build succeeded')
    print(botName)
    print(botID)
    print('=============')

    await bot.change_presence(status=discord.Status.online, activity=discord.Game('컬방에서 감시'))

bot.run(botToken)