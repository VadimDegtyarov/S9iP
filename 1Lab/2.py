str = input("Введите строку: ")
ch = 0
upreg = 0
CH = 0
lowreg = 0
if int(str.isalpha()):
    for el in str:

        if el.istitle():
            ch += 1
            CH = 0
            if (ch == 2):
                upreg += 1
                ch = 0
        else:
            ch = 0
            CH += 1
            if (CH == 2):
                lowreg += 1
                CH = 0

else:
    print("Неверно введена строка")
    exit()

print(f"Нижний: {lowreg},верхний: {upreg}")
