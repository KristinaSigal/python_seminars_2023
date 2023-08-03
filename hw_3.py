"""
Дан список повторяющихся элементов.
Вернуть список с дублирующимися элементами.
В результирующем списке не должно быть дубликатов.
"""


def del_duplicates(lst):
    res_list = []
    for x in lst:
        if lst.count(x) > 1 and res_list.count(x) == 0:
            res_list.append(x)
    return res_list


lst = [1, 1, 6, 3, 2, 3, 4, 4, 2, 2, 5, 5, 6]
print(del_duplicates(lst))
