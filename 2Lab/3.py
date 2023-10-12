import random


def my_arr(n, m, i, j):
    arr = [[random.randint(0, 10) for el in range(0, m)] for elem in range(0, n)]
    for el1 in arr:
        print(el1)
    print("\n")
    for element in arr:
        str1 = 0
        if i and j > 0:
            str1 = element[i - 1]
            element[i - 1] = element[j - 1]
            element[j - 1] = str1
        else:
            str1 = element[i]
            element[i] = element[j]
            element[j] = str1

    for el2 in arr:
        print(el2)


n = int(input("Введите количество строк"))
m = int(input("Введите количество столбцов"))
i = int(input("Введите 1 стролбец"))
j = int(input("Введите 2 стролбец"))
if n or m or i or j < 0:
    exit("ошибка")
my_arr(n, m, i, j)
