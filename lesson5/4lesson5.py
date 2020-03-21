# Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные. При этом английские
# числительные должны заменяться на русские. Новый блок строк должен записываться в новый текстовый файл


numbers = {
    'One': 'Один',
    'Two': 'Два',
    'Three': 'Три',
    'Four': 'Четыре',
}

with open(r'C:\\Users\\NELYUBINA\\git-project\\GB-homework\\lesson5\\4lesson5.txt', 'r', encoding='utf-8') as my_file:
    with open(r'C:\\Users\\NELYUBINA\\git-project\\GB-homework\\lesson5\\4_1lesson5.txt', 'w', encoding='utf-8') as new:
        for line in my_file:
            new_line = line.split()
            new_line[0] = numbers.get(line.split()[0])
            new.write(' '.join(new_line) + '\n')
