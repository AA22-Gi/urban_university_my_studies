"""
Задача "Всё не так уж просто":
Дан список чисел numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
Используя этот список составьте второй список primes содержащий только простые числа.
А так же третий список not_primes, содержащий все не простые числа.
Выведите списки primes и not_primes на экран(в консоль).
Пункты задачи:
 1. Создайте пустые списки primes и not_primes.
 2. При помощи цикла for переберите список numbers.
 3. Напишите ещё один цикл for (вложенный), где будут подбираться делители для числа из 1ого цикла.
 4. Отметить простоту числа можно переменной is_prime, записав в неё значение True перед проверкой.
 5. В процессе проверки на простоту записывайте числа из списка numbers в списки primes и not_primes
    в зависимости от значения переменной is_prime после проверки (True - в prime, False - в not_prime).
 6. Выведите списки primes и not_primes на экран(в консоль).
"""

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []

is_prime = True
for i in numbers:
    for e in range(2, i):
        if i % e == 0:
            is_prime = False
            not_primes.append(i)
            break
    if is_prime and i != 1:
        primes.append(i)
    is_prime = True

print(f'Primes: {primes}')
print(f'Not primes: {not_primes}')

# Альтерантивное решение
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
# primes = []
# not_primes = []
#
# for i in numbers:
#     for e in range(2, i):
#         if i % e == 0:
#             not_primes.append(i)
#     if i != 1 and i not in not_primes:
#         primes.append(i)
#
# print(f'Primes: {list(set(primes))}')
# print(f'Not primes: {list(set(not_primes))}')
