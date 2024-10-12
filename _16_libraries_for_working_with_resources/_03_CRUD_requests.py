from fastapi import FastAPI, Path
from typing import Annotated

app = FastAPI()
users = {'1': 'Имя: Example, возраст: 18'}


@app.get('/users')
async def get_all_users() -> dict:
    return users


@app.post('/user/{username}/{age}')
async def create_user(username: Annotated[str, Path(min_length=4, max_length=20,
                                                    description='Enter username',
                                                    example='UrbanUser')],
                      age: Annotated[int, Path(ge=12, le=70,
                                               description='Enter age',
                                               example='24')]):
    user_id = str(max(map(int, users.keys())) + 1)
    users[user_id] = f'Имя: {username}, возраст: {age}'
    return 'User {user_id} is registered'
