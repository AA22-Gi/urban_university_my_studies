"""
Библиотека requests, это библиотека для отправки HTTP-запросов на сайт.
Она упрощает процесс получения данных с веб-сайтов.

Основные методы:
requests.get(url): отправляет GET-запрос на указанный URL.
response.status_code: возвращает статус код ответа.
response.json(): возвращает ответ в формате JSON (если поддерживается).

"""
import requests
from pprint import pprint

url = 'https://api.github.com'
response = requests.get(url)
status_code = response.status_code

if __name__ == '__main__':
    if response.status_code == 200:
        data = response.json()
        pprint(data)
    else:
        print(f'Ошибка: статус код {status_code}')
