import inspect
from pprint import pprint


class Person:
    """Класс <Человек>, который обладает рядом атрибутов и методов"""

    def __init__(self, age=0, name=None, gender=None):
        self.head = True
        self.age = age
        self.name = name
        self.gender = gender

    def say_hello(self) -> str:
        return 'Hello!'

    def say_name(self):
        return f'меня зовут {self.name}'

    def say_age(self):
        return f'мне {self.age} лет'


def introspection_info(obj: object) -> dict:
    """Принимает объект и возвращает словарь, содержащий:
    тип объекта, его атрибуты, методы и модуль"""
    res = dict()
    res['type'] = get_type(obj)
    res['attributes'] = get_attributes(obj)
    res['methods'] = get_methods(obj)
    res['module'] = get_module(obj)
    return res


def get_type(obj: object) -> str:
    """Принимает объект и возвращает его тип"""
    type_obj = type(obj).__name__
    return type_obj


def get_methods(obj: object) -> list:
    """Принимает объект и возвращает его методы"""
    methods = [name for name, value in inspect.getmembers(obj) if callable(value)]
    return methods


def get_attributes(obj: object) -> list:
    """Принимает объект и возвращает его атрибуты"""
    attributes = []
    for name, value in inspect.getmembers(obj):
        if not callable(value) and '__' not in name:
            attributes.append(name)
    return attributes


def get_module(obj: object) -> str:
    """Принимает объект и возвращает его модуль"""
    obj_module = obj.__class__.__module__
    return obj_module


if __name__ == '__main__':
    number_info = introspection_info(42)
    pprint(number_info)

    # экземпляр класса Person
    anna = Person(name='Anna', gender='female', age=25)
    number_info = introspection_info(anna)
    pprint(number_info)
