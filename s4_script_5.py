"""
Задание №5
✔ Функция принимает на вход три списка одинаковой длины:
✔ имена str,
✔ ставка int,
✔ премия str с указанием процентов вида «10.25%».
✔ Вернуть словарь с именем в качестве ключа и суммой премии в качестве значения.
✔ Сумма рассчитывается как ставка умноженная на процент премии.
"""

#
# def func(lst_names, lst_bases, lst_bonuses):
#     res = {el_1: el_2 * float(el_3.rstrip("%")) / 100
#            for el_1, el_2, el_3 in zip(lst_names, lst_bases, lst_bonuses)}
#     return res
#
#
# names = ['Борис', 'Иван', 'Петр', "Сергей"]
# salaries = [10000, 12000, 16000, 14000]
# awards = ['12.35%', '10.25%', '7.75%', '8.85%']
#
# print(func(names, salaries, awards))


# Вариант2


def func(lst_names, lst_bases, lst_bonuses):
    res = [i[0] * float(i[1].rstrip("%")) / 100 for i in zip(lst_bases, lst_bonuses)]
    return dict(zip(lst_names, res))


names = ['Борис', 'Иван', 'Петр', "Сергей"]
salaries = [10000, 12000, 16000, 14000]
awards = ['12.35%', '10.25%', '7.75%', '8.85%']

print(func(names, salaries, awards))
