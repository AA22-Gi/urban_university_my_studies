"""
Задача "Функциональное разнообразие"

1) Lambda-функция.
    Даны 2 строки:
        first = 'Мама мыла раму'
        second = 'Рамена мало было'
    Необходимо составить lambda-функцию для следующего выражения - list(map(?, first, second)).
    Здесь ? - место написания lambda-функции.

    Результатом должен быть список совпадения букв в той же позиции:
        [False, True, True, False, False, False, False, False, True, False, False, False, False, False]
    Где True - совпало, False - не совпало.

2) Замыкание.

    1.Напишите функцию get_advanced_writer(file_name), принимающую название файла для записи.
    2.Внутри этой функции, напишите ещё одну - write_everything(*data_set),
    где *data_set - параметр принимающий неограниченное количество данных любого типа.
    3.Логика write_everything заключается в добавлении в файл file_name всех данных из data_set в том же виде.
    4.Функция get_advanced_writer возвращает функцию write_everything.

    Данный код:
        write = get_advanced_writer('example.txt')
        write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])

3) Метод __call__.

    Создайте класс MysticBall, объекты которого обладают атрибутом words хранящий коллекцию строк.
    В этом классе также определите метод __call__
    который будет случайным образом выбирать слово из words и возвращать его.
    Для случайного выбора с одинаковой вероятностью для каждого данного в коллекции
    можете использовать функцию choice из модуля random.

    Ваш код (количество слов для случайного выбора может быть другое):
        from random import choice
        # Ваш класс здесь
        first_ball = MysticBall('Да', 'Нет', 'Наверное')
        print(first_ball())
        print(first_ball())
        print(first_ball())
        Примерный результат (может отличаться из-за случайности выбора):
        Да
        Да
        Наверное
"""
from random import choice

first = 'Мама мыла раму'
second = 'Рамена мало было'
result = list(map(lambda a, b: a == b, first, second))


def get_advanced_writer(file_name: str):
    def write_everything(*data_set):
        return file_name, data_set

    return write_everything


class MysticBall:
    def __init__(self, *args):
        self.args = args

    def __call__(self):
        return choice(self.args)


if __name__ == '__main__':
    assert result == [False, True, True, False, False, False, False, False, True, False, False, False, False, False]

    write = get_advanced_writer('example.txt')
    assert write('А', 'это', 'уже', 'число', 5, 'в', 'списке'
                 == ('example.txt', ('А', 'это', 'уже', 'число', 5, 'в', 'списке')))

    first_ball = MysticBall('Да', 'Нет', 'Наверное')
    print(first_ball())
    print(first_ball())
    print(first_ball())
