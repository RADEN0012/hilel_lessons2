import string

# Вхідні дані
user_input = input("Введіть дві літери через дефіс (наприклад: a-c): ")

# Розділяємо по дефісу
start_char, end_char = user_input.split('-')

# Отримуємо рядок усіх літер
letters = string.ascii_letters

# Знаходимо індекси початкової та кінцевої літери
start_index = letters.index(start_char)
end_index = letters.index(end_char)

# Виводимо підрядок (включно до end_index)
result = letters[start_index:end_index + 1]
print(result)
