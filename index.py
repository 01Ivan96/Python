import random

def creatingList(lenList):
    listNumbers = []
    for i in range(lenList):
        listNumbers.append( random.randint(1, 10) )
    print(listNumbers)
    return listNumbers

# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# '''
lenFirstList = int(input("Длина первого списка: "))
lenSecondList = int(input("Длина второго списка: "))

firstListNumbers = creatingList(lenFirstList)
secondListNumbers = creatingList(lenSecondList)

# 1 способ
newList = []
for i in firstListNumbers:
    if i in secondListNumbers and i not in newList:
        newList.append(i)

# 2 способ
# newSet = set(firstListNumbers) & set(secondListNumbers)
# newList = list(newSet)


newList.sort()
print(newList)
# '''


# Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. Она растет на круглой грядке, причем кусты высажены только по окружности. Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растет N кустов.
# Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло различное число ягод – на i-ом кусте выросло ai ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники. Эта система состоит из управляющего модуля и нескольких собирающих модулей. Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом, собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, которое может собрать за один заход собирающий модуль, находясь перед некоторым кустом заданной во входном файле грядки.

'''
numberBushes = int(input("Количество кустов (более 2): "))

print("\nСписок количества ягод на кустах:")
listNumberBerries = creatingList(numberBushes)

# Последний куст считаем отдельно, т.к. при проходе по for будет происходить выход за длину списка (последний индекс + 1)
maxSumBerries = listNumberBerries[-2] + listNumberBerries[-1] + listNumberBerries[0]
for i in range(len(listNumberBerries)-1):
    sumAroundBush = listNumberBerries[i-1] + listNumberBerries[i] + listNumberBerries[i+1]
    if sumAroundBush > maxSumBerries:
        maxSumBerries = sumAroundBush

print(maxSumBerries)
'''