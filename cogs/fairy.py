import discord
import asyncio
from discord.ext.commands import Cog
from discord.commands import slash_command

import requests
import json

fairyDevice = ['2A:BC:84:94:87:9C', '1C:C1:0C:E2:54:78', '3E:57:55:B5:7A:8A', 'EE:A6:85:AE:31:2C', '56:98:A2:57:F4:C3']

class Fairy(Cog):
    def __init__(self, bot):
        self.bot = bot

    @slash_command(name='지성이있나요')
    async def fairy(self, ctx):
        """컬방에 요정이 있는지 알려줍니다."""
        
        is_fairy = False
        
        # 이지성 KERT_5G 기기별 MAC ADRESS
        # 핸드폰:   2A:BC:84:94:87:9C
        # 노트북:   1C:C1:0C:E2:54:78
        # 아이패드: 3E:57:55:B5:7A:8A
        
        # 이지성 KERT_2G 기기별 MAC ADRESS        
        # 핸드폰:   EE:A6:85:AE:31:2C
        # 노트북:   1C:C1:0C:E2:54:78
        # 아이패드: 56:98:A2:57:F4:C3
        
        with requests.Session() as session:
            login_url = "http://router.asus.com/login.cgi"
            
            login_data = {
                'action_wait': '5',
                'current_page': 'Main_Login.asp',
                'next_page': 'index.asp',
                'login_authorization': 'S0VSVDpwYXNzd29yZDEyMw=='
            }
            login_headers = {
                'Referer':'http://router.asus.com/Main_Login.asp',
                'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36',
            }
        
            login_res = session.post(login_url, headers=login_headers, data=login_data)
            url = "http://router.asus.com/ajax_onboarding.asp"
            headers = {
                'Referer':'http://router.asus.com/index.asp',
                'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36'
            }
            
            res = session.get(url, headers=headers)
            res_text = res.text
            res_text = res_text[res_text.rfind('get_allclientlist'):-36].replace('get_allclientlist = ', '')
            res_json = json.loads(res_text)[0]['B0:6E:BF:66:07:80']
            
            
        kertList = []
        kertList.extend(list(res_json['2G'].keys()))
        kertList.extend(list(res_json['5G'].keys()))
        
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