"""
Задание №4
✔ Функция получает на вход список чисел.
✔ Отсортируйте его элементы in place без использования встроенных в язык сортировок.
✔ Как вариант напишите сортировку пузырьком. Её описание есть в википедии.
"""


# from random import randint
#
#
# def bubble_sort(lst_obj):
#     n = 1
#     while n < len(lst_obj):
#         for i in range(len(lst_obj) - n):
#             if lst_obj[i] > lst_obj[i + 1]:
#                 lst_obj[i], lst_obj[i + 1] = lst_obj[i + 1], lst_obj[i]
#         n += 1
#     return lst_obj
#
#
# orig_list = [randint(-100, 100) for _ in range(10)]
# print(bubble_sort(orig_list))


def sort_(list_numbers):
    for i, item_i in enumerate(list_numbers):
        for j in range(i, len(list_numbers)):
            if item_i > list_numbers[j]:
                list_numbers[i], list_numbers[j] = list_numbers[j], list_numbers[i]


list_num = [5, 6, 1, -8, 0]
print(list_num)
sort_(list_num)
print(list_num)
