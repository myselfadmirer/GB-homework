# Пользователь вводит строку из нескольких слов, разделённых пробелами. Вывести каждое слово с новой строки. Строки
# необходимо пронумеровать. Если в слово длинное, выводить только первые 10 букв в слове.

phrase = input('Введите слова через пробел\n').split()
for ind, word in enumerate(phrase, 1):
    print(f'{ind}. {word[:10]}')
