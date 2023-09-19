"""
Задание №2
Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и
знаменателем. Программа должна возвращать сумму и произведение* дробей.
Для проверки своего кода используйте модуль fractions.
"""

import fractions

print('Введите дроби в формате a/b: ')
f1 = input('f1 = ')
f2 = input('f2 = ')

f1_process = f1.split('/')
num1 = int(f1_process[0])
den1 = int(f1_process[1])

f2_process = f2.split('/')
num2 = int(f2_process[0])
den2 = int(f2_process[1])


summ = ((num1 * den2 + num2 * den1) / (den1 * den2))
mult = ((num1 * num2) / (den1 * den2))

print(summ)
print(mult)

# Check
f1_1 = fractions.Fraction(num1, den1)
f2_1 = fractions.Fraction(num2, den2)
print(format(f1_1 + f2_1))
print(format(f1_1 * f2_1))
