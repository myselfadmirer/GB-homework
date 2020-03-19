# Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем. Об окончании
# ввода данных свидетельствует пустая строка.


with open(r'C:\\Users\\NELYUBINA\\git-project\\GB-homework\\lesson5\\1lesson5.txt', 'w', encoding='utf-8') as my_file:
    while True:
        user_input = input('input string: ')
        my_file.write(user_input + '\n')
        if not user_input:
            break
