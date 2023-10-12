with open("Sessions.txt", 'r', encoding='utf-8') as Sessions:
    sses = Sessions.readlines()
    Dict = {}
    for el in sses:
        sl = ''
        summ = 0
        digits = []

        for el1 in range(len(el)):
            if el1 < el.index(':'):
                sl += el[el1]
            elif el[el1].isdigit():
                num_str = el[el1]
                while el[el1 + 1].isdigit():
                    el1 += 1
                    num_str += el[el1]
                digits.append(int(num_str))

        Dict[sl] = sum(digits)

    print(Dict)
