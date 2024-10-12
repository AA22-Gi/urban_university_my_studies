from fastapi import FastAPI, Path

app = FastAPI()
users = {'1': 'Имя: Example, возраст: 18'}


@app.get('/users')
async def get_all_users() -> dict:
    return users


@app.post('/user/{username}/{age}')
async def create_user(username: str, age: int):
    user_id = str(max(map(int, users.keys())) + 1)
    users[user_id] = f'Имя: {username}, возраст: {age}'
    return 'User {user_id} is registered'
