import time
import asyncio

from config import bot_config


def GetBotIntro():
    '''Get the bot fundametal info\n
    Don't need any input, this function will read the bot_config file 
    to get thing it need'''
    re_text='<strong>Bot Info</strong>\n\n'
    re_text+=f'<strong>Version:</strong> <strong>{str(bot_config.version)}</strong>\n'
    re_text+=f'<strong>Introduction:</strong> {str(bot_config.intro)}'
    return str(re_text)

async def Dosth(text:str,func) -> None :
    func(text)