"""
Задание №5
✔ Напишите программу, которая решает квадратные уравнения даже если
дискриминант отрицательный.
✔ Используйте комплексные числа для извлечения квадратного корня.
"""

import math
import cmath

print('Введите значения коффициентов для квадратного уравнения ax2-bx-c=0')
a = int(input('a = '))
b = int(input('b = '))
c = int(input('c = '))
j = ''

discriminant = b ** 2 - 4 * a * c
print('Дискриминант D = ', discriminant)

if discriminant > 0:
    x1 = (-b + math.sqrt(discriminant)) / (2 * a)
    x2 = (-b - math.sqrt(discriminant)) / (2 * a)
    print('x1 =', round(x1, 3), '\n' 'x2 = ', round(x2, 3))

elif discriminant == 0:
    x = -b / (2 * a)
    print('x = ', round(x, 2))

else:

    x1 = (-b + cmath.sqrt(discriminant)) / (2 * a)
    x2 = (-b - cmath.sqrt(discriminant)) / (2 * a)
    print('x1 =', x1, '\n' 'x2 = ', x2)
