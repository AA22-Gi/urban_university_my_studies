from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import asyncio

from pyexpat.errors import messages

from api_bot import API
from aiogram.dispatcher.filters.state import State, StatesGroup

api = API
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())


class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()


    @dp.message_handler(message=['Calories'])
    async def set_age(message):
        await message.answer('Введите свой возраст:')

    def set_growth(message, state):
        pass

    def set_weight(message, state):
        pass

    def send_calories(message, state):
        pass


@dp.message_handler(commands=['start'])
async def start(message):
    await message.answer('Привет! Я бот помогающий твоему здоровью.')


@dp.message_handler()
async def all_massages(message):
    await message.answer('Введите команду /start, чтобы начать общение.')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
