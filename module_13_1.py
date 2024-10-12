import time
import asyncio


def greeting():
    print('\033[30m\033[47mДомашнее задание по теме "Асинхронность на практике"\033[0m')
    print('\033[30m\033[47mЦель: приобрести навык использования асинхронного запуска функций на практике\033[0m')
    print('\033[30m\033[47mЗадача "Асинхронные силачи":\033[0m')
    print('\033[30m\033[47mСтудент Крылов Эдуард Васильевич\033[0m')
    print()


def farewell():
    print()
    print('\033[30m\033[47mДата работы над заданием: 12.10.2024г.\033[0m')
    print('\033[30m\033[47mБлагодарю за внимание :-)\033[0m')


async def start_strongman(name, power):
    start = time.time()
    balls = 5
    zim = balls / power
    print(f'\033[32mСилач {name} начал соревнования, сила: {power}, шаров: {balls}\033[0m')
    for ball in range(1, balls + 1):
        await asyncio.sleep(zim)
        print(f'Силач \033[34m{name}\033[0m поднял \033[35m{ball}\033[0m шар.')
    finish = time.time()
    print(f'\033[31mСилач {name} закончил соревнования за {round(finish - start, 2)} сек.\033[0m')


async def start_tournament():
    strongman1 = asyncio.create_task(start_strongman('Pasha', 3))
    strongman2 = asyncio.create_task(start_strongman('Denis', 4))
    strongman3 = asyncio.create_task(start_strongman('Apolon', 5))
    await strongman1
    await strongman2
    await strongman3


greeting()
asyncio.run(start_tournament())
farewell()
