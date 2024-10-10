from fastapi import FastAPI

app = FastAPI()
# строка для запуска через терминал
command_to_run = 'python -m uvicorn _16_libraries_for_working_with_resources._01_fastapi_basics_and_routing:app'


@app.get('/user/admin')
async def admin() -> str:
    return 'Вы вошли как администратор'

@app.get('/user/{user_id}')
async def _user_id(user_id: str = 'Alex') -> str:
    return 'Вы вошли как пользователь № {user_id}'


@app.get('/')
async def main() -> str:
    return 'Главная страница'
