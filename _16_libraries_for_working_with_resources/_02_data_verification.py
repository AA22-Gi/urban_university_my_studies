from fastapi import FastAPI, Path
from typing import Annotated

app = FastAPI()


@app.get('/')
async def main() -> str:
    return 'Главная страница'


@app.get('/user/admin')
async def admin() -> str:
    return 'Вы вошли как администратор'


@app.get('/user/{user_id}')
async def user_id_(user_id: int = Path(ge=1, le=100, description='Enter User ID', example='1')) -> str:
    return f'Вы вошли как пользователь № {user_id}'


@app.get('/user')
async def user_info(username: str = 'Alex', age: int = 38) -> str:
    return f'Информация о пользователе. Имя: {username}, Возраст: {age}'


# строка для запуска через терминал
command_to_run = 'python -m uvicorn _16_libraries_for_working_with_resources._02_data_verification:app --reload'
