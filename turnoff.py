from time import sleep


def turnoff():
    print('Всё, игра закончена. Программа выключится через 8 секунд.')
    left_time = 8
    for j in range(8, -1):
        print('Осталось %i секунд(ы)' % left_time)
        left_time += left_time - 1
        sleep(1)
    quit()
