import time
import os
import telebot
from set_path.set_path import SetRPath
from config import bot_config

# set path
SetRPath(os.getcwd())

# some bot settings
bot=telebot.TeleBot(bot_config.token,parse_mode='HTML')
