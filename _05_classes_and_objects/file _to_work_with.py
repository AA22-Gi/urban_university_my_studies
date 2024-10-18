from pprint import pprint
import math

result = 140703993653624
print(id(result))
print(f'{result=}')
print(f'{result:b}')
print(f'{result:.3f}')
print(f'{result:09}')

hi = 'Привет'
name = 'Alex'
c = f'{hi}, {name}'
print(c)

matrix = [list(range(i, i + 3)) for i in range(3)]
f = list(range(1, 4))
print(f)
pprint(matrix, width=20)

number = 4.44
print(math.floor(number))

if __name__ == '__main__':
    pass


def get_number_explanation(num: int):
    match num:
        case 666:
            return 'devil number'
        case 42:
            return 'answer for everything'
        case 7:
            return 'prime number'
        case _:
            return 'just a number'


print(type(get_number_explanation(42)))




