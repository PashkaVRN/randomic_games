from time import *
from random import randint

def guess_the_number():
    """Игра в угадай число."""

    print("Игра - 'Угадайка число!'")
    sleep(1)
    print('Правила игры:')
    print('    Я загадаю число, а тебе придется угадать по принцепу тепло/холодно.')
    sleep(1)
    name = input('Привет, введите имя: ')
    num = randint(1, 100)
    while True:
        user_num = int(input(f'{name}, введите число от 1 до 100: '))
        sleep(1)
        if user_num > num:
            print('Слишком много, давайте еще разок')
        elif user_num < num:
            print('Слишком мало, давайте еще разок')
        else:
            print('Вы угадали!')
            sleep(2.5)
            print(f'{name}, хотите еще сыграть?')
            sleep(0.5)
            if input() == 'да':
                sleep(1)
                print('')
                continue
            else:
                sleep(1.0)
                print('')
                print('Ясненько')
                sleep(1.2)
                print('Понятненько')
                sleep(1.2)
                print('Ну что ж, 'f'{name}, рад был поиграть с тобой, до новых встреч!')
                break

if __name__ =='__main__':
    guess_the_number()