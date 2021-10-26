def text_cities_rules():
    print("Правила игры в 'Города России':\n"
          "Каждый участник в свою очередь называет реально существующий город России,\n"
          "название которого начинается на ту букву, которой оканчивается название предыдущего названного города.\n"
          'Если вы уже дочитали это сообщение, то просто подождите.\n')
    from time import sleep
    sleep(8)


class InputWord:
    def __init__(self, word):
        self.word = word
        last_letter = self.word[-1]
        first_letter = self.word[0]
        self.last_letter = last_letter
        self.first_letter = first_letter

    def pass_first_word(self):
        if self.word[0] == prevword[-1]:
            return True
        else:
            return False

    def reply(self):
        from cities_lists import abv, abc
        position = 0
        for char in abv:
            position += 1
            if char == self.last_letter:
                break
        try:
            for g in abc[position]:
                if g not in mentioned:
                    return g
        except IndexError:
            return False

    def mention(self):
        mentioned.append(self.word)


print("Игра в 'Города России' началась.")
print("Чтобы выйти, введите '!'")
mentioned = []
turn_number = 0
print('----------------------------')
city = input('Вводи название города: ')
while city != '!':
    while city in mentioned:
        print('Такой город уже был. \nВводи другой: ')
        city = input('Вводи название города: ')
    city = InputWord(city)
    city.mention()
    prevword = city.reply()
    if not prevword:
        print('Я проиграл - незнаю города на такую букву.')
    else:
        print('А мой ответ - ' + str(prevword))
    city = input('Вводи название города: ')
