"""
Задание №2
Напишите программу, которая получает целое число и возвращает его шестнадцатеричное
строковое представление. Функцию hex используйте для проверки своего результата.
"""

num_dec = int(input('Введите число: '))
res = ''
compare_res = num_dec
print(hex(num_dec))
while num_dec > 0:
    if (num_dec % 16) < 10:
        res = str(num_dec % 16) + res
    else:
        if (num_dec % 16) == 10:
            res = 'a' + res
        elif (num_dec % 16) == 11:
            res = 'b' + res
        elif (num_dec % 16) == 12:
            res = 'c' + res
        elif (num_dec % 16) == 13:
            res = 'd' + res
        elif (num_dec % 16) == 14:
            res = 'e' + res
        elif (num_dec % 16) == 15:
            res = 'f' + res
    num_dec //= 16
print(res)
print('0x' + res)

if ('0x' + res) == str(hex(compare_res)):
    print(True)
