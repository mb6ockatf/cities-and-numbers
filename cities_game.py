from off import off


def text_cities_rules():
    from time import sleep
    print("Правила игры в 'Города России':\n\
        Каждый участник в свою очередь называет реально существующий город России,\n\
        название которого начинается на ту букву, которой оканчивается название предыдущего названного города.\n\
        Если вы уже дочитали это сообщение, то просто подождите.\n")
    sleep(8)


first_time = True
mentioned = []
prevword = 0
turn = 0


def check(city):
    global first_time
    pass_check = False
    while not pass_check:
        while city.word in mentioned:
            print('Такой город уже был. \nВводи другой: ')
            city = InputWord(input('Вводи название города: '))
        pass_check = True
        if not first_time:
            while not city.pass_first_word(prevword):
                print('Это слово начинается не на последнюю букву предыдущего города.\nВведите другое.')
                city = InputWord(input('Вводи название города: '))
                pass_check = False
    mentioned.append(city.word)


class InputWord:
    def __init__(self, word):
        global turn
        self.word = word.lower()
        if self.word == '!':
            print('Игра завершилась на', turn, 'коне.')
            off()
        self.last_letter = self.word[-1]
        self.first_letter = self.word[0]

    def pass_first_word(self, previous):
        if self.word[0] == previous.last_letter:
            return True
        return False

    def reply(self):
        from cities_lists import abc
        while True:
            for k in abc:
                if k == self.last_letter:
                    if abc[k] is not False:
                        for j in abc[k]:
                            if str(j) not in mentioned:
                                mentioned.append(str(j))
                                return str(j)
                        return False
                    self.last_letter = self.word[-2]
                    break
            continue


def cities_game():  # noqa: C901
    global mentioned, first_time, prevword, turn
    print("Игра в 'Города России' началась.\nЧтобы выйти, введите '!'")
    print('----------------------------')
    print('Это', turn + 1, 'кон.')
    city = InputWord(input('Вводи название города: '))
    while True:
        check(city)
        prevword = city.reply()
        if not prevword:
            print('Я проиграл - незнаю города на такую букву.')
        else:
            print('А мой ответ - ' + prevword)
            first_time = False
            prevword = InputWord(prevword)
        turn += 1
        print('Это', turn + 1, 'кон.')
        city = InputWord(input('Вводи название города: '))
