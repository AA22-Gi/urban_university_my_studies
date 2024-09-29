from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import asyncio
from pyexpat.errors import messages
from api_bot import API
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

api = API
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

kb = ReplyKeyboardMarkup()
button1 = KeyboardButton(text='Рассчитать')
button2 = KeyboardButton(text='Информация')


class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()


@dp.message_handler(commands=['start'])
async def start(message):
    await message.answer('Привет! Я бот помогающий твоему здоровью.\n'
                         'Если Вы хотите рассчитать суточную норму калорий введите "Calories"')


@dp.message_handler(text=['Рассчитать'])
async def set_age(message):
    await message.answer('Введите свой возраст: ')
    await UserState.age.set()


@dp.message_handler(state=UserState.age)
async def set_growth(message, state):
    if message.text.isdigit():
        await state.update_data(age=message.text)
        await message.answer('Введите свой рост: ')
        await UserState.growth.set()
    else:
        await message.answer('Возраст должен быть целым числом.\n'
                             'Попробуйте ещё раз: ')


@dp.message_handler(state=UserState.growth)
async def set_weight(message, state):
    if message.text.isdigit():
        await state.update_data(weight=message.text)
        await message.answer('Введите свой вес: ')
        await UserState.weight.set()
    else:
        await message.answer('Рост должен быть целым числом.\n'
                             'Попробуйте ещё раз: ')


@dp.message_handler(state=UserState.weight)
async def send_calories(message, state):
    if message.text.isdigit():
        await state.update_data(growth=message.text)
    else:
        await message.answer('Вес должен быть целым числом.\n'
                             'Попробуйте ещё раз: ')
    data = await state.get_data()
    age = int(data['age'])
    growth = int(data['growth'])
    weight = int(data['weight'])
    # упрощенна формула Миффлина для мужчин
    calories = (10 * weight) + (6.25 * growth) - (5 * age) + 5
    await message.answer(f'Ваша норма калорий: {calories} ккал')
    await state.finish()


@dp.message_handler()
async def all_massages(message):
    await message.answer('Введите команду /start, чтобы начать общение.')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)