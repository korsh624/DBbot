from aiogram import executor, types, Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ContentType

from keyb import get_kb, get_reg
from config import API_TOKEN
import logging
storage = MemoryStorage()
logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot, storage=storage)
person=[]

class Registr(StatesGroup):
    whating_fname=State()
    whating_lname= State()
    whating_ou = State()

@dp.message_handler(commands=['start'])
async def registr(message:types.Message, state: FSMContext):
    await message.answer("Зарегистрируйтесь!",reply_markup=get_reg())

@dp.callback_query_handler(text='reg')
async def registr(cal:types.CallbackQuery, state: FSMContext):
    global person
    person.append(cal.from_user.id)
    await cal.answer()
    await cal.message.answer("Введите ваше имя")
    await state.set_state(Registr.whating_fname.state)

@dp.message_handler(state=Registr.whating_fname)
async def inputname(message:types.Message, state: FSMContext):
    global person
    person.append(message.text)
    await message.answer('Введите фамилию')
    await state.set_state(Registr.whating_lname.state)

@dp.message_handler(state=Registr.whating_lname)
async def inputname(message:types.Message, state: FSMContext):
    global person
    person.append(message.text)
    await message.answer('Введите название ОУ')
    await state.set_state(Registr.whating_ou.state)


@dp.message_handler(state=Registr.whating_ou)
async def inputname(message:types.Message, state: FSMContext):
    global person
    person.append(message.text)
    await message.answer(f'Проверьте данные -  {person[1]} {person[2]} {person[3]}',reply_markup=get_kb())
    await state.finish()

@dp.callback_query_handler(text='ok')
async def writedata(cal:types.CallbackQuery):
    await cal.answer()
    await cal.message.answer("Данные записаны")

    global person
    person = []

@dp.callback_query_handler(text='clear')
async def writedata(cal:types.CallbackQuery):
    await cal.answer()
    await cal.message.answer("Начните заново",reply_markup=get_reg())
    global person
    person = []


if __name__ == '__main__':
    executor.start_polling(dp,skip_updates=True)