import time
import os
import subprocess

import telebot

import r_path
from set_path.set_path import SetRPath
from config import bot_config
import bot_func

# set path
SetRPath(os.getcwd())

# some bot settings
bot=telebot.TeleBot(bot_config.token,parse_mode='HTML')
# get hostname
p=subprocess.run('hostname',shell=True,stdout=subprocess.PIPE)
hostname=p.stdout
hostname=hostname.decode('utf-8')
hostname=hostname.replace('\n','')
link_msg='<strong>Bot Server Started</strong>\n\n'
link_msg+=f'Server <strong>{hostname}</strong> started at <strong>{r_path.r_path}</strong>'
bot.send_message(bot_config.admin,link_msg)



# Now is the function implement
@bot.message_handler(commands=['start', 'help'])
def send_bot_intro(message):
    '''Catch Welcome And Help Message and send some Introduction'''
    re_text=bot_func.GetBotIntro()
    bot.reply_to(message,re_text)



# make the bot to get message constantly
bot.infinity_polling()
