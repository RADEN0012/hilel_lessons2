# Тестові приклади
examples = [
    [0, 1, 7, 2, 4, 8],   # (0 + 7 + 4) * 8 = 88
    [1, 3, 5],            # (1 + 5) * 5 = 30
    [6],                 # 6 * 6 = 36
    []                   # порожній список => 0
]

# Проходимо по кожному прикладу
for lst in examples:
    if len(lst) == 0:
        result = 0
    else:
        suma = 0
        for i in range(0, len(lst), 2):  # проходимо по парних індексах
            suma += lst[i]
        result = suma * lst[-1]  # множимо на останній елемент

    print(f"{lst} => {result}")
