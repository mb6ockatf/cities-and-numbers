def rulesfornumbers():
    import time
    import numbersgame
    print("Правила игры в 'Числа': ")
    print("Назовите любое целое число от 1 до 100. Нельзя называть уже названные \
        числа, следовательно, в одной игре не может быть больше 50 конов. \
        У кого число больше, тот и выиграл кон.))")
    print('При этом, *совпадение чисел допускается* .')
    time.sleep(8)
    from numbersgame import numbersgame
    numbersgame()
