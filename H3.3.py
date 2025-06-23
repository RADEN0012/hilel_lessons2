# Приклади списків
lists = [
    [1, 2, 3, 4, 5, 6],
    [1, 2, 3],
    [1, 2, 3, 4, 5],
    [1],
    []
]

# Обробка кожного списку
for lst in lists:
    length = len(lst)
    middle = (length + 1) // 2  # Більша частина йде в перший список
    first = []
    second = []

    i = 0
    while i < middle:
        first.append(lst[i])
        i += 1

    while i < length:
        second.append(lst[i])
        i += 1

    result = [first, second]
    print(lst, "=>", result)
