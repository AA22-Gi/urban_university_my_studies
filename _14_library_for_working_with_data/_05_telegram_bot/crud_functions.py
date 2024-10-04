import sqlite3


def initiate_db():
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()

    # создание таблицы Goods
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Goods (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        description TEXT,
        price INTEGER NOT NULL
    )
    ''')

    # создание таблицы Users
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Users (
        id INTEGER PRIMARY KEY,
        username TEXT NOT NULL,
        email TEXT NOT NULL,
        age INTEGER NOT NULL,
        balance INTEGER NOT NULL DEFAULT 1000
    )
    ''')

    connection.commit()
    connection.close()


def get_all_products() -> list:
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()

    cursor.execute('SELECT * FROM Goods')
    products = cursor.fetchall()

    connection.close()
    return products


def add_goods():
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()
    for i in range(1, 5):
        cursor.execute('INSERT INTO Goods(title, description, price) VALUES(?, ?, ?)',
                       (f'Product {i}', f'Описание {i}', f'{i * 100}'))

    connection.commit()
    connection.close()

def add_user(username, email, age):
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()

    cursor.execute('''
        INSERT INTO Users (username, email, age)
        VALUES (?, ?, ?)
    ''', (username, email, age))

    connection.commit()
    connection.close()
