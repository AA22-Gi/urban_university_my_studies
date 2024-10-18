"""
Создайте новый проект в PyCharm
Запустите созданный проект

Ваша задача:
    1. Создайте новый класс House
    2. Создайте инициализатор для класса House, который будет задавать атрибут этажности self.numberOfFloors = 0
    3. Создайте метод setNewNumberOfFloors(floors), который будет изменять атрибут numberOfFloors на параметр floors
    и выводить в консоль numberOfFloors
    4. Полученный код напишите в ответ к домашнему заданию
"""


class House:
    def __init__(self, number_of_floors=0):
        self.numberOfFloors = number_of_floors

    def setNewNumberOfFloors(self, floors):
        self.numberOfFloors = floors
        print(self.numberOfFloors)


if __name__ == '__main__':
    h1 = House()
    assert h1.__dict__ == {'numberOfFloors': 0}
    h1.setNewNumberOfFloors(12)
    assert h1.__dict__ == {'numberOfFloors': 12}
