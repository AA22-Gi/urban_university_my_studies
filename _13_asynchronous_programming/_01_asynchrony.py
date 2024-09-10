import asyncio
from asyncio import sleep


async def start_strongman(name, power):
    print(f'Силач {name} начал соревнования.')
    for ball_number in range(1, 6):
        print(f'Силач {name} поднял {ball_number}')
        sleep(power)
    print(f'Силач {name} закончил соревнования.')


async def start_tournament():
    task_1 = start_strongman('Pasha', 3)
    task_2 = start_strongman('Denis', 4)
    task_2 = start_strongman('Apollon', 5)

