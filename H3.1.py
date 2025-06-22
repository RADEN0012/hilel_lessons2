# Запитуємо у користувача два числа
num1 = float(input("Введіть перше число: "))
operation = input("Введіть операцію (+, -, *, /): ")
num2 = float(input("Введіть друге число: "))

# Обробка арифметичних операцій
if operation == "+":
    result = num1 + num2
    print("Результат:", result)
elif operation == "-":
    result = num1 - num2
    print("Результат:", result)
elif operation == "*":
    result = num1 * num2
    print("Результат:", result)
elif operation == "/":
    if num2 == 0:
        print("Помилка: Ділення на нуль неможливе!")
    else:
        result = num1 / num2
        print("Результат:", result)
else:
    print("Помилка: Невідома операція.")
