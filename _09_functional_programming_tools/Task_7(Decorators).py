"""
Напишите 2 функции:
    1.Функция, которая складывает 3 числа (sum_three)
    2.Функция декоратор (is_prime), которая распечатывает "Простое",
    если результат 1ой функции будет простым числом и "Составное" в противном случае.

Примечания:
1.Не забудьте написать внутреннюю функцию wrapper в is_prime
2.Функция is_prime должна возвращать wrapper
3.@is_prime - декоратор для функции sum_three
"""


def is_prime(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        count = True
        for i in range(2, result):
            if result % i == 0:
                count = False
                break
        print('Простое' if count else 'Составное')
        return result

    return wrapper


@is_prime
def sum_three(a: int, b: int, c: int) -> int:
    "Возвращает сумму 3-х чисел"
    return a + b + c


if __name__ == '__main__':
    result = sum_three(2, 3, 6)
    print(result)
    result = sum_three(3, 3, 6)
    print(result)
