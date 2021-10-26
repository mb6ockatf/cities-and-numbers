from time import sleep
from random import randint
from turnoff import *


def text_numbers_rules():
    print("Правила игры в 'Числа': ")
    print("Назовите любое целое число от 1 до 100. Нельзя называть уже названные \
        числа, следовательно, в одной игре не может быть больше 50 конов. \
        У кого число больше, тот и выиграл кон.))")
    print('При этом, *совпадение чисел допускается* .')
    sleep(8)


def numbers_game():
    def numbers_turn(num):
        print()
        print()
        print('Это', int(len(overall) + 1), 'кон.')
        if int(num) != '!':
            if num not in mentioned_nums:
                answer_num = randint(1, 100)
                if answer_num not in mentioned_nums:
                    print(num, ", а мой ответ равен", answer_num)
                    check_turn_win(num, answer_num)
                else:
                    while answer_num in mentioned_nums:
                        answer_num = randint(1, 100)
                    print('% ,', " а мой ответ равен", answer_num % int(num))
                    check_turn_win(num, answer_num)
                num = input('Вводи новое число: ')
            else:
                print('Это число уже было названо.')
                num = input('Введите новое число: ')
            return num
        else:
            show_results()
            turnoff()

    def check_turn_win(num, answer_num):
        overall.append("1")
        mentioned_nums.append(str(num))
        mentioned_nums.append(str(answer_num))
        if int(num) > int(answer_num):
            print("Ты выиграл.")
            wins.append("1")
        elif int(num) < int(answer_num):
            print("Выиграл я.")
            loses.append("1")
        elif int(num) == int(answer_num):
            print("Совпадение века, наши числа равны.")
            balance.append("1")
        print('Кон засчитан.')
        print()

    def show_results():
        """
        Программа выдаёт разные окончания слов в зависимости от числа
        """
        print('Пришло время подвести итоги.')
        if len(wins) % 10 == 1 or len(wins) % 10 == 0 or \
                len(wins) % 10 == 5 or len(wins) % 10 == 6 or \
                len(wins) % 10 == 7 or len(wins) % 10 == 8 or \
                len(wins) % 10 == 9:
            print('Пользователь выиграл', len(wins), 'раз.')
        elif len(wins) % 10 == 2 or len(wins) % 10 == 3 \
                or len(wins) % 10 == 4:
            print('Пользователь выиграл', len(wins), 'раза.')

        if len(loses) % 10 == 1 or len(loses) % 10 == 0 or \
                len(loses) % 10 == 5 or len(loses) % 10 == 6 or \
                len(loses) % 10 == 7 or len(loses) % 10 == 8 or \
                len(loses) % 10 == 9:
            print('Пользователь выиграл', len(loses), 'раз.')
        elif len(loses) % 10 == 2 or len(loses) % 10 == 3 \
                or len(loses) % 10 == 4:
            print('Пользователь выиграл', len(loses), 'раза.')

        if len(balance) % 10 == 1 or len(balance) % 10 == 0 or \
                len(balance) % 10 == 5 or len(balance) % 10 == 6 or \
                len(balance) % 10 == 7 or len(balance) % 10 == 8 or \
                len(balance) % 10 == 9:
            print('Пользователь выиграл', len(balance), 'раз.')
        elif len(balance) % 10 == 2 or len(balance) % 10 == 3 \
                or len(wins) % 10 == 4:
            print('Пользователь выиграл', len(wins), 'раза.')

    print("Игра в 'Числа' началась.")
    print('Чтобы закончить, введите !')
    wins = []
    loses = []
    overall = []
    balance = []
    mentioned_nums = []
    print('Ты начинаешь.')
    your_num = input('Вводи своё число: ')
    while True:
        numbers_turn(your_num)
