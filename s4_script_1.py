"""
Задание №1
Погружение в Python | Функции
✔ Напишите функцию, которая принимает строку текста.
Вывести функцией каждое слово с новой строки.
✔ Строки нумеруются начиная с единицы.
✔ Слова выводятся отсортированными согласно кодировки Unicode.
✔ Текст выравнивается по правому краю так, чтобы у самого
длинного слова был один пробел между ним и номером строки.
"""


def str_printer(str_input):
    res = ''
    str_input = str_input.split()
    str_input.sort()
    maxx = max([len(i) for i in str_input])

    for n, s in enumerate(str_input, 1):
        res = res + (f"{n} {s:>{maxx}}\n")
    return  res

print(str_printer('Здесь может быть Ваш текст'))

# def print_sort_txt(txt):
#     words = txt.lower().split()
#
#     words = sorted(words)
#     max_len = max(len(word) for word in words)
#     for i, word in enumerate(words, start=1):
#         print(f'{i}. {word:>{max_len}}')
#
#
# def print_sort(txt):
#     for i, word in enumerate(sorted(txt.lower().split()), 1):
#         print(f'{i}. {word:>{max(len(word) for word in txt.lower().split())}}')
#
#
# text = "Напишите функцию, которая принимает строку текста"
# print_sort_txt(text)
# print()
# print_sort(text)
