"""
Задание №4
✔ Функция получает на вход список чисел.
✔ Отсортируйте  список по убыванию суммы числе
"""

# def get_sum(num: int):
#     return sum(map(int, str(num)))
#
# lst = [75, 61, 80, 19, 16, 1]
# print(sorted(lst, key=get_sum, reverse=True))


# Вариант2

def func(list_numbers):
    dict_num = {}
    for item in list_numbers:
        dict_num[item] = sum(map(int, str(item)))
    dict_result = sorted(dict_num, key=lambda x: dict_num[x], reverse=True)
    return dict_result

print(func([29, 43, 66, 84]))
