from fastapi import FastAPI, Path, HTTPException, Request
from fastapi.responses import HTMLResponse
from typing import Annotated
from pydantic import BaseModel
import uvicorn
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory='templates')
users = []


class User(BaseModel):
    id: int = None
    username: str
    age: int


@app.get('/')
async def get_users(request: Request) -> HTMLResponse:
    return templates.TemplateResponse('users.html', {'request': request, 'list_users': users})


@app.get('/users/{user_id}')
async def get_all_users(request: Request,user_id: int):
    user = None
    for user_ in users:
        if user_.id == user_id:
            user = user_
            break
    return templates.TemplateResponse('users.html', {'request': request, 'user': user})


@app.post('/user/{username}/{age}')
async def create_user(
        username: Annotated[str, Path(
            min_length=4,
            max_length=20,
            description='Enter username',
            example='UrbanUser'
        )],
        age: Annotated[int, Path(
            ge=12,
            le=70,
            description='Enter age',
            example='24'
        )]) -> User:
    user_id = users[-1].id + 1 if users else 1
    new_user = User(id=user_id, username=username, age=age)
    users.append(new_user)
    return new_user


@app.put('/user/{user_id}/{username}/{age}')
async def update_user_value(
        user_id: Annotated[int, Path(
            ge=0,
            le=1000,
            description='Enter user_id',
            example='2'
        )],
        username: Annotated[str, Path(
            min_length=4,
            max_length=20,
            description='Enter username',
            example='UrbanUser'
        )],
        age: Annotated[int, Path(
            ge=12,
            le=70,
            description='Enter age',
            example='24'
        )]) -> User:
    for user in users:
        if user.id == user_id:
            user.username = username
            user.age = age
            return user

    raise HTTPException(status_code=404, detail='User was not found')


@app.delete('/user/{user_id}')
async def delete_user(
        user_id: Annotated[int, Path(
            ge=0,
            le=1000,
            description='Enter user_id',
            example='2'
        )]) -> User:
    for user in users:
        if user.id == user_id:
            users.remove(user)
            return user

    raise HTTPException(status_code=404, detail='User was not found')


if __name__ == '__main__':
    uvicorn.run(app, host="127.0.0.1", port=8000)
