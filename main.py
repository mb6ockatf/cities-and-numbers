def welcome():
    print('Приветствую!')
    print('Выберите один из следующих пунктов, чтобы продолжить:')
    print()
    print('---"Города России". Введите "1", чтобы запустить.')
    print('---"Числа". Введите "2", чтобы запустить.')
    print()
    game_choice = int(input('Ваш выбор: '))
    while game_choice != int(1) and game_choice != int(2):
        print('Вы ввели что-то непонятное.')
        game_choice = int(input("Ваш выбор: "))
    if game_choice == int(1):
        print("Вы выбрали пункт 'Города Росcии'.")
        print("Чтобы узнать правила, введите 1. Чтобы начать, введите 2")
        print()
        rules_or_game = input("Ваш выбор: ")
        while rules_or_game != str(1) and rules_or_game != str(2):
            print('Вы ввели что-то непонятное.')
            rules_or_game = str(input("Ваш выбор: "))
        import cities_game
        if rules_or_game == str(1):
            cities_game.text_cities_rules()
            cities_game.cities_game()
        else:
            cities_game.cities_game()
    elif game_choice == int(2):
        print("Вы выбрали пункт 'Числа'.")
        print("Чтобы узнать правила, введите 1. Чтобы начать, введите 2")
        print()
        rules_or_game = input("Ваш выбор: ")
        while rules_or_game != str(1) and rules_or_game != str(2):
            print('Вы ввели что-то непонятное.')
            rules_or_game = input("Ваш выбор: ")
        import numbers_game
        if rules_or_game == str(1):
            numbers_game.text_numbers_rules()
            numbers_game.numbers_game()
        else:
            numbers_game.numbers_game()


if __name__ == '__main__':
    welcome()
