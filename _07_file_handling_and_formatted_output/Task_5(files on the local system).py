"""
Создайте новый проект или продолжите работу в текущем проекте.
    1.Используйте os.walk для обхода каталога, путь к которому указывает переменная directory
    2.Примените os.path.join для формирования полного пути к файлам.
    3.Используйте os.path.getmtime и модуль time для получения и отображения времени последнего изменения файла.
    4.Используйте os.path.getsize для получения размера файла.
    5.Используйте os.path.dirname для получения родительской директории файла.

Комментарии к заданию:
Ключевая идея – использование вложенного for
for root, dirs, files in os.walk(directory):
  for file in files:
    filepath = ?
    filetime = ?
    formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
    filesize = ?
    parent_dir = ?
    print(f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {filesize} байт,
    Время изменения: {formatted_time}, Родительская директория: {parent_dir}')
"""
import os
import time

directory = '.'
for root, dirs, files in os.walk(directory):
    for file in files:
        # Путь к файлу
        filepath = os.path.join(root, file)

        # Время изменения файла
        filetime = os.path.getmtime(filepath)
        formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))

        # Размер файла
        filesize = os.path.getsize(filepath)

        # Родительская директории файла
        parent_dir = os.path.dirname(filepath)

        # Вывод информации о файле
        print(f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {filesize} байт, '
              f'Время изменения: {formatted_time}, Родительская директория: {parent_dir}')