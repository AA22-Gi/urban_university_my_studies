import logging

from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from config import *
from keyboards import *
import texts


logging.basicConfig(level=logging.INFO)

bot = Bot(token=API)
db = Dispatcher(bot, storage=MemoryStorage())



if __name__ == '__main__':
    executor.start_polling(db, skip_updates=True)
