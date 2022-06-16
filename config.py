import base64

botName = 'KertBot'
botID = 976727339239100466
botToken = base64.b64decode(open('token', 'r').readline()).decode('ascii')
EXTENSIONS = ['cogs.help', 'cogs.open', 'cogs.fairy', 'cogs.info']

KertColor = 0x000000
KertVer = '컬트봇#8958 | V1.0'