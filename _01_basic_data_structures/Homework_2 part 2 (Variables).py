# Задача «Сдача всем».
# Описание: Кроме ягод в магазине продаётся множество других товаров,
# которые продаются на развес. Давайте автоматизируем расчёт сдачи и для них!
# Формат ввода
# Три натуральных числа: цена товара; вес товара; количество денег у покупателя.
# Формат вывода
# Одно целое число — сдача, которую требуется отдать покупателю
price = float(input())
weight = float(input())
money_buyer = float(input())
print(round(money_buyer - weight * price, 2))

# Задача «Работаем с выводом данных».
# Описание: Сдачу посчитать, конечно, все могут, но красивый чек напечатать — не так просто.
# Формат ввода: название товара; цена товара; вес товара; количество денег у пользователя.
# Формат вывода: Чек <название товара> - <вес>кг - <цена>руб/кг
# Итого: <итоговая стоимость>руб Внесено: <количество денег от пользователя>руб Сдача: <сдача>руб
name_product = input()
price = float(input())
weight = float(input())
money_buyer = float(input())

print(f'{name_product} - {weight} кг - {price} руб/кг')
total_cost = round(weight * price, 2)
print(f'Итого: {total_cost} руб')
print(f'Внесено: {money_buyer} руб')
print(f'Сдача: {money_buyer - total_cost} руб')

# Задача «Самая простая задача на свете».
# Описание: Давай сделаем что-то действительно интересное.
# Формат ввода: Одно натуральное число
# Формат вывода: N строк с фразой: "Купи конструктор!"
num = int(input())
s = '"Купи конструктор"!'
print(f'Обожаю писать {s}\n' * num)
