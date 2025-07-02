# Отримуємо число від користувача
num = int(input("Введіть ціле число: "))

# Поки число більше за 9 — повторюємо множення цифр
while num > 9:
    product = 1
    for digit in str(num):
        product *= int(digit)
    num = product

# Вивід остаточного результату
print(num)
