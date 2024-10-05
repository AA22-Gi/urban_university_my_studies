import asyncio
import logging

from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup

from api_bot import API
from keyboards import *
from texst import *
from crud_functions import *

logging.basicConfig(level=logging.INFO)

initiate_db()  # Инициализация базы данных и создание таблицы
# add_goods()  # Добавление товаров в базу данных
all_goods = get_all_products()  # Получение всех продуктов в виде списка кортежей

api = API
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())


class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()


class RegistrationState(StatesGroup):
    username = State()
    email = State()
    age = State()
    balance = State()


@dp.message_handler(text=['Регистрация'])
async def sing_up(message):
    await message.answer('Введите имя пользователя (только латинский алфавит):')
    await RegistrationState.username.set()


@dp.message_handler(state=RegistrationState.username)
async def set_username(message, state):
    username = message.text
    if is_included(username):
        await message.answer('Пользователь существует, введите другое имя')
        return RegistrationState.username
    else:
        if username.isalpha() and username.isascii():  # Проверяем, что введен только латиница
            await state.update_data(username=username)
            await message.answer('Введите Ваш e-mail:')
            await RegistrationState.email.set()
        else:
            await message.answer('Имя пользователя должно содержать только латинские буквы. Попробуйте снова.')
            return RegistrationState.username


@dp.message_handler(state=RegistrationState.email)
async def set_email(message, state):
    email = message.text
    await state.update_data(email=email)
    await message.answer('Введите свой возраст:')
    await RegistrationState.age.set()


@dp.message_handler(state=RegistrationState.age)
async def set_age_for_registration(message, state):
    if message.text.isdigit():
        age = int(message.text)
        await state.update_data(age=age)
        # Баланс устанавливаем по умолчанию 1000
        await state.update_data(balance=1000)
        data = await state.get_data()
        # записываем в базу данных информацию о пользователе
        add_user(data['username'], data['email'], data['age'])
        await state.finish()
        await message.answer('Регистрация успешно завершена!')
    else:
        await message.answer('Возраст должен быть числом. Попробуйте снова.')
        return RegistrationState.age


@dp.message_handler(commands=['start'])
async def start(message):
    await message.answer('Привет! Я бот помогающий твоему здоровью.', reply_markup=start_kb)


@dp.message_handler(text=['Информация'])
async def info(message):
    await message.answer('Поздравляю, Вы в находитесь в программе позволяющей Вам рассчитать '
                         'необходимое для Вас количество калорий.\nНажмите кнопу "Рассчитать"')


@dp.message_handler(text=['Рассчитать'])
async def main_menu(message):
    await message.answer('Выберите опцию: ', reply_markup=catalog_kb)


@dp.callback_query_handler(text='formulas')
async def get_formulas(call):
    await call.message.answer('10 х вес (кг) + 6,25 x рост (см) – 5 х возраст (г) + 5')
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
        await message.answer('Возраст должен быть целым числом.\nПопробуйте ещё раз: ')


@dp.message_handler(state=UserState.growth)
async def set_weight(message, state):
    if message.text.isdigit():
        await state.update_data(weight=message.text)
        await message.answer('Введите свой вес: ')
        await UserState.weight.set()
    else:
        await message.answer('Рост должен быть целым числом.\nПопробуйте ещё раз: ')


@dp.message_handler(state=UserState.weight)
async def send_calories(message, state):
    if message.text.isdigit():
        await state.update_data(growth=message.text)
    else:
        await message.answer('Вес должен быть целым числом.\nПопробуйте ещё раз: ')

    data = await state.get_data()
    age = int(data['age'])
    growth = int(data['growth'])
    weight = int(data['weight'])

    # упрощенна формула Миффлина для мужчин
    calories = (10 * weight) + (6.25 * growth) - (5 * age) + 5
    await message.answer(f'Ваша норма калорий: {calories} ккал')
    await state.finish()


@dp.message_handler(text=['Купить'])
async def get_buying_list(message):
    for i in range(4):
        await message.answer(f'Название: {all_goods[i][1]} | Описание: {all_goods[i][2]} | Цена: {all_goods[i][3]}')
        with open(f'{i + 1}.png', 'rb') as img:
            await message.answer_photo(img)

    await message.answer('Выберите продукт для покупки:', reply_markup=product_kb)


@dp.callback_query_handler(text='product_buying')
async def send_confirm_message(call):
    await call.message.answer('Вы успешно приобрели продукт!')
    await call.answer()


@dp.message_handler()
async def all_massages(message):
    await message.answer('Введите команду /start, чтобы начать общение.')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
