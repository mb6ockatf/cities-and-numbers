def off():
    from time import sleep
    print('Всё, игра закончена. Программа выключится через 8 секунд.')
    for j in range(8, 0, -1):
        print('Осталось %i секунд(ы)' % j)
        sleep(1)
    quit()
