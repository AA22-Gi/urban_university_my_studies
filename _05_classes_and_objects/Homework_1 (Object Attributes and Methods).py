"""
Задача "Developer - не только разработчик":
Реализуйте класс House, объекты которого будут создаваться следующим образом:
House('ЖК Эльбрус', 30)
Объект этого класса должен обладать следующими атрибутами:
self.name - имя, self.number_of_floors - кол-во этажей
Также должен обладать методом go_to(new_floor), где new_floor - номер этажа(int), на который нужно приехать.
Метод go_to выводит на экран(в консоль) значения от 1 до new_floor(включительно).
Если же new_floor больше чем self.number_of_floors или меньше 1, то вывести строку "Такого этажа не существует".

Пункты задачи:
1. Создайте класс House.
2. Внутри класса House определите метод __init__, в который передадите название и кол-во этажей.
3. Внутри метода __init__ создайте атрибуты объекта self.name и self.number_of_floors, присвойте им переданные значения.
4. Создайте метод go_to с параметром new_floor и напишите логику внутри него на основе описания задачи.
5. Создайте объект класса House с произвольным названием и количеством этажей.
6. Вызовите метод go_to у этого объекта с произвольным числом.
"""


class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        if self.number_of_floors < 1 or self.number_of_floors < new_floor:
            print(f'Такого этажа не существует')
        else:
            for floor in range(1, new_floor + 1):
                print(floor)


if __name__ == '__main__':
    h1 = House('ЖК Горский', 18)
    h2 = House('Домик в деревне', 2)
    h1.go_to(5)
    h2.go_to(10)


