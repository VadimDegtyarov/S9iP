import random

with open("Students.txt", 'w') as Students:
    for i in range(10):
        # data = input("Введите данные студента")
        data = ""
        GPA = [0]
        for l in range(6):
            data += str(random.randint(1, 10))
            data += ' '
        data1 = ''
        for el in range(2, len(data)):
            if data[el] != ' ':
                data1 = data.strip()
                GPA.append(int(data1[el]))

        print(GPA)
        GPAfin = 0
        for el in GPA:
            GPAfin += el
        if 6 > (GPAfin/5):
            print(GPAfin/5)


        Students.write(data)
        Students.write('\n')
