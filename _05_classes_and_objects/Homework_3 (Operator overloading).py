"""
1. Создайте новый проект в PyCharm
2. Запустите созданный проект
Ваша задача:
    1. Создайте новый класс Building
    2. Создайте инициализатор для класса Building, который будет задавать целочисленный атрибут этажности
    self.numberOfFloors и строковый атрибут self.buildingType
    3. Создайте(перегрузите) __eq__, используйте атрибут numberOfFloors и buildingType для сравнения
    4. Полученный код напишите в ответ к домашнему заданию
"""


class Building:
    def __init__(self, number_of_floors=0, building_type=''):
        self.numberOfFloors = number_of_floors
        self.buildingType = building_type

    def __eq__(self, other):
        return self.numberOfFloors == other.numberOfFloors and self.buildingType == other.buildingType


if __name__ == '__main__':
    h1 = Building()
    h2 = Building()
    print(h1 == h2)
    h2.numberOfFloors = 3
    print(h1 == h2)
