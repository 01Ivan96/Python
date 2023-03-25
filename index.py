# Задача 26:  Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.
# '''
number = int(input("Основание степени: "))
degree = int(input("Степень числа: "))

def degreeOfNumber(number, degree):
    if degree != 1:
        return number * degreeOfNumber(number, degree - 1)
    return number

print(f"{number} ^ {degree} = {degreeOfNumber(number, degree)}")
# '''


# Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.
'''
firstNumber = int(input("Первое число: "))
secondNumber = int(input("Второе число: "))

def sumNumbers(number1, number2):
    if number2 == 0:
        return number1
    return 1 + sumNumbers(number1, number2 - 1)

print(sumNumbers(firstNumber, secondNumber))
'''