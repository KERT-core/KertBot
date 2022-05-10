import discord
import asyncio
from discord.ext.commands import Cog
from discord.commands import slash_command

fairyDevice = [r'2A:BC:84:94:87:9C', r'1C:C1:0C:E2:54:78', r'3E:57:55:B5:7A:8A', r'EE:A6:85:AE:31:2C', r'56:98:A2:57:F4:C3']

class Fairy(Cog):
    def __init__(self, bot):
        self.bot = bot


    @slash_command(name='지성이있나요')
    async def fairy(self, ctx):
        """컬방에 지성이의 유무를 알려줍니다."""
        
        is_fairy = False
        
        # 이지성 KERT_5G 기기별 MAC ADRESS
        # 핸드폰:   2A:BC:84:94:87:9C
        # 노트북:   1C:C1:0C:E2:54:78
        # 아이패드: 3E:57:55:B5:7A:8A
        
        # 이지성 KERT_2G 기기별 MAC ADRESS        
        # 핸드폰:   EE:A6:85:AE:31:2C
        # 노트북:   1C:C1:0C:E2:54:78
        # 아이패드: 56:98:A2:57:F4:C3
        
    
        url = r'http://router.asus.com/Main_Login.asp'
        kertList = []
        
        for adress in fairyDevice:
            if adress in kertList:
                is_fairy = True
                break
        
        if is_fairy:
            await ctx.respond('있습니다!')
        else:
            await ctx.respond('없어요ㅠㅠ')

def setup(bot):
    bot.add_cog(Fairy(bot))
    
# import requests
# from bs4 import BeautifulSoup

# URL = 'http://router.asus.com/Main_Login.asp'
# LOGIN_DATA = {
#     'Username': 'Kert', 
#     'Password': 'password123'
# }

# session = requests.session()
# response = session.get(URL, data=LOGIN_DATA)
# response.raise_for_status()

# soup = BeautifulSoup(response.text, 'html.parser')