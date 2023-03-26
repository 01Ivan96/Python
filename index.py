import random

# Задача 30:  Заполните массив элементами арифметической прогрессии. Её первый элемент, разность и количество элементов нужно ввести с клавиатуры. Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.
# '''
firstElement = int(input("Первый элемент: "))
diff = int(input("Разность арифметической прогрессии: "))
amountElements = int(input("Количество элементов: "))

listNumbers = [ firstElement+diff*(i-1) for i in range(1, amountElements+1) ]

print(listNumbers)
# '''


# Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону (т.е. не меньше заданного минимума и не больше заданного максимума)
'''
amountElements = int(input("Количество элементов: "))
firstNumber = int(input("Минимальный элемент: "))
secondNumber = int(input("Максимальный элемент: "))

listNumbers = [ random.randint(0, 10) for i in range(amountElements) ]
print(listNumbers)

listIndex = [ i for i in range(len(listNumbers)) if firstNumber <= listNumbers[i] <= secondNumber ]
print(listIndex)
'''