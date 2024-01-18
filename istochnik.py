import random
import time

start_time = time.time()

number_of_descendants = 1250

list = [[0 for i in range(0,9)] for j in range(0,6)]
for i in range(0,6):
    for j in range(0,9):
        list[i][j] = i

def right_e_f(list):
    c = list[1][6]
    list[1][6] = list[1][8]
    list[1][8] = list[1][2]
    list[1][2] = list[1][0]
    list[1][0] = c

    c = list[1][7]
    list[1][7] = list[1][5]
    list[1][5] = list[1][1]
    list[1][1] = list[1][3]
    list[1][3] = c

    r = list[2][2]
    u = list[2][5]
    s = list[2][8]

    list[2][2] = list[0][2]
    list[2][5] = list[0][5]
    list[2][8] = list[0][8]

    list[0][2] = list[3][2]
    list[0][5] = list[3][5]
    list[0][8] = list[3][8]

    list[3][2] = list[5][6]
    list[3][5] = list[5][3]
    list[3][8] = list[5][0]

    list[5][0] = s
    list[5][3] = u
    list[5][6] = r
    return list

def right_e_b(list):
    c = list[1][2]
    list[1][2] = list[1][8]
    list[1][8] = list[1][6]
    list[1][6] = list[1][0]
    list[1][0] = c

    c = list[1][5]
    list[1][5] = list[1][7]
    list[1][7] = list[1][3]
    list[1][3] = list[1][1]
    list[1][1] = c

    r = list[5][0]
    u = list[5][3]
    s = list[5][6]

    list[5][6] = list[3][2]
    list[5][3] = list[3][5]
    list[5][0] = list[3][8]

    list[3][2] = list[0][2]
    list[3][5] = list[0][5]
    list[3][8] = list[0][8]

    list[0][2] = list[2][2]
    list[0][5] = list[2][5]
    list[0][8] = list[2][8]

    list[2][2] = s
    list[2][5] = u
    list[2][8] = r
    return list
def left_e_f(list):
    c = list[4][0]
    list[4][0] = list[4][2]
    list[4][2] = list[4][8]
    list[4][8] = list[4][6]
    list[4][6] = c

    c = list[4][3]
    list[4][3] = list[4][1]
    list[4][1] = list[4][5]
    list[4][5] = list[4][7]
    list[4][7] = c

    r = list[3][0]
    u = list[3][3]
    s = list[3][6]

    list[3][0] = list[5][8]
    list[3][3] = list[5][5]
    list[3][6] = list[5][2]

    list[5][8] = list[2][0]
    list[5][5] = list[2][3]
    list[5][2] = list[2][6]

    list[2][0] = list[0][0]
    list[2][3] = list[0][3]
    list[2][6] = list[0][6]

    list[0][0] = r
    list[0][3] = u
    list[0][6] = s

    return list

def left_e_b(list):
    c = list[4][6]
    list[4][6] = list[4][8]
    list[4][8] = list[4][2]
    list[4][2] = list[4][0]
    list[4][0] = c

    c = list[4][5]
    list[4][5] = list[4][1]
    list[4][1] = list[4][3]
    list[4][3] = list[4][7]
    list[4][7] = c

    r = list[0][0]
    u = list[0][3]
    s = list[0][6]

    list[0][0] = list[2][0]
    list[0][3] = list[2][3]
    list[0][6] = list[2][6]

    list[2][0] = list[5][8]
    list[2][3] = list[5][5]
    list[2][6] = list[5][2]

    list[5][8] = list[3][0]
    list[5][5] = list[3][3]
    list[5][2] = list[3][6]

    list[3][0] = r
    list[3][3] = u
    list[3][6] = s

    return list

def top_e_r(list):#поворот верхней грани вправо
    c = list[2][2]
    list[2][2] = list[2][8]
    list[2][8] = list[2][6]
    list[2][6] = list[2][0]
    list[2][0] = c

    c = list[2][5]
    list[2][5] = list[2][7]
    list[2][7] = list[2][3]
    list[2][3] = list[2][1]
    list[2][1] = c

    r = list[4][0]
    u = list[4][1]
    s = list[4][2]

    list[4][0] = list[5][0]
    list[4][1] = list[5][1]
    list[4][2] = list[5][2]

    list[5][0] = list[1][0]
    list[5][1] = list[1][1]
    list[5][2] = list[1][2]

    list[1][0] = list[0][0]
    list[1][1] = list[0][1]
    list[1][2] = list[0][2]

    list[0][0] = r
    list[0][1] = u
    list[0][2] = s
    return list

def top_e_l(list): #поворот верхней грани влево
    c = list[2][6]
    list[2][6] = list[2][8]
    list[2][8] = list[2][2]
    list[2][2] = list[2][0]
    list[2][0] = c

    c = list[2][7]
    list[2][7] = list[2][5]
    list[2][5] = list[2][1]
    list[2][1] = list[2][3]
    list[2][3] = c
    r = list[4][0]
    u = list[4][1]
    s = list[4][2]

    list[4][0] = list[0][0]
    list[4][1] = list[0][1]
    list[4][2] = list[0][2]

    list[0][0] = list[1][0]
    list[0][1] = list[1][1]
    list[0][2] = list[1][2]

    list[1][0] = list[5][0]
    list[1][1] = list[5][1]
    list[1][2] = list[5][2]

    list[5][0] = r
    list[5][1] = u
    list[5][2] = s
    return list

def bot_e_r(list):#поворот нижней грани вправо
    c = list[3][6]
    list[3][6] = list[3][8]
    list[3][8] = list[3][2]
    list[3][2] = list[3][0]
    list[3][0] = c

    c = list[3][7]
    list[3][7] = list[3][5]
    list[3][5] = list[3][1]
    list[3][1] = list[3][3]
    list[3][3] = c

    r = list[4][6]
    u = list[4][7]
    s = list[4][8]

    list[4][6] = list[5][6]
    list[4][7] = list[5][7]
    list[4][8] = list[5][8]

    list[5][6] = list[1][6]
    list[5][7] = list[1][7]
    list[5][8] = list[1][8]

    list[1][6] = list[0][6]
    list[1][7] = list[0][7]
    list[1][8] = list[0][8]

    list[0][6] = r
    list[0][7] = u
    list[0][8] = s
    return list
def bot_e_l(list): #поворот нижней грани влево
    c = list[3][2]
    list[3][2] = list[3][8]
    list[3][8] = list[3][6]
    list[3][6] = list[3][0]
    list[3][0] = c

    c = list[3][5]
    list[3][5] = list[3][7]
    list[3][7] = list[3][3]
    list[3][3] = list[3][1]
    list[3][1] = c

    r = list[4][6]
    u = list[4][7]
    s = list[4][8]

    list[4][6] = list[0][6]
    list[4][7] = list[0][7]
    list[4][8] = list[0][8]

    list[0][6] = list[1][6]
    list[0][7] = list[1][7]
    list[0][8] = list[1][8]

    list[1][6] = list[5][6]
    list[1][7] = list[5][7]
    list[1][8] = list[5][8]

    list[5][6] = r
    list[5][7] = u
    list[5][8] = s
    return list

def front_e_r(list): #поворот фронтальной грани вправо
    c = list[0][6]
    list[0][6] = list[0][8]
    list[0][8] = list[0][2]
    list[0][2] = list[0][0]
    list[0][0] = c

    c = list[0][7]
    list[0][7] = list[0][5]
    list[0][5] = list[0][1]
    list[0][1] = list[0][3]
    list[0][3] = c

    r = list[4][2]
    u = list[4][5]
    s = list[4][8]

    list[4][2] = list[3][0]
    list[4][5] = list[3][1]
    list[4][8] = list[3][2]

    list[3][0] = list[1][6]
    list[3][1] = list[1][3]
    list[3][2] = list[1][0]

    list[1][0] = list[2][6]
    list[1][3] = list[2][7]
    list[1][6] = list[2][8]

    list[2][6] = s
    list[2][7] = u
    list[2][8] = r
    return list

def front_e_l(list): #поворот фронтальной грани влево
    c = list[0][2]
    list[0][2] = list[0][8]
    list[0][8] = list[0][6]
    list[0][6] = list[0][0]
    list[0][0] = c

    c = list[0][5]
    list[0][5] = list[0][7]
    list[0][7] = list[0][3]
    list[0][3] = list[0][1]
    list[0][1] = c

    r = list[4][2]
    u = list[4][5]
    s = list[4][8]

    list[4][2] = list[2][8]
    list[4][5] = list[2][7]
    list[4][8] = list[2][6]

    list[2][6] = list[1][0]
    list[2][7] = list[1][3]
    list[2][8] = list[1][6]

    list[1][0] = list[3][2]
    list[1][3] = list[3][1]
    list[1][6] = list[3][0]

    list[3][0] = r
    list[3][1] = u
    list[3][2] = s
    return list

def back_e_r(list): #поворот задней грани вправо
    c = list[5][3]
    list[5][3] = list[5][1]
    list[5][1] = list[5][5]
    list[5][5] = list[5][7]
    list[5][7] = c

    c = list[5][8]
    list[5][8] = list[5][6]
    list[5][6] = list[5][0]
    list[5][0] = list[5][2]
    list[5][2] = c

    r = list[3][6]
    u = list[3][7]
    s = list[3][8]

    list[3][6] = list[1][8]
    list[3][7] = list[1][5]
    list[3][8] = list[1][2]

    list[1][2] = list[2][0]
    list[1][5] = list[2][1]
    list[1][8] = list[2][2]

    list[2][0] = list[4][6]
    list[2][1] = list[4][3]
    list[2][2] = list[4][0]

    list[4][0] = r
    list[4][3] = u
    list[4][6] = s
    return list

def back_e_l(list): #поворот задней грани влево
    c = list[5][1]
    list[5][1] = list[5][3]
    list[5][3] = list[5][7]
    list[5][7] = list[5][5]
    list[5][5] = c

    c = list[5][6]
    list[5][6] = list[5][8]
    list[5][8] = list[5][2]
    list[5][2] = list[5][0]
    list[5][0] = c

    r = list[2][0]
    u = list[2][1]
    s = list[2][2]
    list[2][0] = list[1][2]
    list[2][1] = list[1][5]
    list[2][2] = list[1][8]

    list[1][2] = list[3][8]
    list[1][5] = list[3][7]
    list[1][8] = list[3][6]

    list[3][6] = list[4][0]
    list[3][7] = list[4][3]
    list[3][8] = list[4][6]

    list[4][0] = s
    list[4][3] = u
    list[4][6] = r
    return list

def centre_e_r(list):
    r = list[0][3]
    u = list[0][4]
    s = list[0][5]
    list[0][3] = list[4][3]
    list[0][4] = list[4][4]
    list[0][5] = list[4][5]

    list[4][3] = list[5][3]
    list[4][4] = list[5][4]
    list[4][5] = list[5][5]

    list[5][3] = list[1][3]
    list[5][4] = list[1][4]
    list[5][5] = list[1][5]

    list[1][3] = r
    list[1][4] = u
    list[1][5] = s

def centre_e_l(list):
    r = list[4][3]
    u = list[4][4]
    s = list[4][5]
    list[4][3] = list[0][3]
    list[4][4] = list[0][4]
    list[4][5] = list[0][5]

    list[0][3] = list[1][3]
    list[0][4] = list[1][4]
    list[0][5] = list[1][5]

    list[1][3] = list[5][3]
    list[1][4] = list[5][4]
    list[1][5] = list[5][5]

    list[5][3] = r
    list[5][4] = u
    list[5][5] = s

def diff0(list):
    summa = 0
    for i in range(0,9):
        if i == 0 or i == 2 or i == 6 or i == 8:
            continue
        if list[3][i] == 3:
            summa += 1
    for i in range(0,6):
        if i == 2 or i == 3:
            continue
        if list[i][7] == list[i][4]:
            summa += 1
    return summa + 5
def diff1(list):
    summa = 0
    for i in range(0,9):
        if list[3][i] == 3:
            summa += 1
    for i in range(0,6):
        if i == 2 or i == 3:
            continue
        if list[i][6] == list[i][4]:
            summa += 1
        if list[i][7] == list[i][4]:
            summa += 1
        if list[i][8] == list[i][4]:
            summa += 1
    return summa + 5

def diff2(list):
    summa = 0
    for i in range(0,9):
        if list[3][i] == 3:
            summa += 1
    for i in range(0,6):
        if i == 2 or i == 3:
            continue
        if list[i][6] == list[i][4]:
            summa += 1
        if list[i][7] == list[i][4]:
            summa += 1
        if list[i][8] == list[i][4]:
            summa += 1
        if list[i][3] == list[i][4]:
            summa += 1
        if list[i][5] == list[i][4]:
            summa += 1
    return summa + 5

def diff3(list):
    summa = 0
    for i in range(0,9):
        if list[3][i] == 3:
            summa += 1
    for i in range(0,6):
        if i == 2 or i == 3:
            continue
        if list[i][6] == list[i][4]:
            summa += 1
        if list[i][7] == list[i][4]:
            summa += 1
        if list[i][8] == list[i][4]:
            summa += 1
        if list[i][3] == list[i][4]:
            summa += 1
        if list[i][5] == list[i][4]:
            summa += 1
    for i in range(0,9):
        if i == 0 or i == 2 or i == 4 or i == 6 or i == 8:
            continue
        if list[2][i] == 2:
            summa += 1
    return summa + 5

def diff4(list):
    summa = 0
    for i in range(0,9):
        if list[3][i] == 3:
            summa += 1
    for i in range(0,6):
        if i == 2 or i == 3:
            continue
        if list[i][6] == list[i][4]:
            summa += 1
        if list[i][7] == list[i][4]:
            summa += 1
        if list[i][8] == list[i][4]:
            summa += 1
        if list[i][3] == list[i][4]:
            summa += 1
        if list[i][5] == list[i][4]:
            summa += 1
        if list[i][1] == list[i][4]:
            summa += 1
    for i in range(0,9):
        if i == 0 or i == 2 or i == 4 or i == 6 or i == 8:
            continue
        if list[2][i] == 2:
            summa += 1
    return summa + 5

def diff5(list):
    summa = 0
    for i in range(0,9):
        if list[3][i] == 3:
            summa += 1
    for i in range(0,6):
        if i == 2 or i == 3:
            continue
        if list[i][6] == list[i][4]:
            summa += 1
        if list[i][7] == list[i][4]:
            summa += 1
        if list[i][8] == list[i][4]:
            summa += 1
        if list[i][3] == list[i][4]:
            summa += 1
        if list[i][5] == list[i][4]:
            summa += 1
        if list[i][1] == list[i][4]:
            summa += 1
    for i in range(0,9):
        if i == 0 or i == 2 or i == 4 or i == 6 or i == 8:
            continue
        if list[2][i] == 2:
            summa += 1
    if (list[0][2] == list[0][4] or list[0][2] == list[2][4] or list[0][2] == list[1][4]) \
        and (list[2][8] == list[0][4] or list[2][8] == list[2][4] or list[2][8] == list[1][4]) \
        and (list[1][0] == list[0][4] or list[1][0] == list[2][4] or list[1][0] == list[1][4]):
        summa += 1
    if (list[0][0] == list[0][4] or list[0][0] == list[4][4] or list[0][0] == list[2][4]) \
        and (list[2][6] == list[0][4] or list[2][6] == list[4][4] or list[2][6] == list[2][4])\
        and (list[4][2] == list[0][4] or list[4][2] == list[4][4] or list[4][2] == list[2][4]):
        summa += 1
    if (list[4][0] == list[4][4] or list[4][0] == list[2][4] or list[4][0] == list[5][4])\
        and (list[5][2] == list[4][4] or list[5][2] == list[2][4] or list[5][2] == list[5][4])\
        and (list[2][0] == list[4][4] or list[2][0] == list[2][4] or list[2][0] == list[5][4]):
        summa += 1
    if (list[1][2] == list[1][4] or list[1][2] == list[2][4] or list[1][2] == list[5][4])\
        and (list[2][2] == list[1][4] or list[2][2] == list[2][4] or list[2][2] == list[5][4]) \
        and (list[5][0] == list[1][4] or list[5][0] == list[2][4] or list[5][0] == list[5][4]):
        summa += 1

    return summa + 5
def diff6(list): #Критерий близости решения
    summa = 0
    for i in range(0, 6):
        for j in range(0,9):
            if list[i][4] == list[i][j]:
                summa += 1
    return summa

functions = [top_e_l, top_e_r]
functions1 =[top_e_l, top_e_r, front_e_r, front_e_l, right_e_f, right_e_b, left_e_f, left_e_b,bot_e_r,bot_e_l, back_e_r,back_e_l]
permutations = [[front_e_r], [right_e_f], [top_e_r], [left_e_f], [centre_e_r, bot_e_r, top_e_r], [bot_e_r]]
permutations1 = [[top_e_r], [centre_e_r, bot_e_r, top_e_r], [right_e_f, top_e_l, right_e_b,top_e_r]]
permutations2 = [[top_e_l],[centre_e_r, bot_e_r, top_e_r],[top_e_r, left_e_f, top_e_l, left_e_b, front_e_l, left_e_b, front_e_r,left_e_f],[top_e_l, right_e_f, top_e_r, right_e_b, front_e_r, right_e_b, front_e_l,right_e_f]]
permutations3 = [[front_e_r, right_e_f, top_e_l, right_e_b, top_e_r, front_e_l], [top_e_r]]
permutations4 = [[right_e_f, top_e_l, right_e_b, top_e_l, right_e_f, top_e_l, top_e_l, right_e_b], [top_e_l]]
permutations5 = [[top_e_r, left_e_f, top_e_l, right_e_f, top_e_r, left_e_b, top_e_l, right_e_b], [centre_e_r, bot_e_r, top_e_r]]
permutations6 = [[top_e_l],[right_e_b, bot_e_l, right_e_f,bot_e_r,right_e_b, bot_e_l, right_e_f,bot_e_r]]
# Создаем пустой двумерный массив
combined_list = []

def absolutely_new_generation():
    for i in range(number_of_descendants):
        # Создаем пустой список функций
        inner_list = []

        # Проходим по циклу для формирования внутреннего списка функций
        for j in range(1):
            # Создаем функцию
            func = random.choice(functions)

            # Добавляем функцию во внутренний список
            inner_list.append(func)
            inner_list.clear()

        # Добавляем внутренний список в основной двумерный массив
        combined_list.append(inner_list)
def transformation(end_decision):
    str = ""
    str1 = ""
    str2 = ""
    str3 = ""
    str4 = ""
    for i in range(0,min(60, len(end_decision))):
        if end_decision[i].__name__ == "back_e_l":
            str += "B "
        if end_decision[i].__name__ == "back_e_r":
            str += "B' "
        if end_decision[i].__name__ == "right_e_b":
            str += "R' "
        if end_decision[i].__name__ == "right_e_f":
            str += "R "
        if end_decision[i].__name__ == "bot_e_l":
            str += "D' "
        if end_decision[i].__name__ == "bot_e_r":
            str += "D "
        if end_decision[i].__name__ == "top_e_r":
            str += "U' "
        if end_decision[i].__name__ == "front_e_r":
            str += "F "
        if end_decision[i].__name__ == "front_e_l":
            str += "F' "
        if end_decision[i].__name__ == "top_e_l":
            str += "U "
        if end_decision[i].__name__ == "left_e_b":
            str += "L "
        if end_decision[i].__name__ == "left_e_f":
            str += "L' "
        if end_decision[i].__name__ == "centre_e_r":
            str += "E "
    for i in range(60,min(120, len(end_decision))):
        if end_decision[i].__name__ == "back_e_l":
            str1 += "B "
        if end_decision[i].__name__ == "back_e_r":
            str1 += "B' "
        if end_decision[i].__name__ == "right_e_b":
            str1 += "R' "
        if end_decision[i].__name__ == "right_e_f":
            str1 += "R "
        if end_decision[i].__name__ == "bot_e_l":
            str1 += "D' "
        if end_decision[i].__name__ == "bot_e_r":
            str1 += "D "
        if end_decision[i].__name__ == "top_e_r":
            str1 += "U' "
        if end_decision[i].__name__ == "front_e_r":
            str1 += "F "
        if end_decision[i].__name__ == "front_e_l":
            str1 += "F' "
        if end_decision[i].__name__ == "top_e_l":
            str1 += "U "
        if end_decision[i].__name__ == "left_e_b":
            str1 += "L "
        if end_decision[i].__name__ == "left_e_f":
            str1 += "L' "
        if end_decision[i].__name__ == "centre_e_r":
            str1 += "E "
    for i in range(120,min(180, len(end_decision))):
        if end_decision[i].__name__ == "back_e_l":
            str2 += "B "
        if end_decision[i].__name__ == "back_e_r":
            str2 += "B' "
        if end_decision[i].__name__ == "right_e_b":
            str2 += "R' "
        if end_decision[i].__name__ == "right_e_f":
            str2 += "R "
        if end_decision[i].__name__ == "bot_e_l":
            str2 += "D' "
        if end_decision[i].__name__ == "bot_e_r":
            str2 += "D "
        if end_decision[i].__name__ == "top_e_r":
            str2 += "U' "
        if end_decision[i].__name__ == "front_e_r":
            str2 += "F "
        if end_decision[i].__name__ == "front_e_l":
            str2 += "F' "
        if end_decision[i].__name__ == "top_e_l":
            str2 += "U "
        if end_decision[i].__name__ == "left_e_b":
            str2 += "L "
        if end_decision[i].__name__ == "left_e_f":
            str2 += "L' "
        if end_decision[i].__name__ == "centre_e_r":
            str2 += "E "
    for i in range(180,min(240, len(end_decision))):
        if end_decision[i].__name__ == "back_e_l":
            str3 += "B "
        if end_decision[i].__name__ == "back_e_r":
            str3 += "B' "
        if end_decision[i].__name__ == "right_e_b":
            str3 += "R' "
        if end_decision[i].__name__ == "right_e_f":
            str3 += "R "
        if end_decision[i].__name__ == "bot_e_l":
            str3 += "D' "
        if end_decision[i].__name__ == "bot_e_r":
            str3 += "D "
        if end_decision[i].__name__ == "top_e_r":
            str3 += "U' "
        if end_decision[i].__name__ == "front_e_r":
            str3 += "F "
        if end_decision[i].__name__ == "front_e_l":
            str3 += "F' "
        if end_decision[i].__name__ == "top_e_l":
            str3 += "U "
        if end_decision[i].__name__ == "left_e_b":
            str3 += "L "
        if end_decision[i].__name__ == "left_e_f":
            str3 += "L' "
        if end_decision[i].__name__ == "centre_e_r":
            str3 += "E "
    for i in range(240,min(300, len(end_decision))):
        if end_decision[i].__name__ == "back_e_l":
            str4 += "B "
        if end_decision[i].__name__ == "back_e_r":
            str4 += "B' "
        if end_decision[i].__name__ == "right_e_b":
            str4 += "R' "
        if end_decision[i].__name__ == "right_e_f":
            str4 += "R "
        if end_decision[i].__name__ == "bot_e_l":
            str4 += "D' "
        if end_decision[i].__name__ == "bot_e_r":
            str4 += "D "
        if end_decision[i].__name__ == "top_e_r":
            str4 += "U' "
        if end_decision[i].__name__ == "front_e_r":
            str4 += "F "
        if end_decision[i].__name__ == "front_e_l":
            str4 += "F' "
        if end_decision[i].__name__ == "top_e_l":
            str4 += "U "
        if end_decision[i].__name__ == "left_e_b":
            str4 += "L "
        if end_decision[i].__name__ == "left_e_f":
            str4 += "L' "
        if end_decision[i].__name__ == "centre_e_r":
            str4 += "E "
    return str, str1, str2, str3, str4

end_decision = []
list1 = [[0 for i in range(0, 9)] for j in range(0,6)]

funcs = [diff0, diff1, diff2, diff3, diff4, diff5, diff6]
numbers = [14,26,34,38,42,46,54]

# Выбор лучших
def best(list, combined_list,l):
    global list1
    summa1 = [0]*number_of_descendants
    c = 0
    for i in range(0, number_of_descendants):
        for f in range(0, len(list)):
            for j in range(0, len(list[f])):
                list[f][j] = list1[f][j]
        for j in range(len(end_decision), len(combined_list[i])):
            combined_list[i][j](list)
            d = funcs[l](list)
            c = numbers[l] - d
            if c == 0 and j == len(combined_list[i]) - 1:
                end_decision.clear()
                end_decision.extend(combined_list[i])
                print(list)
                for b in range(0,number_of_descendants):
                    if b == i:
                        continue
                    combined_list[b].clear()
                    for m in range(0, len(combined_list[i])):
                        combined_list[b].append(combined_list[i][m])
                for f in range(0, len(list)):
                    for e in range(0, len(list[f])):
                        list1[f][e] = list[f][e]
                return 0
        summa1[i] = c
    combined_list = sorted(combined_list, key=lambda x: summa1[combined_list.index(x)])
    if l != 6:
        for i in range(556, number_of_descendants-100):
            combined_list[i].clear()
            u = random.randint(0,555)
            for j in range(0, len(combined_list[u])):
                combined_list[i].append(combined_list[u][j])
    for f in range(0, len(list)):
        for j in range(0, len(list[f])):
            list[f][j] = list1[f][j]
    return 1

def reborn():
    for i in range(0,number_of_descendants):
        combined_list[i] = combined_list[i][:len(end_decision)]

clown = ""
clown1 = ""
clown2 = ""
clown3 = ""
clown4 = ""
importantclown = []
def decision():
    absolutely_new_generation()
    global clown, clown1, clown2, clown3, clown4
    global list1
    for i in range(0, len(list)):
        for j in range(0, len(list[i])):
            list1[i][j] = list[i][j]
    y = 1
    z = 0
    count_generation = 30
    if diff0(list)<14:
        for i in range(0, number_of_descendants):
            combined_list[i].extend(random.choice(permutations))
        while best(list, combined_list, y - 1) != 0:
            z = z + 1
            if z == count_generation:
                reborn()
                z = 0
            else:
                for i in range(0,number_of_descendants):
                    combined_list[i].extend(random.choice(permutations))
    z = 0
    if diff1(list)<26:
        for i in range(0, number_of_descendants):
            combined_list[i].extend(random.choice(permutations1))
        while best(list, combined_list, y) != 0:
            z = z + 1
            if z == count_generation:
                reborn()
                z = 0
            else:
                for i in range(0, number_of_descendants):
                    combined_list[i].extend(random.choice(permutations1))
    z = 0
    if diff2(list)<34:
        for i in range(0, number_of_descendants):
            combined_list[i].extend(random.choice(permutations2))
        while best(list, combined_list, y + 1) != 0:
            z = z + 1
            if z == count_generation:
                reborn()
                z = 0
            else:
                for i in range(0, number_of_descendants):
                    combined_list[i].extend(random.choice(permutations2))
    z = 0
    if diff3(list) < 38:
        for i in range(0, number_of_descendants):
            combined_list[i].extend(random.choice(permutations3))
        while best(list, combined_list, y + 2) != 0:
            z = z + 1
            if z == count_generation:
                reborn()
                z = 0
            else:
                for i in range(0, number_of_descendants):
                    combined_list[i].extend(random.choice(permutations3))
    z = 0
    if diff4(list) < 42:
        for i in range(0, number_of_descendants):
            combined_list[i].extend(random.choice(permutations4))
        while best(list, combined_list, y + 3) != 0:
            z = z + 1
            if z == count_generation:
                reborn()
                z = 0
            else:
                for i in range(0, number_of_descendants):
                    combined_list[i].extend(random.choice(permutations4))
    z = 0
    if diff5(list) < 46:
        for i in range(0, number_of_descendants):
            combined_list[i].extend(random.choice(permutations5))
        while best(list, combined_list, y + 4) != 0:
            z = z + 1
            if z == count_generation:
                reborn()
                z = 0
            else:
                for i in range(0, number_of_descendants):
                    combined_list[i].extend(random.choice(permutations5))
    z = 0
    if diff6(list) < 54:
        for i in range(0, number_of_descendants):
            combined_list[i].extend(random.choice(permutations6))
        while best(list, combined_list, y + 5) != 0:
            z = z + 1
            if z == count_generation:
                reborn()
                z = 0
            else:
                for i in range(0, number_of_descendants):
                    combined_list[i].extend(random.choice(permutations6))
    for i in range(0, len(list)):
        for j in range(0, len(list[i])):
            list1[i][j] = list[i][j]
    clown, clown1, clown2, clown3, clown4 = transformation(end_decision)
    importantclown = end_decision.copy()

end_time = time.time()
execution_time = end_time - start_time
print("Время выполнения программы:", execution_time, "секунд")