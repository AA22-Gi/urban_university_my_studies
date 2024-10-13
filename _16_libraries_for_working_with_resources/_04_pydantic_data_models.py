from fastapi import FastAPI, Path
from typing import Annotated
from pydantic import BaseModel

app = FastAPI()
users = []


class User(BaseModel):
    id: int
    username: str
    age: int


@app.get('/users')
async def get_all_users() -> dict:
    return users


@app.post('/user/{username}/{age}')
async def create_user(username: Annotated[str, Path(min_length=4, max_length=20,
                                                    description='Enter username',
                                                    example='UrbanUser')],
                      age: Annotated[int, Path(ge=12, le=70,
                                               description='Enter age',
                                               example='24')]) -> str:
    user_id = str(max(map(int, users.keys())) + 1)
    users[user_id] = f'Имя: {username}, возраст: {age}'
    return f'User {user_id} is registered'


@app.put('/user/{user_id}/{username}/{age}')
async def update_user_value(user_id: str,
                            username: Annotated[str, Path(min_length=4, max_length=20,
                                                          description='Enter username',
                                                          example='UrbanUser')],
                            age: Annotated[int, Path(ge=12, le=70,
                                                     description='Enter age',
                                                     example='24')]) -> str:
    if user_id in users:
        users[user_id] = f'Имя: {username}, возраст: {age}'
        return f'The user {user_id} is registered'


@app.delete('/user/{user_id}')
async def delete_user(user_id: str) -> str:
    if user_id in users:
        username = users[user_id].split()[1][:-1]
        del users[user_id]
    return f'Пользователь {username} удален'


command_to_run = 'python -m uvicorn _16_libraries_for_working_with_resources._03_CRUD_requests:app --reload'
