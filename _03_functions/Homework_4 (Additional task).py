"""
Задание "Раз, два, три, четыре, пять .... Это не всё?":
Все ученики Урбана, без исключения, очень умные ребята. Настолько умные,
что иногда по утру сами путаются в том, что намудрили вчера вечером.
Один из таких учеников уснул на клавиатуре в процессе упорной учёбы (ещё и трудолюбивые).
Тем не менее даже после сна, его код остался рабочим и выглядел следующим образом:

data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

Увидев это студент задался вопросом: "А есть ли универсальное решение для подсчёта суммы всех чисел и длин всех строк?"
Да, выглядит страшно, да и обращаться нужно к каждой внутренней структуре (списку, словарю и т.д.) по-разному.

Ученику пришлось каждый раз использовать индексацию и обращение по ключам - универсального решения
для таких структур он не нашёл.
Помогите сокурснику осуществить его задумку.

Что должно быть подсчитано:
Все числа (не важно, являются они ключами или значениям или ещё чем-то).
Все строки (не важно, являются они ключами или значениям или ещё чем-то)

Для примера, указанного выше, расчет вёлся следующим образом:
1 + 2 + 3 + len('a') + 4 + len('b') + 5 + 6 + len('cube') + 7 + .... + 35 = 99
"""


def get_sum_list(value: list) -> int:
    if not value:
        return 0
    if isinstance(value[0], int):
        return value[0] + get_sum_list(value[1:])
    if isinstance(value[0], str):
        return len(value[0]) + get_sum_list(value[1:])
    if isinstance(value[0], list):
        return get_sum_list(value[0]) + get_sum_list(value[1:])
    if isinstance(value[0], tuple):
        value[0] = list(value[0])
        return get_sum_list(value[0]) + get_sum_list(value[1:])
    if isinstance(value[0], set):
        value[0] = list(value[0])
        return get_sum_list(value[0]) + get_sum_list(value[1:])
    if isinstance(value[0], dict):
        return get_sum_dict(value[0]) + get_sum_list(value[1:])


def get_sum_dict(value: dict) -> int:
    if not value:
        return 0
    key = list(value)[0]
    key_value = value[list(value)[0]]
    value.pop(key)
    return len(key) + key_value + get_sum_dict(value)


def get_sum_values(value) -> int:
    if not value:
        return 0
    if isinstance(value, int):
        return value
    if isinstance(value, str):
        return len(value)
    if isinstance(value, list):
        return get_sum_list(value)
    if isinstance(value, tuple):
        value = list(value)
        return get_sum_list(value)
    if isinstance(value, set):
        value = list(value)
        return get_sum_list(value)
    if isinstance(value, dict):
        return get_sum_dict(value)


data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

if __name__ == '__main__':
    assert get_sum_values([]) == 0
    assert get_sum_values([1, 2, 3]) == 6
    assert get_sum_values([[1, 2, 3], [1, 2, 3]]) == 12
    assert get_sum_values([1, 2, '3']) == 4
    assert get_sum_values(('Urban2', 35)) == 41
    assert get_sum_values({'cube', 7, 'drum', 8}) == 23
    assert get_sum_values([[1, 2, 3], {'a', 4, 'b', 5}, (6, {'cube', 7, 'drum', 8})]) == 46
    assert get_sum_values([[1, 2, 3], {'a', 4, 'b', 5}, (6, {'cube', 7, 'drum', 8}, "Hello")]) == 51
    assert get_sum_values([((), [{(2, 'Urban', ('Urban2', 35))}])]) == 48
    assert get_sum_values([[1, 2, 3], {'a', 4, 'b', 5}, (6, {'cube', 7, 'drum', 8}),
                           "Hello", ((), [{(2, 'Urban', ('Urban2', 35))}])]) == 99
    assert get_sum_values([{'a': 4, 'b': 5}]) == 11
    assert get_sum_values([(6, {'cube': 7, 'drum': 8})]) == 29

    assert get_sum_values(data_structure) == 99
