import asyncio
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

# --------------------------------------


def get_update():
    markup=InlineKeyboardMarkup()
    markup.row_width=1
    markup.add(InlineKeyboardButton('⏏️检查更新',callback_data='cb_check_update'))
    return markup