from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

start_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Рассчитать'),
            KeyboardButton(text='Информация')
        ],
        [KeyboardButton(text='Купить')]
    ], resize_keyboard=True
)

catalog_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Рассчитать норму калорий', callback_data='calories')],
        [InlineKeyboardButton(text='Формулы расчёта', callback_data='formulas')],
    ]
)

product_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Шейкер', callback_data='shaker')],
        [InlineKeyboardButton(text='Скакалка', callback_data='jump_rope')],
        [InlineKeyboardButton(text='Фитнес-резинки', callback_data='elastic_band')],
        [InlineKeyboardButton(text='Гантели', callback_data='dumbbells')]
    ]
)
