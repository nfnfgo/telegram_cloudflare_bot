import time
import asyncio

from config import bot_config


def GetBotIntro():
    '''Get the bot fundametal info\n
    Don't need any input, this function will read the bot_config file 
    to get thing it need'''
    re_text='**Bot Info**\n\n'
    re_text+=f'**Version:** **{str(bot_config.version)}**\n'
    re_text+=f'**Introduction:** {str(bot_config.intro)}'
    return str(re_text)

async def Dosth(text:str,func) -> None :
    func(text)