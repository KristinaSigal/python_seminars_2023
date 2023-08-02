"""
Задание №3
✔ Функция получает на вход строку из двух чисел через пробел.
✔ Сформируйте словарь, где ключом будет
символ из Unicode, а значением — целое число.
✔ Диапазон пар ключ-значение от наименьшего из введённых
пользователем чисел до наибольшего включительно.
"""


def func(data):
    dct = {chr(int(el)): el for el in sorted(data.split())}
    return dct


print(func('1 4 3'))

# Вариант 2

def create_dict(string_numbers):
    limit_1 = int(string_numbers.split()[0])
    limit_2 = int(string_numbers.split()[1])
    dict_numbers = {}
    for i in range(limit_1, limit_2 + 1):
        dict_numbers[chr(i)] = i
    return dict_numbers


input_data = input('Введите значения: ')
print(create_dict(input_data))
