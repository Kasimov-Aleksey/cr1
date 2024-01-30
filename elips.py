
data_x_and_y = []

x1 = int(input("Введите х1:   "))
y1 = int(input("Введите у1:   "))
# x2 = int(input("Введите х2:   "))
# y2 = int(input("Введите у2:   "))
mod = int(input("Введите mod:   "))
a = int(input("Введите a:   "))
data_x_and_y_new = []
max_porog_x = int(input("Введите max х:   "))
min_porog_x = int(input("Введите  min х:   "))
max_porog_y = int(input("Введите max y:   "))
min_porog_y = int(input("Введите  min y:   "))
print("      x      y                           ")
print(f"1P = ({float(x1)}, {float(y1)} )")
def sum_points(x1, y1, a, mod):
    bon = 0
    cheker = 3
##################################################
    bon = 0
    while True:
        cisl = (3 * x1 ** 2 + a) + bon
        c = cisl / (2 * y1)
        if c == int(c):
            break

        bon += mod
    data_1 = []
    x3 = c ** 2 - 2 * x1
    y3 = c * (x1 - x3) - y1
    while True:
        min = 1
        if x3 < 0:
            min = -1
        x3 = x3 - mod * (min)
        if min_porog_x <= x3 <= max_porog_x:
            break
    while True:
        min = 1
        if y3 < 0:
            min = -1
        y3 = y3 - mod * (min)
        if min_porog_y <= y3 <= max_porog_y:
            break


    data_1.append(str(x3))
    data_1.append(str(y3))
    x2, y2 = x3, y3

    print(f"2P = ({', '.join(data_1)})")
#################################################
    while True:
        data = []
        while True:

            cisl = (y2 - y1) + bon
            if cisl == 0 or (x2 - x1)==0:
                return data_x_and_y_new
            c = cisl / (x2 - x1)
            if c == int(c):
                break

            bon += mod

        x3 = c ** 2 - x1 - x2
        y3 = c * (x1 - x3) - y1
        while True:
            min = 1
            if x3 < 0:
                min = -1
            x3 = x3 - mod * (min)
            if min_porog_x <= x3 <= max_porog_x:
                break
        while True:
            min = 1
            if y3 < 0:
                min = -1
            y3 = y3 - mod * (min)
            if min_porog_y <= y3 <= max_porog_y:
                break
        data.append(str(x3))
        data.append(str(y3))

        data_x_and_y_new.append(data)
        print(f"{cheker}P = ({', '.join(data)})")
        x2, y2 = x3, y3
        cheker+=1
    return data_x_and_y_new


data_x_and_y_new = sum_points(x1, y1, a, mod)
# print(data_x_and_y_new)
