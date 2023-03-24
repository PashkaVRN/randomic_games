import random


def game_dice():
    """Игра сброса игральных костей."""

    again = 'да'
    while again.lower() == 'да':
        print('Бросаем кубики... ')
        print('Значения граней:')
        print(random.randint(1, 6))
        again = input('Бросить кубики еще раз? да/нет: ')


if __name__ == "__main__":
    game_dice()
