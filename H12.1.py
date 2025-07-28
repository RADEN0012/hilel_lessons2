import codecs
import re

def delete_html_tags(html_file, result_file='cleaned.txt'):
    with codecs.open(html_file, 'r', 'utf-8') as file:
        html = file.read()

    # Видалити HTML-теги
    cleaned_text = re.sub(r'<[^>]+>', '', html)

    # Залишити тільки непорожні рядки
    cleaned_lines = [line.strip() for line in cleaned_text.splitlines() if line.strip()]

    # Записати у файл
    with codecs.open(result_file, 'w', 'utf-8') as output:
        output.write('\n'.join(cleaned_lines))
