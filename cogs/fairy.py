import discord
import asyncio
from discord.ext.commands import Cog
from discord.commands import slash_command

from config import KertColor, KertVer

import requests
import json
import datetime as dt

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

        with open(f'fairy_archive/{dt.datetime.now().strftime("%Y.%m")}.txt', 'a') as archive:
            archive.write(dt.datetime.now().strftime(f'%Y-%m-%dT%H:%M:%S <{ctx.author.name}> <{ctx.guild}> {ctx.author.id} {1 if is_fairy else 0}\n'))
            
    @slash_command(name='요정랭킹')
    async def fairyRank(self, ctx):
        """`/지성이있나요` 명령어를 얼마나 사용했는지 알려줍니다."""
        
        with open(f'fairy_archive/{dt.datetime.now().strftime("%Y.%m")}.txt', 'r') as archive:
            fairyCounter = dict()
            
            while True:
                log = tuple(map(int, archive.readline().split()[-2:]))
                if not log: break
                
                if log[0] not in fairyCounter:
                    fairyCounter[log[0]] = [1, 0]
                else:
                    fairyCounter[log[0]][0] += 1
                    
                fairyCounter[log[0]][1] += log[1]

        commandRankList = sorted(fairyCounter.items(), key=lambda x: x[1][0], reverse=True)
        succeedRankList = sorted(fairyCounter.items(), key=lambda x: x[1][1], reverse=True)
        
        
        if ctx.author.id not in fairyCounter:
            myCommandRankMsg = f'시도 순위\n{ctx.author.name}님은 명령어를 사용하시지 않았습니다'
            mySucceedRankMsg = f'성공 순위\n{ctx.author.name}님은 명령어를 사용하시지 않았습니다'
        else:
            myCommandRank = commandRankList.index((ctx.author.id, fairyCounter[ctx.author.id]))
            mySucceedRank = succeedRankList.index((ctx.author.id, fairyCounter[ctx.author.id]))
            
            myCommandRankMsg = f'시도 순위\n{ctx.author.name}님은 {myCommandRank+1}위({commandRankList[myCommandRank][1][0]}회) 입니다.'
            mySucceedRankMsg = f'성공 순위\n{ctx.author.name}님은 {mySucceedRank+1}위({succeedRankList[mySucceedRank][1][1]}회) 입니다.'


        commandRank = ''
        succeedRank = ''
        
        for rank in range(3 if len(fairyCounter) >= 3 else len(fairyCounter)):
            commandRank += f'{rank+1}위. {await self.bot.fetch_user(commandRankList[rank][0])}({commandRankList[rank][1][0]}회)\n'
            succeedRank += f'{rank+1}위. {await self.bot.fetch_user(succeedRankList[rank][0])}({succeedRankList[rank][1][1]}회)\n'


        rankEmbed = discord.Embed(title='요정 랭킹', color=KertColor)
        rankEmbed.add_field(name=myCommandRankMsg, value=commandRank, inline=True)
        rankEmbed.add_field(name=mySucceedRankMsg, value=succeedRank, inline=True)
        rankEmbed.set_footer(text=KertVer)
        
        await ctx.respond(embed=rankEmbed)

def setup(bot):
    bot.add_cog(Fairy(bot))