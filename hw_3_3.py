"""
Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения.
Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность.
Достаточно вернуть один допустимый вариант. *Верните все возможные варианты комплектации рюкзака.
"""


def get_ruk(max_mas):
    dict_ = {'палатка': 5, 'котелок': 1, 'спальный мешок': 2, 'резиновые сапоги': 1, 'тушонка': 1, 'топор': 2}
    sum_mas = 0
    result = {}
    for key, value in dict_.items():
        if value + sum_mas < max_mas:
            result[key] = value
            sum_mas += value
    return dict_


max_mas = 10
print(get_ruk(max_mas))
