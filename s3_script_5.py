"""
Задание №5 | Коллекции
✔ Создайте вручную список с повторяющимися целыми числами.
✔ Сформируйте список с порядковыми номерами нечётных элементов исходного списка.
✔ Нумерация начинается с единицы.
"""
# решение 1
lst_numbers = []
lst = [1, 2, 2, 3, 3, 4, 5, 5]
for i in range(len(lst)):
    if lst[i] % 2 == 1:
        lst_numbers.append(i + 1)
print(lst_numbers)

# решение 2
lst_numbers = [i + 1 for i in range(len(lst)) if lst[i] % 2 == 1]
print(lst_numbers)
