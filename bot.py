from aiogram import types, Bot, Dispatcher,executor
from config import API_TOKEN
import logging
import os
import sqlite3
def create_table():
   conn = sqlite3.connect('users.db')
   cur = conn.cursor()
   cur.execute("""CREATE TABLE IF NOT EXISTS users(
               userid INT PRIMARY KEY,
               username TEXT,
               message TEXT);
               """)
   conn.commit()
   cur.close()
   conn.close()

logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(text='база')
async def echo(message: types.Message):
   conn = sqlite3.connect('users.db')
   cur = conn.cursor()
   user = cur.execute(f"""SELECT * FROM users WHERE userid = {message.chat.id}""").fetchone()
   if not user:
       print('NO')
   else:
       print("YES")
   await message.answer(message.text)
   if not user:
       data = (message.chat.id, message.chat.username)
       cur.execute("""INSERT INTO users(userid, username) VALUES (?,?)""", data)
       conn.commit()
       conn.close()
       await message.answer('Вы добавлены в базу данных')
   else:
       print(user)
       id, username = user[0],user[1]
       await message.answer(f'Вы уже есть в базе данных. Ваш id = {id}, username = {username}')


if __name__ == '__main__':
    create_table()
    executor.start_polling(dp,skip_updates=True)