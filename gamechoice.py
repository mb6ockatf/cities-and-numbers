def gamechoice():
    gamechoice = str(input('Ваш выбор: '))
    if gamechoice == "1":
        print("Вы выбрали пункт 'Города Росcии'.")
        print("Чтобы узнать правила, введите 1. Чтобы начать, введите 2")
        print()
        rulesorgamechoice = str(input("Ваш выбор: "))
        if rulesorgamechoice == '1':
            from rulesforcities import rulesforcities
            rulesforcities()
        elif rulesorgamechoice == '2':
            from citiesgame import citiesgame
            citiesgame()
        else:
            print('Вы ввели что-то непонятное. Перезапустите программу.')
    elif gamechoice == "2":
        print("Вы выбрали пункт 'Числа'.")
        print("Чтобы узнать правила, введите '1'. Чтобы начать, введите 2")
        print()
        rulesorgamechoice = str(input("Ваш выбор: "))
        if rulesorgamechoice == '1':
            from rulesfornumbers import rulesfornumbers
            rulesfornumbers()
        elif rulesorgamechoice == '2':
            from numbersgame import numbersgame
            numbersgame()
        else:
            print('Вы ввели что-то непонятное. Перезапустите программу.')
