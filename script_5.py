"""Посчитайте сумму чётных элементов от 1 до n исключая кратные e.
Используйте while и if.
Попробуйте разные значения e и n."""

n = int(input('Введите n: '))
e = int(input('Введите e: '))
total = 0
i = 2
while i <= n:
    if i % e != 0:
        total += i
    i += 2
print(total)