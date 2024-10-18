"""
Задача
Дано 2 списка:
first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

Необходимо создать 2 генераторных сборки:
    1.В переменную first_result запишите генераторную сборку, которая высчитывает разницу длин строк из списков
    first и second, если их длины не равны. Для перебора строк попарно из двух списков используйте функцию zip.
    2.В переменную second_result запишите генераторную сборку, которая содержит результаты сравнения строк
    в одинаковых позициях из списков first и second. Составьте эту сборку НЕ используя функцию zip.
    Используйте функции range и len.
"""
first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

first_result = (abs(len(elem[0]) - len(elem[1])) for elem in zip(first, second) if len(elem[0]) != len(elem[1]))
second_result = (len(first[i]) == len(second[i]) for i in range(len(first)))

if __name__ == '__main__':
    assert list(first_result) == [1, 2]
    assert list(second_result) == [False, False, True]
