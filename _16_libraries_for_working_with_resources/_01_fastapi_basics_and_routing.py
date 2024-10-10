from fastapi import FastAPI

app = FastAPI()
# строка для запуска через терминал
command_to_run = 'python -m uvicorn _16_libraries_for_working_with_resources._01_fastapi_basics_and_routing:app'


@app.get('/')
async def main() -> str:
    return 'Главная страница'
