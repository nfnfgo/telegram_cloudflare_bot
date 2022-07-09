import time
import os
import subprocess
import asyncio

from telebot.async_telebot import AsyncTeleBot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

import r_path
from set_path.set_path import SetRPath
from config import bot_config
import bot_func
import gen_inline_botton as botton

# set path
SetRPath(os.getcwd())

# some bot settings
bot=AsyncTeleBot(bot_config.token,parse_mode='markdown')
# get hostname
p=subprocess.run('hostname',shell=True,stdout=subprocess.PIPE)
hostname=p.stdout
hostname=hostname.decode('utf-8')
hostname=hostname.replace('\n','')
link_msg='**Bot Server Started**\n\n'
link_msg+=f'Server **{hostname}** started at **{r_path.r_path}**'

# --------------------------------------------------------------

# Now is the function implement
@bot.message_handler(commands=['start', 'help'])
async def send_bot_intro(message):
    '''Catch Welcome And Help Message and send some Introduction'''
    re_text=bot_func.GetBotIntro()
    await bot.reply_to(message,re_text,reply_markup=botton.get_update())

@bot.callback_query_handler(func=lambda call:True)
async def callback_query(call):
    await bot.answer_callback_query(call.id,'⚠️功能未开放')

@bot.message_handler(commands='cfapi')
async def set_cloudflare_api(message):
    await bot.reply_to(message,
    '⚠️ *功能未开放* \n请直接修改`config/cf_config.py`')

# make the bot to get message constantly
asyncio.run(bot.infinity_polling())
