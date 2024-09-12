from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import asyncio
from api_bot import API

api = API
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())


@dp.message_handler()
async def start(message):
    pass


@dp.message_handler()
async def all_massages(message):
    pass


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
