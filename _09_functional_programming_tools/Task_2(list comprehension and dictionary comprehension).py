"""
Задача
Даны несколько списков, состоящих из строк
first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']
second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']

    1.В переменную first_result запишите список созданный при помощи сборки состоящий из длин строк списка
    first_strings, при условии, что длина строк не менее 5 символов.
    2.В переменную second_result запишите список созданный при помощи сборки состоящий из пар слов(кортежей)
    одинаковой длины. Каждое слово из списка first_strings должно сравниваться с каждым из second_strings. (два цикла)
    3.В переменную third_result запишите словарь созданный при помощи сборки, где парой ключ-значение
    будет строка-длина строки. Значения строк будут перебираться из объединённых вместе списков first_strings
    и second_strings. Условие записи пары в словарь - чётная длина строки.

Примечания:
Помните, когда вы используете 2 цикла for внутри сборки, первый цикл - внешний, второй - внутренний.
"""
first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']
second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']

first_result = [len(word) for word in first_strings if len(word) > 4]
second_result = [(word1, word2) for word1 in first_strings for word2 in second_strings if len(word1) == len(word2)]
third_result = {word: len(word) for word in first_strings + second_strings if len(word) % 2 == 0}

if __name__ == '__main__':
    assert first_result == [10, 8, 8]
    assert second_result == [
        ('Elon', 'Task'),
        ('Elon', 'Java'),
        ('Musk', 'Task'),
        ('Musk', 'Java'),
        ('Monitors', 'Computer'),
        ('Variable', 'Computer')
    ]
    assert third_result == {
        'Elon': 4,
        'Musk': 4,
        'Programmer': 10,
        'Monitors': 8,
        'Variable': 8,
        'Task': 4,
        'Java': 4,
        'Computer': 8
    }
