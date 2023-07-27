"""
Задание №7 | Коллекции
✔ Пользователь вводит строку текста.
✔ Подсчитайте сколько раз встречается каждая буква в строке без использования метода count и с ним.
✔ Результат сохраните в словаре, где ключ — символ, а значение — частота встречи символа в строке.
✔ Обратите внимание на порядок ключей. Объясните почему они совпадают или не совпадают в ваших решениях.
"""

data = input("Введите строку текста: ")
dct = {}
for el in data:
    val = data.count(el)
    dct[el] = val
print(dct)

data = input("Введите строку текста: ")
dct = {}
for el_1 in data:
    count = 0
    for el_2 in data:
        if el_1 == el_2:
            count += 1
    dct[el_1] = count
print(dct)
