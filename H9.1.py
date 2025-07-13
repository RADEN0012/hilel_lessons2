def popular_words(text, words):
    # Приводимо текст до нижнього регістру та розбиваємо на слова
    text_words = text.lower().split()

    # Повертаємо словник із підрахованими входженнями
    return {word: text_words.count(word) for word in words}
assert popular_words(
    '''When I was One I had just begun When I was Two I was nearly new''',
    ['i', 'was', 'three', 'near']
) == {
    'i': 4,
    'was': 3,
    'three': 0,
    'near': 0
}, 'Test1'

print('OK')
