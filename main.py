def ask_choise():
    global what_program
    what_program = int(input("\nВы хотите проверить улучшение уровня Силы, Интеллекта или уровня персонажа?\n"
                             "Для Силы введите — 1, для Интеллекта — 2, для уровня персонажа — 3, для выхода — 0\n"
                             "Если хотите узнать сколько уровней персонажа вы сможете прокачать за имеющийся опыт — 4\n"
                             "Если хотите узнать сколько уровней Силы/Интеллекта вы сможете прокачать за имеющиеся ОХ — 5\n"))
    func_numbers = [0, 1, 2, 3, 4, 5]
    found = 0
    for i in func_numbers:
        if (what_program == i):
            found = 1
            break
    if (found != 1):
        print("Вы ввели неправильное число, попробуйте еще раз")
        ask_choise()



what_program = 9999;
while (what_program != 0):
    ask_choise()
    if (what_program == 1):
        N1 = int(input("Введите текущий уровень Силы: "))
        N2 = int(input("Введите уровень, которого хотите достичь: "))
        if (N2 > N1):
            oh = 0
            s = 0
            v = 0

            for i in range(N1 + 1, N2 + 1):
                if (i % 5 != 0) and (i % 10 != 0) and (i % 50 != 0):
                    oh += 1
                    s += 1
                    v += 50
                elif (i % 10 != 0) and (i % 50 != 0):
                    oh += 2
                    s += 5
                    v += 100
                elif i % 50 != 0:
                    oh += 4
                    s += 10
                    v += 500
                else:
                    oh += 8
                    s += 15
                    v += 500

            print("\nC уровня ", N1, " на уровень", N2)
            print("Необходимые ОХ:", oh)
            print("Получаемая грузоподъёмность:", s)
            print("Получаемая выносливость:", v)
        else:
            print("Вы ввели неправильные значения, попробуйте еще раз")


    elif (what_program == 2):
        N1 = int(input("Введите текущий уровень Интеллекта: "))
        N2 = int(input("Введите уровень, которого хотите достичь: "))
        if (N2 > N1):
            oh = 0
            mana = 0
            slots = 0
            s = 0
            v = 0

            for i in range(N1+1, N2+1):
                if (i % 5 != 0) and (i % 10 != 0) and (i % 50 != 0):
                    oh += 1
                    mana += 100
                    slots += 1
                elif (i % 10 != 0) and (i % 50 != 0):
                    oh += 2
                    mana += 200
                    slots += 2
                elif i % 50 != 0:
                    oh += 4
                    mana += 250
                    slots += 3
                else:
                    oh += 8
                    mana += 300
                    slots += 4

            print("\nC уровня ", N1, " на уровень", N2)
            print("Необходимые ОХ:", oh)
            print("Получаемая мана/ки:", mana)
            print("Получаемые ячейки:", slots, "\n\n")
        else:
            print("Вы ввели неправильные значения")

    elif (what_program == 3):
        N1 = int(input("Введите текущий уровень: "))
        N2 = int(input("Введите уровень, которого хотите достичь: "))
        if (N2 > N1):
            s = 0
            oh = 0

            for i in range(N1+1, N2+1):
                if (i % 5 != 0) and (i % 10 != 0) and (i % 50 != 0):
                    s += 100
                    oh += 1
                elif (i % 10 != 0) and (i % 50 != 0):
                    s += 250
                    oh += 3
                elif i % 50 != 0:
                    s += 500
                    oh += 5
                else:
                    s += 1000
                    oh += 10

            print("\nC уровня ", N1, " на уровень", N2)
            print("Необходимый опыт: ", s)
            print("Получаемые ОХ:", oh, "\n\n")
        else:
            print("Вы ввели неправильные значения")
    elif (what_program == 4):
        N1 = int(input("Введите текущий уровень: "))
        N2 = int(input("Введите имеющийся опыт: "))
        exp = N2
        level = N1
        if (exp > 100):
            level = N1 + 1
            oh = 0
            while (True):
                if (level % 5 != 0) and (level % 10 != 0) and (level % 50 != 0):
                    if (exp < 100):
                        break
                    exp -= 100
                    oh += 1
                elif (level % 10 != 0) and (level % 50 != 0):
                    if (exp < 250):
                        break
                    exp -= 250
                    oh += 3
                elif level % 50 != 0:
                    if (exp < 500):
                        break
                    exp -= 500
                    oh += 5
                else:
                    if (exp < 1000):
                        break
                    exp -= 1000
                    oh += 10
                level += 1
                print("На", level, "уровне тратится в общей сумме", N2 - exp, "опыта, получено в общей сумме", oh, "ОХ")
            print("\nЗа", N2, "опыта с", N1, "уровня можно подняться до", level, "уровня, получив", oh, "ОХ")
        else:
            print("Вам не хватает опыта для повышения уровня")
    elif (what_program == 5):
        N1 = int(input("Введите текущий уровень: "))
        N2 = int(input("Введите имеющиеся ОХ: "))
        oh = N2
        level = N1
        if (oh > 1) or (oh == 1):
            level += 1
        mana = 0
        slots = 0
        s = 0
        v = 0
        while (True):
            if (level % 5 != 0) and (level % 10 != 0) and (level % 50 != 0):
                if (oh < 1) or (oh == 0):
                    print("Остаток ОХ:", oh, ",больше уровней не повысить")
                    break
                oh -= 1
                mana += 100
                slots += 1
            elif (level % 10 != 0) and (level % 50 != 0):
                if (oh < 2):
                    print("Остаток ОХ:", oh, ",больше уровней не повысить")
                    break
                oh -= 2
                mana += 200
                slots += 2
            elif level % 50 != 0:
                if (oh < 4):
                    print("Остаток ОХ:", oh, ",больше уровней не повысить")
                    break
                oh -= 4
                mana += 250
                slots += 3
            else:
                if (oh < 8):
                    print("Остаток ОХ:", oh, ",больше уровней не повысить")
                    break
                oh -= 8
                mana += 300
                slots += 4
            print("На", level, "уровне тратится в общей сумме", N2 - oh, "ОХ, получено в общем", mana, "маны и", slots, "слотов")
            level += 1
        print("\nЗа", N2, "ОХ с", N1, "уровня можно подняться до", level, "уровня, получив", mana, " маны и ", slots, " слотов")