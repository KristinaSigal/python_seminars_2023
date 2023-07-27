"""
Задание №1
✔ Вручную создайте список с целыми числами, которые повторяются.
Получите новый список, который содержит уникальные (без повтора) элементы исходного списка.
✔ *Подготовьте два решения, короткое и длинное, которое не использует другие коллекции помимо списков.
"""

lst = [3, 3, 4, 5, 1]
print(lst)
print(list(set(lst)))


new_lst = []  # перебираем все элементы в lst. Если его нет, закидываем  в new_list
for el in lst:
    if el in new_lst:
        continue
    else:
        new_lst.append(el)
print(new_lst)


new_lst_1 = []
for el in lst:
    if el not in new_lst_1:
        new_lst.append(el)
print(sorted(new_lst_1, reverse=True))