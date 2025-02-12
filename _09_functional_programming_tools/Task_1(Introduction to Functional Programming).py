"""
Задача "Вызов разом"

Напишите функцию apply_all_func(int_list, *functions), которая принимает параметры:
    1.int_list - список из чисел (int, float)
    2.*functions - неограниченное кол-во функций (которые применимы к спискам, состоящим из чисел)

Эта функция должна:
    1.Вызвать каждую функцию к переданному списку int_list
    2.Возвращать словарь, где ключом будет название вызванной функции,
    а значением - её результат работы со списком int_list.

Пункты задачи:
    1.В функции apply_all_func создайте пустой словарь results.
    2.Переберите все функции из *functions.
    3.При переборе функций записывайте в словарь results результат работы этой функции под ключом её названия.
    4.Верните словарь results.
    5.Запустите функцию apply_all_func, передав в неё список из чисел и набор других функций.

Пример результата выполнения программы:
    В примере используются следующие функции:
    1.min - принимает список, возвращает минимальное значение из него.
    2.max - принимает список, возвращает минимальное значение из него.
    3.len - принимает список, возвращает кол-во элементов в нём.
    4.sum - принимает список, возвращает сумму его элементов.
    5.sorted - принимает список, возвращает новый отсортированный список на основе переданного34

Пример работы кода:
    print(apply_all_func([6, 20, 15, 9], max, min))
    print(apply_all_func([6, 20, 15, 9], len, sum, sorted))

Вывод на консоль:
    {'max': 20, 'min': 6} {'len': 4, 'sum': 50, 'sorted': [6, 9, 15, 20]}

Примечания:
    1.Для того, чтобы взять название функции можно обратиться к атрибуту __name__
    2.При попытке передачи, например, списка из строк, некоторые функции могут работать некорректно
    или вовсе не работать. Используйте списки чисел.
"""


def apply_all_func(int_list: list[int, float], *functions: tuple) -> dict:
    results = dict()
    for function in functions:
        results[function.__name__] = function(int_list)
    return results


if __name__ == '__main__':
    assert apply_all_func([6, 20, 15, 9], max, min) == {'max': 20, 'min': 6}
    assert (apply_all_func([6, 20, 15, 9], len, sum, sorted)
            == {'len': 4, 'sum': 50, 'sorted': [6, 9, 15, 20]})
