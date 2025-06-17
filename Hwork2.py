# Введення числа
num = int(input("Enter a 5-digit number: "))

# Отримуємо кожну цифру з кінця
digit1 = num % 10            # остання цифра
digit2 = (num // 10) % 10    # передостання
digit3 = (num // 100) % 10   # середня
digit4 = (num // 1000) % 10  # друга
digit5 = (num // 10000)      # перша

# Формуємо число у зворотному порядку
reversed_num = digit1 * 10000 + digit2 * 1000 + digit3 * 100 + digit4 * 10 + digit5

# Виводимо результат
print("Перевернуте число:", reversed_num)
