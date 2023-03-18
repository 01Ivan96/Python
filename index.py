import random

# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
# '''

lenList = int(input("Длина списка: "))
listNumbers = []
for i in range(lenList):
 listNumbers.append( random.randint(1, 10) )
print(listNumbers)

searchNumber = int(input("Число необходимое для поиска: "))

# 1 способ
countNumber = 0
for j in listNumbers:
 if j == searchNumber:
  countNumber += 1

# 2 способ
# countNumber = listNumbers.count(searchNumber)

print(countNumber)
# '''


# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
'''

lenList = int(input("Длина списка: "))
listNumbers = []
for i in range(lenList):
 listNumbers.append( random.randint(1, 10) )
print(listNumbers)

newNumber = int(input("Введите число: "))

flagLeft = False
if min(listNumbers) < newNumber:
 flagLeft = True
 possibleNumberLeft = min(listNumbers)

flagRight = False
if max(listNumbers) > newNumber:
 flagRight = True
 possibleNumberRight = max(listNumbers)


for j in listNumbers:
 if j < newNumber and ( newNumber - j < newNumber - possibleNumberLeft ):
  possibleNumberLeft = j
 elif j > newNumber and ( j - newNumber < possibleNumberRight - newNumber ):
  possibleNumberRight = j
 
if flagLeft and flagRight:
 print(f"{possibleNumberLeft}, {possibleNumberRight}")
elif flagLeft:
 print(f"{possibleNumberLeft}, а числа больше {newNumber} нет!")
elif flagRight:
 print(f"{possibleNumberRight}, а числа меньше {newNumber} нет!")
'''


# Задача 20: * В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность. В случае с английским алфавитом очки распределяются так:A, E, I, O, U, L, N, S, T, R – 1 очко; D, G – 2 очка; B, C, M, P – 3 очка; F, H, V, W, Y – 4 очка; K – 5 очков; J, X – 8 очков; Q, Z – 10 очков. А русские буквы оцениваются так: А, В, Е, И, Н, О, Р, С, Т – 1 очко; Д, К, Л, М, П, У – 2 очка; Б, Г, Ё, Ь, Я – 3 очка; Й, Ы – 4 очка; Ж, З, Х, Ц, Ч – 5 очков; Ш, Э, Ю – 8 очков; Ф, Щ, Ъ – 10 очков. Напишите программу, которая вычисляет стоимость введенного пользователем слова. Будем считать, что на вход подается только одно слово, которое содержит либо только английские, либо только русские буквы.
'''
priceChar = [
    [0, ' '],
    [1, 'АВЕИНОРСТAEIOULNSTR'],
    [2, 'ДКЛМПУDG'],
    [3, 'BCMPBCMP'],
    [4, 'ЙЫFHVWY'],
    [5, 'ЖЗХЦЧK'],
    [6, 'ШЭЮJX'],
    [7, 'ФЩЪQZ']
]

userWord = input("Введите одно слово: ").upper()

sumPoints = 0
for char in userWord:
    for indexItem in range(len(priceChar)):
        if char in priceChar[indexItem][1]:
            sumPoints += priceChar[indexItem][0]

print(sumPoints)
'''