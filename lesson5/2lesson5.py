# Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк,
# количества слов в каждой строке.


count_str = 0
count_word = 0

with open(r'C:\\Users\\NELYUBINA\\git-project\\GB-homework\\lesson5\\2lesson5.txt', 'r', encoding='utf=8') as my_file:
    for line in enumerate(my_file):
        count_word = line[1].split()
        print(f'В {line[0] + 1} строке количество слов - {len(count_word)}')
        count_str += 1
print(f'Всего строк - {count_str}')
