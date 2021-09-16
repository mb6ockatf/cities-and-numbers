from time import sleep
from random import randint
from turnoff import turnoff


def numbers_rules():
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
        print('Это', int(len(counted_overall) + 1), 'кон.')
        if int(num) != '!':
            if num not in mentioned_cities:
                answer_num = randint(1, 100)
                if answer_num not in mentioned_cities:
                    print(num, ", а мой ответ равен", answer_num)
                    check_winner_count_words(num, answer_num)
                else:
                    while answer_num in mentioned_cities:
                        answer_num = randint(1, 100)
                    print('% ,', " а мой ответ равен", answer_num % int(num))
                    check_winner_count_words(num, answer_num)
                num = input('Вводи новое число: ')
            else:
                print('Это число уже было названо.')
                print('Кон завершается аварийно, никто не выиграл. Запускаю следующий кон.')
                num = input('Введите новое число: ')
        else:
            show_results()
            turnoff()

    def check_winner_count_words(num, answer_num):
        counted_overall.append("1")
        mentioned_cities.append(str(num))
        mentioned_cities.append(str(answer_num))
        if int(num) > int(answer_num):
            print("Ты выиграл.")
            counted_wins.append("1")
        elif int(num) < int(answer_num):
            print("Выиграл я.")
            counted_loses.append("1")
        elif int(num) == int(answer_num):
            print("Совпадение века, наши числа равны.")
            counted_balance.append("1")
        print('Кон засчитан.')
        print()

    def show_results():
        """
        Программа выдаёт разные сообщения в зависимости от числа
        """
        print('Пришло время подвести итоги.')
        if len(counted_wins) % 10 == 1 or len(counted_wins) % 10 == 0 or \
                len(counted_wins) % 10 == 5 or len(counted_wins) % 10 == 6 or \
                len(counted_wins) % 10 == 7 or len(counted_wins) % 10 == 8 or \
                len(counted_wins) % 10 == 9:
            print('Пользователь выиграл', len(counted_wins), 'раз.')
        elif len(counted_wins) % 10 == 2 or len(counted_wins) % 10 == 3 \
                or len(counted_wins) % 10 == 4:
            print('Пользователь выиграл', len(counted_wins), 'раза.')

        if len(counted_loses) % 10 == 1 or len(counted_loses) % 10 == 0 or \
                len(counted_loses) % 10 == 5 or len(counted_loses) % 10 == 6 or \
                len(counted_loses) % 10 == 7 or len(counted_loses) % 10 == 8 or \
                len(counted_loses) % 10 == 9:
            print('Пользователь выиграл', len(counted_loses), 'раз.')
        elif len(counted_loses) % 10 == 2 or len(counted_loses) % 10 == 3 \
                or len(counted_loses) % 10 == 4:
            print('Пользователь выиграл', len(counted_loses), 'раза.')

        if len(counted_balance) % 10 == 1 or len(counted_balance) % 10 == 0 or \
                len(counted_balance) % 10 == 5 or len(counted_balance) % 10 == 6 or \
                len(counted_balance) % 10 == 7 or len(counted_balance) % 10 == 8 or \
                len(counted_balance) % 10 == 9:
            print('Пользователь выиграл', len(counted_balance), 'раз.')
        elif len(counted_balance) % 10 == 2 or len(counted_balance) % 10 == 3 \
                or len(counted_wins) % 10 == 4:
            print('Пользователь выиграл', len(counted_wins), 'раза.')

    print("Игра в 'Числа' началась.")
    print('Чтобы закончить, введите !')
    counted_wins = []
    counted_loses = []
    counted_overall = []
    counted_balance = []
    mentioned_cities = []
    print('Ты начинаешь.')
    num = input('Вводи своё число: ')
    endless_cycle = True
    while endless_cycle:
        numbers_turn(num)
