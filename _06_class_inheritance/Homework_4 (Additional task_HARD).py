"""
Задание "Они все так похожи":
2D? 3D? Даже 4D?.... Настолько глубоко мы заходить конечно же не будем, 4D подождёт,
но вот с двумерными и трёхмерными фигурами можем поэкспериментировать.
Вы когда-нибудь задумывались как устроены графические библиотеки для языков программирования?
Безусловно, там выполняются огромные расчёты при помощи вашей видеокарты, но...
Что лежит в основе удобного использования таких объектов?

По названию задачи можно понять, что все геометрические фигуры обладают схожими свойствами, такими как:
длины сторон, цвет и др.

Давайте попробуем реализовать простейшие классы для некоторых таких фигур и при этом применить наследование
(в будущем, изучая сторонние библиотеки, вы будете замечать схожие классы, уже написанные кем-то ранее):

Общее ТЗ:
Реализовать классы Figure(родительский), Circle, Triangle и Cube,
объекты которых будут обладать методами изменения размеров, цвета и т.д.
Многие атрибуты и методы должны быть инкапсулированны и для них должны быть написаны интерфейсы взаимодействия
(методы) - геттеры и сеттеры.

Подробное ТЗ:

Атрибуты класса Figure: sides_count = 0
Каждый объект класса Figure должен обладать следующими атрибутами:
    - Атрибуты(инкапсулированные): __sides(список сторон (целые числа)), __color(список цветов в формате RGB)
    - Атрибуты(публичные): filled(закрашенный, bool)
И методами:
    - Метод get_color, возвращает список RGB цветов.
    - Метод __is_valid_color - служебный, принимает параметры r, g, b,
    который проверяет корректность переданных значений перед установкой нового цвета.
    Корректным цвет: все значения r, g и b - целые числа в диапазоне от 0 до 255 (включительно).
    - Метод set_color принимает параметры r, g, b - числа и изменяет атрибут __color на соответствующие значения,
    предварительно проверив их на корректность. Если введены некорректные данные, то цвет остаётся прежним.
    - Метод __is_valid_sides - служебный, принимает неограниченное кол-во сторон, возвращает True если все стороны
    целые положительные числа и кол-во новых сторон совпадает с текущим, False - во всех остальных случаях.
    - Метод get_sides должен возвращать значение я атрибута __sides.
    - Метод __len__ должен возвращать периметр фигуры.
    - Метод set_sides(self, *new_sides) должен принимать новые стороны, если их количество не равно sides_count,
    то не изменять, в противном случае - менять.

Атрибуты класса Circle: sides_count = 1
Каждый объект класса Circle должен обладать следующими атрибутами и методами:
    - Все атрибуты и методы класса Figure
    - Атрибут __radius, рассчитать исходя из длины окружности (одной единственной стороны).
    - Метод get_square возвращает площадь круга (можно рассчитать как через длину, так и через радиус).

Атрибуты класса Triangle: sides_count = 3
Каждый объект класса Triangle должен обладать следующими атрибутами и методами:
    - Все атрибуты и методы класса Figure
    - Атрибут __height, высота треугольника (можно рассчитать зная все стороны треугольника)
    - Метод get_square возвращает площадь треугольника.
Атрибуты класса Cube: sides_count = 12
Каждый объект класса Cube должен обладать следующими атрибутами и методами:
    - Все атрибуты и методы класса Figure.
    - Переопределить __sides сделав список из 12 одинаковы сторон (передаётся 1 сторона)
    - Метод get_volume, возвращает объём куба.

ВАЖНО!
При создании объектов делайте проверку на количество переданных сторон, если сторон не ровно sides_count,
то создать массив с единичными сторонами и в том кол-ве, которое требует фигура.
Пример 1: Circle((200, 200, 100), 10, 15, 6), т.к. сторона у круга всего 1, то его стороны будут - [1]
Пример 2: Triangle((200, 200, 100), 10, 6), т.к. сторон у треугольника 3, то его стороны будут - [1, 1, 1]
Пример 3: Cube((200, 200, 100), 9), т.к. сторон(рёбер) у куба - 12, то его стороны будут - [9, 9, 9, ....., 9] (12)
Пример 4: Cube((200, 200, 100), 9, 12), т.к. сторон(рёбер) у куба - 12, то его стороны будут - [1, 1, 1, ....., 1]

Код для проверки:
circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15) # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
print(cube1.get_sides())
circle1.set_sides(15) # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())


Выходные данные (консоль):
[55, 66, 77]
[222, 35, 130]
[6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6]
[15]
15
216

Примечания (рекомендации):
Рекомендуется сделать дополнительные (свои проверки) работы методов объектов каждого класса.
Делайте каждый класс и метод последовательно и проверяйте работу каждой части отдельно.
Для проверки принадлежности к типу рекомендуется использовать функцию isinstance.
Помните, служебные инкапсулированные методы можно и нужно использовать только внутри текущего класса.
Вам не запрещается вводить дополнительные атрибуты и методы, творите, но не переборщите!
"""
from math import pi, sqrt


class Figure:
    sides_count = 0

    def __init__(self, color: tuple = (0, 0, 0), *sides):
        self.filled = False
        self.__color = list(color)
        if len(sides) == self.sides_count:
            self.__sides = list(sides)
        else:
            self.__sides = [sides[0]] * self.sides_count

    def get_color(self):
        return self.__color

    def __is_valid_color(self, r, g, b):
        for color in r, g, b:
            if not (isinstance(color, int) and 0 <= color < 256):
                return False
        return True

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]

    def get_sides(self):
        return self.__sides

    def __is_valid_sides(self, *sides):
        sides = list(*sides)
        if len(sides) == len(self.__sides):
            for side in sides:
                if not isinstance(side, int) or side <= 0:
                    return False
            return True

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(new_sides):
            self.__sides = list(new_sides)

    def __len__(self):
        return sum(self.__sides)


class Circle(Figure):
    sides_count = 1

    def __init__(self, color: tuple = (0, 0, 0), *sides):
        super().__init__(color, *sides)
        self.__radius = self.__len__() / (2 * pi)

    def get_radius(self):
        return self.__radius

    def get_diameter(self):
        return self.__radius * 2

    def get_square(self):
        return pi * self.__radius ** 2


class Triangle(Figure):
    sides_count = 3

    def __init__(self, color: tuple = (0, 0, 0), *sides):
        super().__init__(color, *sides)
        self.__height = self.__calculate_height()

    def __calculate_height(self):
        square = self.get_square()
        return square * 2 / self.get_sides()[0]

    def get_square(self):
        semiperimeter = sum(self.get_sides()) / 2  # находим полупериметр треугольника
        square = sqrt(semiperimeter *  # находим площадь треугольника по формуле Герона
                      (semiperimeter - self.get_sides()[0]) *
                      (semiperimeter - self.get_sides()[1]) *
                      (semiperimeter - self.get_sides()[2]))
        return square


class Cube(Figure):
    sides_count = 12

    def __init__(self, color: tuple = (0, 0, 0), *sides):
        super().__init__(color, *sides)
        if len(sides) == 1:
            self.__sides = [sides[0]] * self.sides_count

    def get_volume(self):
        return self.__sides[0] ** 3


if __name__ == '__main__':
    # Figure
    figure = Figure((200, 200, 100), 10)  # создаем экземпляр Figure
    assert figure.filled == False
    assert figure.sides_count == 0
    assert figure.get_color() == [200, 200, 100]
    assert figure.get_sides() == []

    figure.set_color(15, 36, 3)  # меняем цвет на новый
    assert figure.get_color() == [15, 36, 3]
    figure.set_color(15, 36, -23)  # цвет не поменяется, поскольку одно из значений не валидно
    assert figure.get_color() == [15, 36, 3]

    figure.set_sides(35)  # изменяем длину стороны
    assert figure.get_sides() == []
    figure.set_sides(0)
    assert figure.get_sides() == []
    figure.set_sides(-5)
    assert figure.get_sides() == []
    figure.set_sides(-5, 4)
    assert figure.get_sides() == []
    figure.set_sides('a')
    assert figure.get_sides() == []
    assert figure.__len__() == 0

    # круг
    circle1 = Circle((200, 200, 100), 10)  # (Цвет, стороны)
    assert circle1.get_sides() == [10]  # длинна окружности
    assert circle1.get_square() == 7.9577471545947684  # площадь
    assert circle1.get_radius() == 1.5915494309189535  # радиус
    assert circle1.get_diameter() == 3.183098861837907  # диаметр
    assert circle1.get_color() == [200, 200, 100]  # цвета

    circle1.set_color(15, 36, 3)  # меняем цвет на новый
    assert circle1.get_color() == [15, 36, 3]
    circle1.set_color(-15, 36, -23)  # цвет не поменяется, поскольку одно из значений не валидно
    assert circle1.get_color() == [15, 36, 3]
    circle1.set_color(1, 2, 300.0)
    assert circle1.get_color() == [15, 36, 3]

    circle1.set_sides(33)  # изменяем длину окружности круга
    assert circle1.get_sides() == [33]
    circle1.set_sides(0)
    assert circle1.get_sides() == [33]
    circle1.set_sides(-5)
    assert circle1.get_sides() == [33]
    circle1.set_sides(-5, 4)
    assert circle1.get_sides() == [33]
    circle1.set_sides('a')
    assert circle1.get_sides() == [33]
    assert circle1.__len__() == 33

    # Треугольник
    triangle1 = Triangle((200, 200, 100), 10)  # (Цвет, стороны)
    # assert triangle1.get_sides() == [10, 10, 10]  # длинна окружности
    triangle1 = Triangle((200, 200, 100), 8, -7, 9)  # (Цвет, стороны)
    assert triangle1.get_sides() == [8, -7, 9]
    assert triangle1.get_square() == 26.832815729997478  # площадь треугольника
    assert triangle1.get_color() == [200, 200, 100]
    triangle1.set_color(23, 34, 23)  # меняем цвет
    assert triangle1.get_color() == [23, 34, 23]

    # Куб
    cube1 = Cube((222, 35, 130), 6)
    assert cube1.get_sides() == [6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6]

    # Проверка на изменение цветов:
    cube1.set_color(55, 66, 77)  # Изменится
    assert cube1.get_color() == [55, 66, 77]
    cube1.set_color(300, 70, 15)  # Не изменится
    assert cube1.get_color() == [55, 66, 77]
    # Проверка на изменение сторон:
    cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
    assert cube1.get_sides() == [6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6]
    assert cube1.get_volume() == 216  # объём куба

    print('Good 😍')
