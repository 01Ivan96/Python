import random

# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной. Выведите минимальное количество монет, которые нужно перевернуть
# '''
numberCoins = int(input("Кол-во монет: "))

arrayCoins = []
for i in range(numberCoins):
    arrayCoins.append(random.randint(0, 1))
print(arrayCoins)

countEagles = 0
countTails = 0
for j in arrayCoins:
    if j == 0:
        countEagles += 1
    else:
        countTails += 1

if countEagles < countTails:
    print(f"Переверните {countEagles} орлов!")
elif countEagles > countTails:
    print(f"Переверните {countTails} решек!")
else:
    print(f"Можете перевернуть как орлов, так и решек: {countTails}!")
# '''


# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.
'''
numberX = random.randint(0, 1000)
numberY = random.randint(0, 1000)
if numberX > numberY:
    newNumber = numberX
    numberX = numberY
    numberY = newNumber

print(f"Сумма чисел: {numberX + numberY}\nПроизведение чисел: {numberX * numberY}")

answerX = int(input("Какое первое число загадал Петя (оно должно быть <= второго): "))
answerY = int(input("Какое второе число загадано Петей: "))

if answerX == numberX and answerY == numberY:
    print("Верно!")
else:
    print(f"Правильный ответ: {numberX}, {numberY}")
'''



# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.
'''
number = int(input("Введите натуральное число: "))

i = 0
while 2 ** i <= number:
    print(2 ** i, end="  ")
    i += 1
'''