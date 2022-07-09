import time
import os
import subprocess
import asyncio

from telebot.async_telebot import AsyncTeleBot

import r_path
from set_path.set_path import SetRPath
from config import bot_config
import bot_func

# set path
SetRPath(os.getcwd())

# some bot settings
bot=AsyncTeleBot(bot_config.token,parse_mode='HTML')
# get hostname
p=subprocess.run('hostname',shell=True,stdout=subprocess.PIPE)
hostname=p.stdout
hostname=hostname.decode('utf-8')
hostname=hostname.replace('\n','')
link_msg='<strong>Bot Server Started</strong>\n\n'
link_msg+=f'Server <strong>{hostname}</strong> started at <strong>{r_path.r_path}</strong>'



# Now is the function implement
@bot.message_handler(commands=['start', 'help'])
async def send_bot_intro(message):
    '''Catch Welcome And Help Message and send some Introduction'''
    re_text=bot_func.GetBotIntro()
    await bot.reply_to(message,re_text)

ok_text='ok'
async def print_sth_ok(text:str)->None:
    print(text,ok_text)

@bot.message_handler(func=lambda message: True)
async def echo_msg(message):
    await bot_func.Dosth(message.text,print_sth_ok())
    await asyncio.sleep(5)
    await bot.reply_to(message,message.text)

# make the bot to get message constantly
asyncio.run(bot.polling())


