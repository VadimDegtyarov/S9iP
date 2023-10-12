import random

try:
    number = [random.randint(0, 1111111) for i in range(1, 11)]
    print(number)
except:
    print("Отсутствует модуль рандом")
finally:
    print("Блок try завершил выполнение")
