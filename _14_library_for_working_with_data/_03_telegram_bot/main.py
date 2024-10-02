import asyncio
import logging

from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from api_bot import API

from keyboards import *
from texst import *
from fsm import *

logging.basicConfig(level=logging.INFO)

api = API
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())


@dp.message_handler(commands=['start'])
async def start(message):
    await message.answer(hello, reply_markup=start_kb)


@dp.message_handler(text=['Информация'])
async def info(message):
    await message.answer(information)


@dp.message_handler(text=['Рассчитать'])
async def main_menu(message):
    await message.answer('Выберите опцию: ', reply_markup=catalog_kb)


@dp.callback_query_handler(text='formulas')
async def get_formulas(call):
    await call.message.answer(formulas)
    await call.answer()


@dp.callback_query_handler(text=['calories'])
async def set_age(call):
    await call.message.answer('Введите свой возраст: ')
    await call.answer()
    await UserState.age.set()


@dp.message_handler(state=UserState.age)
async def set_growth(message, state):
    if message.text.isdigit():
        await state.update_data(age=message.text)
        await message.answer('Введите свой рост: ')
        await UserState.growth.set()
    else:
        await message.answer(again)


@dp.message_handler(state=UserState.growth)
async def set_weight(message, state):
    if message.text.isdigit():
        await state.update_data(weight=message.text)
        await message.answer('Введите свой вес: ')
        await UserState.weight.set()
    else:
        await message.answer(again)


@dp.message_handler(state=UserState.weight)
async def send_calories(message, state):
    if message.text.isdigit():
        await state.update_data(growth=message.text)
    else:
        await message.answer(again)

    data = await state.get_data()
    age = int(data['age'])
    growth = int(data['growth'])
    weight = int(data['weight'])

    # упрощенна формула Миффлина для мужчин
    calories = (10 * weight) + (6.25 * growth) - (5 * age) + 5
    await message.answer(f'Ваша норма калорий: {calories} ккал')
    await state.finish()


@dp.message_handler(text=['Купить'])
async def prod(message):
    await message.answer('Рады Вас видеть!', reply_markup=product_kb)


@dp.callback_query_handler(text='shaker')
async def prod_1(call):
    with open('1.png', 'rb') as img:
        await call.message.answer_photo(img, 'Шейкер')
    await call.answer()


@dp.callback_query_handler(text='jump_rope')
async def prod_2(call):
    with open('2.png', 'rb') as img:
        await call.message.answer_photo(img, 'Скакалка')
    await call.answer()


@dp.callback_query_handler(text='elastic_band')
async def prod_3(call):
    with open('3.png', 'rb') as img:
        await call.message.answer_photo(img, 'Фитнес-резинки')
    await call.answer()


@dp.callback_query_handler(text='dumbbells')
async def prod_4(call):
    with open('4.png', 'rb') as img:
        await call.message.answer_photo(img, 'Гантели')
    await call.answer()


@dp.message_handler()
async def all_massages(message):
    await message.answer('Введите команду /start, чтобы начать общение.')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
