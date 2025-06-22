def split_list(lst):
    mid = (len(lst) + 1) // 2  # Ділимо список на дві частини, якщо непарна кількість — перша більша
    return [lst[:mid], lst[mid:]]

# Приклади для перевірки
print(split_list([1, 2, 3, 4, 5, 6]))   # [[1, 2, 3], [4, 5, 6]]
print(split_list([1, 2, 3]))            # [[1, 2], [3]]
print(split_list([1, 2, 3, 4, 5]))      # [[1, 2, 3], [4, 5]]
print(split_list([1]))                 # [[1], []]
print(split_list([]))                  # [[], []]
