"""
Задача "Мифическое наследование"
Необходимо написать 3 класса:
    1)Horse - класс описывающий лошадь. Объект этого класса обладает следующими атрибутами:
        1.x_distance = 0 - пройденный путь.
        2.sound = 'Frrr' - звук, который издаёт лошадь.
    И методами:
        3.run(self, dx), где dx - изменение дистанции, увеличивает x_distance на dx.

    2)Eagle - класс описывающий орла. Объект этого класса обладает следующими атрибутами:
        1.y_distance = 0 - высота полёта
        2.sound = 'I train, eat, sleep, and repeat' - звук, который издаёт орёл (отсылка)
    И методами:
        3.fly(self, dy) где dy - изменение дистанции, увеличивает y_distance на dy.

    3)Pegasus - класс описывающий пегаса. Наследуется от Horse и Eagle в том же порядке.
    Объект такого класса должен обладать атрибутами классов родителей в порядке наследования.
    Также обладает методами:
        1.move(self, dx, dy) - где dx и dy изменения дистанции.
        В этом методе должны запускаться наследованные методы run и fly соответственно.
        2.get_pos(self) возвращает текущее положение пегаса в виде кортежа - (x_distance, y_distance) в том же порядке.
        3.voice - который печатает значение унаследованного атрибута sound.

Пункты задачи:
1. Создайте классы родители: Horse и Eagle с методами из описания.
2. Создайте класс наследник Pegasus с методами из описания.
3. Создайте объект класса Pegasus и вызовите каждый из ранее перечисленных методов, проверив их работу.

Примечания:
Будьте внимательней, когда вызываете методы классов родителей в классе наследнике при множественном наследовании:
при обращении через super() методы будут искаться сначала в первом, потом во втором и т.д. классах по mro().
Заметьте, что Pegasus издаёт звук "I train, eat, sleep, and repeat",
т.к. по порядку сначала идёт наследование от Horse, а после от Eagle.
"""


class Horse:
    def __init__(self, x_distance=0, sound='Frrr'):
        self.x_distance = x_distance
        self.sound = sound
        super().__init__()

    def run(self, dx: int):
        self.x_distance += dx


class Eagle:
    def __init__(self, y_distance=0, sound='I train, eat, sleep, and repeat'):
        self.y_distance = y_distance
        self.sound = sound

    def fly(self, dy):
        self.y_distance += dy


class Pegasus(Horse, Eagle):
    def move(self, dx, dy):
        self.run(dx)
        self.fly(dy)

    def get_pos(self):
        return (self.x_distance, self.y_distance)

    def voice(self):
        print(self.sound)


if __name__ == '__main__':
    p1 = Pegasus()

    assert p1.get_pos() == (0, 0)
    print(p1.get_pos())
    p1.move(10, 15)
    assert p1.get_pos() == (10, 15)
    print(p1.get_pos())
    p1.move(-5, 20)
    assert p1.get_pos() == (5, 35)
    print(p1.get_pos())

    p1.voice()
