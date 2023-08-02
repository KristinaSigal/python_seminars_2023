"""
Задание №2
✔ Напишите функцию, которая принимает строку текста.
✔ Сформируйте список с уникальными кодами Unicode каждого
символа введённой строки отсортированный по убыванию.
"""


# def func(data):
#     res = sorted(list(set([ord(el) for el in data])), reverse=True)
#     return res
#
#
# data = input("Введите строку текста: ")
# print(func(data))

# Вариант 2

# def to_ord(string):
#     return sorted(set(map(ord, list(string))), reverse=True)
#
#
# to_ord = lambda x: sorted(set(map(ord, list(x))), reverse=True)
# print(to_ord('Карл у Клары украл коралы'))
#
# print(ord('a'))
# print(chr(99))


# Вариант 3

def unicod_text(text):

    new_spisok = set(text)
    spisok_res = []
    for item in new_spisok:
        spisok_res.append(ord(item))
    spisok_res.sort(reverse=True)
    return spisok_res


text = "Hello world. I teach python"
print(*unicod_text(text))
