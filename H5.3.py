import string

text = input("Введіть рядок: ")

# Видаляємо знаки пунктуації та пробіли (крім букв і цифр)
cleaned = ''.join(char for char in text if char not in string.punctuation)

# Розбиваємо на слова
words = cleaned.split()

# Робимо кожне слово з великої літери
capitalized_words = [word.capitalize() for word in words]

# Об’єднуємо в один рядок і додаємо "#"
hashtag = "#" + ''.join(capitalized_words)

# Обрізаємо, якщо довжина більше 140 символів
if len(hashtag) > 140:
    hashtag = hashtag[:140]

print(hashtag)
