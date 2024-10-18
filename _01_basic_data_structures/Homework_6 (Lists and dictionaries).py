"""
2. Работа со списками:
  - Создайте переменную my_list и присвойте ей список из нескольких элементов, например, фруктов.
  - Выведите на экран список my_list.
  - Выведите на экран первый и последний элементы списка my_list.
  - Выведите на экран подсписок my_list с третьего до пятого элементов.
  - Измените значение третьего элемента списка my_list.
  - Выведите на экран измененный список my_list.

3. Работа со словарями:
  - Создайте переменную my_dict и присвойте ей словарь с парами ключ-значение, например, переводами некоторых слов.
  - Выведите на экран словарь my_dict.
  - Выведите на экран значение для заданного ключа в my_dict.
  - Измените значение для заданного ключа или добавьте новый в my_dict.
  - Выведите на экран измененный словарь my_dict.
"""

my_list = ['apple', 'banana', 'orange', 'kiwi', 'grape']
print('List:', my_list)
print('First element:', my_list[0])
print('Last element:', my_list[-1])
print('Sublist:', my_list[2:4])
my_list[2] = 'mandarin'
print('Modified list:', my_list)
print()

my_dict = {'apple': 'яблоко',
           'banana': 'банан',
           'orange': 'апельсин',
           'kiwi': 'киви'}
print('Dictionary:', my_dict)
print('Translation:', my_dict['apple'])
my_dict['apple'] = ['яблоко', 'красное']
my_dict['grape'] = 'виноград'
print('Modified dictionary:', my_dict)
