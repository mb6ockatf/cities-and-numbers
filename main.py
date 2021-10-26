from cities_game import text_cities_rules, cities_game
from numbers_game import text_numbers_rules, numbers_game


def welcome():
    print('Приветствую!')
    print('Выберите один из следующих пунктов, чтобы продолжить:')
    print()
    print('---"Города России". Введите "1", чтобы запустить.')
    print('---"Числа". Введите "2", чтобы запустить.')
    print()
    game_choice = int(input('Ваш выбор: '))
    while game_choice != 1 and game_choice != 2:
        print('Вы ввели что-то непонятное.')
        game_choice = int(input("Ваш выбор: "))
    if game_choice == 1:
        print("Вы выбрали пункт 'Города Росcии'.")
        print("Чтобы узнать правила, введите 1. Чтобы начать, введите 2")
        print()
        rules_or_game = input("Ваш выбор: ")
        while rules_or_game != 1 or rules_or_game != 2:
            print('Вы ввели что-то непонятное.')
            rules_or_game = input("Ваш выбор: ")
        if rules_or_game == 1:
            text_cities_rules()
            cities_game()
        else:
            cities_game()
    elif game_choice == 2:
        print("Вы выбрали пункт 'Числа'.")
        print("Чтобы узнать правила, введите 1. Чтобы начать, введите 2")
        print()
        rules_or_game = int(input("Ваш выбор: "))
        while rules_or_game != 1 or rules_or_game != 2:
            print('Вы ввели что-то непонятное.')
            rules_or_game = int(input("Ваш выбор: "))
        if rules_or_game == 1:
            text_numbers_rules()
            numbers_game()
        else:
            numbers_game()


if __name__ == '__main__':
    welcome()
