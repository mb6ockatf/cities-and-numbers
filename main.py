game_choice = int(input('Приветствую!\n\
Выберите один из следующих пунктов, чтобы продолжить:\n\n\
- "Города России". Введите "1", чтобы запустить.\n\
- "Числа". Введите "2", чтобы запустить.\n\
Ваш выбор: '))
while game_choice != 1 and game_choice != 2:
    game_choice = int(input("Вы ввели что-то непонятное.\n\
Ваш выбор: "))


if game_choice == 1:
    rules_or_game = input("Вы выбрали пункт 'Города Росcии'.\n\
Чтобы узнать правила, введите 1. Чтобы начать, введите 2\nВаш выбор: ")
    while rules_or_game != '1' and rules_or_game != '2':
        rules_or_game = input('Вы ввели что-то непонятное.\nВаш выбор: ')
    import cities_game
    if rules_or_game == '1':
        cities_game.text_cities_rules()
        cities_game.cities_game()
    else:
        cities_game.cities_game()


elif game_choice == 2:
    rules_or_game = input("Вы выбрали пункт 'Числа'.\nЧтобы узнать правила, введите 1. Чтобы начать, введите 2\n\
Ваш выбор: ")
    while rules_or_game != '1' and rules_or_game != '2':
        rules_or_game = input("Вы ввели что-то непонятное.\nВаш выбор: ")
    if rules_or_game == '1':
        print("Правила игры в 'Числа':\n\
        Назовите любое целое число от 1 до 100. Нельзя называть уже названные \n\
        числа, следовательно, в одной игре не может быть больше 50 конов \n\
        У кого число больше, тот и выиграл кон.\n\
        При этом, *совпадение чисел допускается* .")
        from time import sleep
        sleep(8)
        import numbers_game
    else:
        import numbers_game
