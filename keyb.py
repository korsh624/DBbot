from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ContentType
def get_kb():
    kb=InlineKeyboardMarkup()
    ok=InlineKeyboardButton('ok', callback_data='ok')
    claer=InlineKeyboardButton('clear', callback_data='clear')
    kb.add(ok,claer)
    return kb
def get_reg():
    kb = InlineKeyboardMarkup()
    reg = InlineKeyboardButton('ok', callback_data='reg')
    kb.add(reg)
    return kb