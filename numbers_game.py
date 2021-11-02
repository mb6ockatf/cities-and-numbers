def text_numbers_rules():
    print("Правила игры в 'Числа':\n\
        Назовите любое целое число от 1 до 100. Нельзя называть уже названные \n\
        числа, следовательно, в одной игре не может быть больше 50 конов \n\
        У кого число больше, тот и выиграл кон.\n\
        При этом, *совпадение чисел допускается* .")
    from time import sleep
    sleep(8)


def reply():
    from random import randint
    if len(mentioned) == 100:
        return 0
    out = randint(1, 100)
    while out in mentioned:
        out = randint(1, 100)
    mentioned.append(out)
    return out


def show_results():
    """
    Программа выдаёт разные окончания слов в зависимости от числа
    """
    print('Пришло время подвести итоги.')
    print('Пользователь выиграл:', wins)
    print('Пользователь проиграл:', loses)
    print('Баланс был:', balance)
    print('Всего было сделано конов:', overall)


wins = 0
loses = 0
overall = 0
balance = 0
mentioned = []


def numbers_game():  # noqa: C901
    global wins, loses, overall, balance, mentioned

    class InputNum:
        def __init__(self, num) -> None:
            self.num = int(num)

        def check(self) -> None:
            while self.num in mentioned or not 1 <= self.num <= 100:
                while self.num in mentioned:
                    print('Такое число уже было названо, введите другое.')
                    self.num = InputNum(input('Вводи своё число: ')).num
                while not 1 <= self.num <= 100:
                    print('Твоё число не в ходит в диапазон от 1 до 100')
                    self = InputNum(input('Вводи своё число: '))
            mentioned.append(self.num)


    print("Игра в 'Числа' началась.")
    print('Чтобы закончить, введите !')
    print('Ты начинаешь.')
    first_time = True
    your_num = InputNum(input('Вводи своё число: '))
    while your_num.num != '!':
        your_num.check()
        answer = reply()
        if answer != 0:
            print('А мой ответ равен', answer)
            overall += 1
            if answer > your_num.num:
                loses += 1
            elif answer < your_num.num:
                wins += 1
            else:
                balance += 1
            your_num = InputNum(input('Вводи своё число: '))
        else:
            print('Чисел больше нет, игра завершилась.')
            your_num = InputNum('!')
    show_results()
    from turnoff import turnoff
    turnoff()
