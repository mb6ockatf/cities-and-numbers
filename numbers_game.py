def text_numbers_rules():
    print("Правила игры в 'Числа':\nНазовите любое целое число от 1 до 100. Нельзя называть уже названные \n"
          "числа, следовательно, в одной игре не может быть больше 50 конов \nУ кого число больше, тот и выиграл кон.")
    print('При этом, *совпадение чисел допускается* .')
    from time import sleep
    sleep(8)


def numbers_game():
    class InputNum:
        def __init__(self, num):
            self.num = num

        def mention(self):
            mentioned.append(self.num)

        def check_range(self):
            if 1 <= self.num <= 100:
                return True
            else:
                return False

    def show_results():
        """
        Программа выдаёт разные окончания слов в зависимости от числа
        """
        print('Пришло время подвести итоги.')
        print('Пользователь выиграл:', wins)
        print('Пользователь проиграл:', loses)
        print('Баланс был:', balance)
        print('Всего было сделано конов:', overall)

    def reply():
        from random import randint
        if len(mentioned) == 100:
            return 0
        reply = randint(1, 100)
        while reply in mentioned:
            reply = randint(1, 100)
        return reply

    print("Игра в 'Числа' началась.")
    print('Чтобы закончить, введите !')
    wins = 0
    loses = 0
    overall = 0
    balance = 0
    mentioned = []
    print('Ты начинаешь.')
    first_time = True
    your_num = InputNum(int(input('Вводи своё число: ')))
    while your_num != '!':
        if not first_time:
            your_num = InputNum(your_num)
        while not your_num.check_range():
            print('Твоё число не в ходит в диапазон от 1 до 100')
            your_num = InputNum(input('Вводи своё число: '))
        your_num.mention()
        reply = reply()
        if reply != 0:
            print('А мой ответ равен', reply)
            overall += 1
            if reply > your_num.num:
                loses += 1
            elif reply < your_num.num:
                wins += 1
            else:
                balance += 1
            your_num = input('Вводи своё число: ')
        else:
            print('Чисел больше нет, игра завершилась.')
            your_num = InputNum('!')
    show_results()
    from turnoff import turnoff

    turnoff()
