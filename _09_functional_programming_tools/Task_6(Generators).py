"""
Напишите функцию-генератор all_variants(text), которая принимает строку text и возвращает объект-генератор,
при каждой итерации которого будет возвращаться подпоследовательности переданной строки.

Пункты задачи:
    1.Напишите функцию-генератор all_variants(text).
    2.Опишите логику работы внутри функции all_variants.
    3.Вызовите функцию all_variants и выполните итерации.

Примечания:
    Для функции генератора используйте оператор yield.
"""


def all_variants(text: str):
    for e in range(len(text)):
        for s in range(len(text) - e):
            yield text[s:s + e + 1]


if __name__ == '__main__':
    a = all_variants("abc")
    for i in a:
        print(i)
