def arg(value):
    if isinstance(value, tuple):
        summ = ''
        for el in value:
            summ = summ + el
        print(len(summ))

    elif isinstance(value, list):
        summ = 0
        boolok = False
        for el in value:
            if isinstance(el, int):
                el = int(el)
                if el < 0:
                    boolok = True
                if boolok:
                    summ = summ + el
        print(summ)

    elif isinstance(value, int):
        i = 0
        for el in str(value):
            if int(el) % 2 == 0:
                i = i + int(el)
        print(i)
    elif isinstance(value, str):
        numbers = [int(word) for word in value if word.isdigit()]
        summ = sum(numbers)
        print(summ)


value1 = ("apple", "banana", "cherry")
arg(value1)
value2 = [1, 2, 3, -1, 2, 4, 6, 8, 9, 'sad', 'asdg']
arg(value2)
value3 = 24686420
arg(value3)
value4 = "The price is 1234"
arg(value4)
