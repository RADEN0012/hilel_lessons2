# Введення 4-значного числа
num = int(input("Enter a 4-digit number: "))

# Отримання цифр числа за допомогою ділення
digit1 = num // 1000                 # перша цифра
digit2 = (num // 100) % 10           # друга цифра
digit3 = (num // 10) % 10            # третя цифра
digit4 = num % 10                    # четверта цифра

# Вивід цифр у стовпчик
print(digit1)
print(digit2)
print(digit3)
print(digit4)
