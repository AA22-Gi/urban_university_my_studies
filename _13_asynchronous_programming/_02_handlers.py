from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import asyncio

api = '7431730886:AAG_OfnRd9Xb6ex7hZXUZTppXz-1Zm0XDek'
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())
