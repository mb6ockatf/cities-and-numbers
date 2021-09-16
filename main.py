from cities_game import cities_rules, cities_game
from numbers_game import numbers_rules, numbers_game


def welcome():
    print('Приветствую!')
    print('Выберите один из следующих пунктов, чтобы продолжить:')
    print()
    print('---"Города России". Введите "1", чтобы запустить.')
    print('---"Числа". Введите "2", чтобы запустить.')
    print()
    game_choice = str(input('Ваш выбор: '))
    if game_choice == "1":
        print("Вы выбрали пункт 'Города Росcии'.")
        print("Чтобы узнать правила, введите 1. Чтобы начать, введите 2")
        print()
        rules_or_game = str(input("Ваш выбор: "))
        if rules_or_game == '1':
            cities_rules()
            cities_game()
        elif rules_or_game == '2':
            cities_game()
        else:
            print('Вы ввели что-то непонятное. Перезапустите программу.')
    elif game_choice == "2":
        print("Вы выбрали пункт 'Числа'.")
        print("Чтобы узнать правила, введите '1'. Чтобы начать, введите 2")
        print()
        rules_or_game = str(input("Ваш выбор: "))
        if rules_or_game == '1':
            numbers_rules()
            numbers_game()
        elif rules_or_game == '2':
            numbers_game()
        else:
            print('Вы ввели что-то непонятное. Перезапустите программу.')


if __name__ == '__main__':
    welcome()
