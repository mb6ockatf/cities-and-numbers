def text_cities_rules():
    print("Правила игры в 'Города России':\n"
          "Каждый участник в свою очередь называет реально существующий город России,\n"
          "название которого начинается на ту букву, которой оканчивается название предыдущего названного города.\n"
          'Если вы уже дочитали это сообщение, то просто подождите.\n')
    from time import sleep
    sleep(8)


first_time = True
mentioned = []
prevword = 0


def check(city) -> None:
    global first_time
    pass_check = False
    while not pass_check:
        while city.word in mentioned:
            print('Такой город уже был. \nВводи другой: ')
            city.word = InputWord(input('Вводи название города: ')).word
        pass_check = True
        if not first_time:
            while not city.pass_first_word():
                print('Это слово начинается не на последнюю букву предыдущего города.\nВведите другое.')
                city.word = InputWord(input('Вводи название города: ')).word
                pass_check = False
    first_time = False


class InputWord:
    def __init__(self, word):
        self.word = word
        self.last_letter = self.word[-1]
        self.first_letter = self.word[0]

    def pass_first_word(self):
        if self.word[0] == str(prevword)[-1]:
            return True
        return False

    def reply(self):
        from cities_lists import abv, abc
        for k in abc:
            if k == self.last_letter:
                for j in abc[k]:
                    if j not in mentioned:
                        return j

    def mention(self):
        mentioned.append(self.word)


def cities_game():
    global mentioned, first_time, prevword
    print("Игра в 'Города России' началась.\nЧтобы выйти, введите '!'")
    print('----------------------------')
    turn = 0
    print('Это', turn + 1, 'кон.')
    city = InputWord(input('Вводи название города: '))
    while city != '!':
        check(city)
        city.mention()
        prevword = city.reply()
        if not prevword:
            print('Я проиграл - незнаю города на такую букву.')
        else:
            print('А мой ответ - ' + str(prevword))
            first_time = False
            prevword = InputWord(prevword)
            prevword.mention()
        turn += 1
        print('Это', turn + 1, 'кон.')
        city = InputWord(input('Вводи название города: '))
    print('Игра завершилась на', turn, 'коне.')
    from turnoff import turnoff
    turnoff()
