import random


def eagle_or_tails():
    """Игра в орел или решка."""

    again = 'да'
    while again.lower() == 'да':
        for _ in range(1):
            num = random.randint(0, 1)
            print('Бросаем кубик... ')
            if num == 0:
                print('Выпал Орел')
            else:
                print('Выпала Решка')
        again = input('Бросить монетку еще раз? да/нет: ')


if __name__ == "__main__":
    eagle_or_tails()
