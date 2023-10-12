with open("F1.txt", 'w') as F1:
    n = input("Введите значение n: ")
    k = input("Введите значение k: ")
    if n.isdigit() and k.isdigit():
        n = int(n)
        k = int(k)
    else:
        print("n and k должны ыть числами")
        exit()
    arrline = []
    while True:
        data = input("Введите данные в файл F1: ")
        if (data == ""):
            break
        F1.write(data)
        F1.write('\n')

with open("F1.txt", 'r') as F1:
    lines = F1.readlines()
    for i in range(n, k + 1):
        arrline.append(lines[i])

with open("F2.txt", 'w') as F2:
    for el in arrline:
        F2.write(el)
with open("F2.txt", 'r') as F2:
    lines = F2.readlines()
    Num = 0
    for el in range(len(lines)):
        lines[el] = lines[el].strip()
        for el1 in lines[el]:
            if el1 not in ('A', 'E', 'I', 'O', 'U', 'Y', 'a', 'e', 'i', 'o', 'u', 'y') and el1.isalpha():
                Num += 1
                print(el1, Num)
