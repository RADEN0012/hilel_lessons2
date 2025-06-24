import random

# Створюємо список випадкової довжини від 3 до 10
original_list = []
length = random.randint(3, 10)

# Заповнюємо список випадковими числами від 1 до 100
for i in range(length):
    number = random.randint(1, 100)
    original_list.append(number)

# Створюємо новий список із першого, третього та другого з кінця елементів
new_list = [original_list[0], original_list[2], original_list[-2]]

# Виводимо обидва списки
print("Початковий список:", original_list)
print("Новий список:", new_list)
