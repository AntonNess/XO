print("Добро пожаловать в игру крестики-нолики!\n"
       "Для установки своего знака, в предлагаемом диалоге выберете цифру необходимого поля.\n"
       "Удачи Вам!")
bord = list(range(1, 10))
win = [(1, 2, 3),
       (4, 5, 6),
       (7, 8, 9),
       (1, 4, 7),
       (2, 5, 8),
       (3, 6, 9),
       (1, 5, 9),
       (3, 5, 7)]


def new_bord():
    for i in range(3):
        print("|", bord[0 + i * 3], "|", bord[1 + i * 3], "|", bord[2 + i * 3], "|")


def xo(enter_xo):
    while True:
        address = input("Введите куда ставим " + enter_xo + ":")
        if not (address in '123456789'):
            print("Ошибка ввода, превышен интервал ввода")
            continue
        address = int(address)
        if str(bord[address - 1]) in "X0":
            print('Клетка занята')
            continue
        bord[address - 1] = enter_xo
        break


def winers():
    for answer in win:
        if (bord[answer[0] - 1]) == (bord[answer[1] - 1]) == (bord[answer[2] - 1]):
            return bord[answer[1] - 1]
    else:
        return False


def game():
    counter = 0
    while True:
        new_bord()
        if counter % 2 == 0:
            xo("X")
        else:
            xo("0")
        if counter > 3:
            end = winers()
            if end:
                new_bord()
                print("Победил", end, "!!!")
                break
        counter += 1
        if counter > 8:
            new_bord()
            print("Победила дружба!")
            break


game()
