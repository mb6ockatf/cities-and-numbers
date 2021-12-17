from time import sleep
wins = 0
loses = 0
overall = 0
balance = 0
mentioned = []
your_num = input("Игра в 'Числа' началась.\nЧтобы закончить, введите !\nТы начинаешь.\n\
Вводи своё число: ")
while your_num != '!':
    while True:
        try:
            your_num = int(your_num)
            break
        except ValueError:
            your_num = input("Не целое число.\nВводите: ")
    while your_num in mentioned or not (1 <= your_num <= 100):
        while your_num in mentioned:
            your_num = input('Такое число уже было названо, введите другое.\nВводи своё число: ')
        while not 1 <= int(your_num <= 100):
            self = input('Твоё число не в ходит в диапазон от 1 до 100\nВводи своё число: ')
    mentioned.append(your_num)
    from random import randint

    if len(mentioned) == 100:
        answer = 0
    else:
        out = randint(1, 100)
        while out in mentioned:
            out = randint(1, 100)
        mentioned.append(out)
        answer = out
    if answer != 0:
        print('А мой ответ равен', answer)
        overall += 1
        if answer > your_num:
            loses += 1
        elif answer < your_num:
            wins += 1
        else:
            balance += 1
        your_num = input('Вводи своё число: ')
    else:
        print('Чисел больше нет, игра завершилась.')
        your_num = '!'
print('Пришло время подвести итоги.', 'Пользователь выиграл:', wins, 'Пользователь проиграл:', loses,
      'Баланс был:', balance, 'Всего было сделано конов:', overall, sep='\n')
print('Всё, игра закончена. Программа выключится через 8 секунд.')
for j in range(8, 0, -1):
    print('Осталось %i секунд(ы)' % j)
    sleep(1)
quit()
