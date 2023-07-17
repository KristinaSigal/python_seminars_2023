"""Решите квадратное уравнение 5x2-10x-400=0
последовательно сохраняя переменные a, b, c, d, x1 и x2.
*Попробуйте решить уравнения с другими значениями a, b, c.
"""
import math

print('Введите значения коффициентов для квадратного уравнения ax2-bx-c=0')
a = int(input('a = '))
b = int(input('b = '))
c = int(input('c = '))

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
    print("В квадратном уравнении 5x2-10x-400=0 корней нет")
