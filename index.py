# Задача 2: Найдите сумму цифр трехзначного числа.

number = 0
while number < 100 or number > 999:
    number = int(input("Введите целое трёхзначное число: "))
sum = 0

# 1 способ
newnumber = number
while newnumber > 0:
    sum += newnumber % 10
    newnumber //= 10
print(sum)
'''
# 2 способ
strNumber = str(number)
for i in strNumber:
    sum += int(i)
print(sum)
'''

# Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов. Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали одинаковое количество журавликов, а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?
'''
number = 2
while number % 3 != 0:
    number = int(input("Общее количество поделок (кратное 3): "))
numberCraftsBoys = number // 6
numberCraftsGirl = number - 2 * numberCraftsBoys

print(f"Петя - {numberCraftsBoys}; Катя - {numberCraftsGirl}; Серёжа - {numberCraftsBoys}")
'''

# Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером. Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех. Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая проверяет счастливость билета.
'''
number = 0
while number < 100000 or number > 999999:
    number = int(input("Введите целое шестизначное число: "))
sum1 = 0
sum2 = 0

firstHalfNumber = str( number // 1000 )
secondHalfNumber = str( number % 1000 )

for i in firstHalfNumber:
    sum1 += int(i)
for j in secondHalfNumber:
    sum2 += int(j)

if sum1 == sum2:
    print("Yes")
else:
    print("No")
'''

# Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).
'''
print("Кол-во долек шоколадки по длине и ширине: ")
rows = int(input())
columns = int(input())

numberSlices = int(input("Количество долек за один разлом: "))

if numberSlices % rows == 0 or numberSlices % columns == 0:
    print("Yes")
else:
    print("No")
'''