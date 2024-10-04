from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

start_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Рассчитать'),
            KeyboardButton(text='Информация')
        ],
        [
            KeyboardButton(text='Купить'),
            KeyboardButton(text='Регистрация')
        ]
    ], resize_keyboard=True
)

catalog_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Рассчитать норму калорий', callback_data='calories')],
        [InlineKeyboardButton(text='Формула расчёта', callback_data='formulas')],
    ]
)

product_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Шейкер', callback_data='product_buying'),
         InlineKeyboardButton(text='Скакалка', callback_data='product_buying'),
         InlineKeyboardButton(text='Фитнес-резинки', callback_data='product_buying'),
         InlineKeyboardButton(text='Гантели', callback_data='product_buying')]
    ]
)
