# Ввід від користувача
seconds_input = int(input("Введіть кількість секунд (0 до 8640000): "))

# Кількість секунд у 1 дні
seconds_per_day = 24 * 60 * 60

# Обчислюємо кількість днів та залишок секунд
days, remainder = divmod(seconds_input, seconds_per_day)

# Обчислюємо години з залишку
hours, remainder = divmod(remainder, 3600)

# Обчислюємо хвилини з залишку
minutes, seconds = divmod(remainder, 60)

# Форматуємо з ведучими нулями
hours_str = str(hours).zfill(2)
minutes_str = str(minutes).zfill(2)
seconds_str = str(seconds).zfill(2)

# Узгодження слова "день/дні/день"
if days == 1:
    day_word = "день"
elif 2 <= days % 10 <= 4 and not 12 <= days % 100 <= 14:
    day_word = "дні"
else:
    day_word = "днів"

# Вивід результату
print(f"{days} {day_word}, {hours_str}:{minutes_str}:{seconds_str}")
