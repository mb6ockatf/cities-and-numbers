def numbersgame():
    def oneturn():
        print()
        print()
        print('Это', int(len(has_been_mentioned_overall) + 1), 'кон.')
        num = input('Вводи новое число: ')
        if int(num) != '!':
            if num not in mentioned:
                answer_num = random.randint(1, 100)
                if answer_num not in mentioned:
                    print(num, ", а мой ответ равен", answer_num)
                    analyticsnumbers(num, answer_num)
                    oneturn()
                else:
                    while answer_num in mentioned:
                        answer_num = random.randint(1, 100)
                    print('% ,', " а мой ответ равен", answer_num % int(num))
                    analyticsnumbers(num, answer_num)
                    oneturn()
            else:
                print('Это число уже было названо.')
                print('Кон завершается аварийно, никто не выиграл. Запускаю следующий кон.')
                oneturn()
        else:
            showresults()
            turnoff()

    def turnoff():
        print('Всё, игра закончена. Программа выключится через 8 секунд.')
        left_time = 8
        for j in range(:8, -1):
            print('Осталось %i секунд(ы)' % left_time)
            left_time += left_time - 1
            sleep(1)
        # TODO: bugs may appear in this cycle above
        quit()

    def analyticsnumbers(num, answer_num):
        has_been_mentioned_overall.append("1")
        mentioned.append(str(num))
        mentioned.append(str(answer_num))
        if int(num) > int(answer_num):
            print("Ты выиграл.")
            has_been_mentioned_wins.append("1")
        elif int(num) < int(answer_num):
            print("Выиграл я.")
            has_been_mentioned_loses.append("1")
        elif int(num) == int(answer_num):
            print("Совпадение века, наши числа равны.")
            has_been_mentioned_balance.append("1")
        print('Кон засчитан.')
        print()

    def showresults():
        print('Пришло время подвести итоги.')
        if len(has_been_mentioned_wins) % 10 == 1 or len(has_been_mentioned_wins) % 10 == 0 or \
            len(has_been_mentioned_wins) % 10 == 5 or len(has_been_mentioned_wins) % 10 == 6 or \
            len(has_been_mentioned_wins) % 10 == 7 or len(has_been_mentioned_wins) % 10 == 8 or \
            len(has_been_mentioned_wins) % 10 == 9:
            print('Пользователь выиграл', len(has_been_mentioned_wins), 'раз.')
        elif len(has_been_mentioned_wins) % 10 == 2 or len(has_been_mentioned_wins) % 10 == 3 \
            or len(has_been_mentioned_wins) % 10 == 4:
            print('Пользователь выиграл', len(has_been_mentioned_wins), 'раза.')

        if len(has_been_mentioned_loses) % 10 == 1 or len(has_been_mentioned_loses) % 10 == 0 or \
            len(has_been_mentioned_loses) % 10 == 5 or len(has_been_mentioned_loses) % 10 == 6 or \
            len(has_been_mentioned_loses) % 10 == 7 or len(has_been_mentioned_loses) % 10 == 8 or \
            len(has_been_mentioned_loses) % 10 == 9:
            print('Пользователь выиграл', len(has_been_mentioned_loses), 'раз.')
        elif len(has_been_mentioned_loses) % 10 == 2 or len(has_been_mentioned_loses) % 10 == 3 \
            or len(has_been_mentioned_loses) % 10 == 4:
            print('Пользователь выиграл', len(has_been_mentioned_loses), 'раза.')

        if len(has_been_mentioned_balance) % 10 == 1 or len(has_been_mentioned_balance) % 10 == 0 or \
            len(has_been_mentioned_balance) % 10 == 5 or len(has_been_mentioned_balance) % 10 == 6 or \
            len(has_been_mentioned_balance) % 10 == 7 or len(has_been_mentioned_balance) % 10 == 8 or \
            len(has_been_mentioned_balance) % 10 == 9:
            print('Пользователь выиграл', len(has_been_mentioned_balance), 'раз.')
        elif len(has_been_mentioned_balance) % 10 == 2 or len(has_been_mentioned_balance) % 10 == 3 \
            or len(has_been_mentioned_wins) % 10 == 4:
            print('Пользователь выиграл', len(has_been_mentioned_wins), 'раза.')

    from time import sleep
    import random
    print("Игра в 'Числа' началась.")
    print('Чтобы закончить, введите !')
    has_been_mentioned_wins = []
    has_been_mentioned_loses = []
    has_been_mentioned_overall = []
    has_been_mentioned_balance = []
    mentioned = []
    print('Ты начинаешь.')
    oneturn()
