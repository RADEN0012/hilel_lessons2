while True:
    # Ввід даних
    num1 = float(input("Введіть перше число: "))
    op = input("Введіть операцію (+, -, *, /): ")
    num2 = float(input("Введіть друге число: "))

    # Виконання операції
    if op == "+":
        result = num1 + num2
    elif op == "-":
        result = num1 - num2
    elif op == "*":
        result = num1 * num2
    elif op == "/":
        if num2 != 0:
            result = num1 / num2
        else:
            print("Ділення на нуль неможливе!")
            continue
    else:
        print("Невідома операція!")
        continue

    # Виведення результату
    print("Результат:", result)

    # Питання про продовження
    answer = input("Продовжити? (y/yes для так): ")
    if answer.lower() not in ("y", "yes"):
        print("Роботу завершено.")
        break
