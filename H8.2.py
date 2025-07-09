import string

def is_palindrome(text):
    # Залишаємо лише алфавітно-цифрові символи, приводимо до нижнього регістру
    cleaned = ''.join(c.lower() for c in text if c.isalnum())
    # Перевіряємо, чи дорівнює рядок своєму зворотному варіанту
    return cleaned == cleaned[::-1]

# Unit tests
assert is_palindrome('A man, a plan, a canal: Panama') == True, 'Test1'
assert is_palindrome('0P') == False, 'Test2'
assert is_palindrome('a.') == True, 'Test3'
assert is_palindrome('aurora') == False, 'Test4'
print("ОК")
