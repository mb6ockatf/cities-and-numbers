from time import sleep

first_time = True
mentioned = []
previous = None
previous_last_letter = None
last_letter = None
turn = 0


def leave():
    if city == '!':
        print('Игра завершилась на', turn, 'коне.\nВсё, игра закончена. Программа выключится через 8 секунд.')
        for j in range(8, 0, -1):
            print('Осталось %i секунд(ы)' % j)
            sleep(1)
        quit()


print("Игра в 'Города России' началась.\nЧтобы выйти, введите '!'", ''.center(100, '-'), f'Это {turn + 1} кон.',
      sep='\n')
city = input('Вводи название города: ')
while True:
    leave()
    city = city.lower()
    pass_check = False
    while not pass_check:
        while city in mentioned:
            city = input('Такой город уже был. \nВводи название города: ')
            leave()
        pass_check = True
        if not first_time:
            while not city[0] == previous_last_letter:
                city = input('Это слово начинается не на последнюю букву предыдущего города.\n\
Введите другое: ')
                leave()
                pass_check = False
    mentioned.append(city)
    last_letter = city[-1] if (city[-1] != 'ё' or city[-1] != 'ь' or city[-1] != '\
ъ' or city != 'ы') else city[-2]
    from cities_lists import abc
    for letter_list in abc:
        if letter_list == last_letter and abc[letter_list] is not False:
            for answer in abc[letter_list]:
                if answer not in mentioned:
                    mentioned.append(answer)
                    previous = answer
                    break
                else:
                    previous = False
        else:
            continue
        break
    if not previous:
        print('Я проиграл - незнаю города на такую букву.')
        print('Всё, игра закончена. Программа выключится через 8 секунд.')
        for j in range(8, 0, -1):
            print('Осталось %i секунд(ы)' % j)
            sleep(1)
        quit()
    else:
        print('А мой ответ - ' + previous)
        first_time = False
        # previous is not bool
        previous_last_letter = previous[-2] if (previous[-1] == 'ё' or previous[-1] == 'ь\
' or previous[-1] == 'ъ' or previous[-1] == 'ы') else previous[-1]
    turn += 1
    print('Это', turn + 1, 'кон.')
    city = input('Вводи название города: ')
