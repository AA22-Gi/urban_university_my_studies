from fastapi import FastAPI

app = FastAPI()
# строка для запуска через терминал
command_to_run = 'python -m uvicorn _16_libraries_for_working_with_resources._01_fastapi_basics_and_routing:app'


@app.get('/user/admin')
async def admin() -> str:
    return 'Вы вошли как администратор'


@app.get('/user/{user_id}')
async def _user_id(user_id: str) -> str:
    return f'Вы вошли как пользователь № {user_id}'


@app.get('/user}')
async def user_info(username: str = 'Alex', age: int = 33) -> str:
    return f'Информация о пользователе. Имя: {username}, Возраст: {age}'


@app.get('/')
async def main() -> str:
    return 'Главная страница'
