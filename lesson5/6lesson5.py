# Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие
# лекционных, практических и лабораторных занятий по этому предмету и их количество. Важно, чтобы для каждого
# предмета не обязательно были все типы занятий. Сформировать словарь, содержащий название предмета и общее
# количество занятий по нему. Вывести словарь на экран. Примеры строк файла:
# Информатика: 100(л) 50(пр) 20(лаб)
# Физика: 30(л) 10(лаб)
# Физкультура: 30(пр)
# Пример словаря:
# {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}


# from re import findall
#
# c_dict = {}
#
# with open(r'C:\\Users\\NELYUBINA\\git-project\\GB-homework\\lesson5\\6lesson5.txt', 'r', encoding='utf-8') as my_file:
#     for line in my_file:
#         my_class = line.split(':')
#         hours = findall(r'[0-9]+', my_class[1])
#         c_dict[my_class[0]] = sum(list(map(int, hours)))
# print(c_dict)


c_dict = {}

with open(r'C:\\Users\\NELYUBINA\\git-project\\GB-homework\\lesson5\\6lesson5.txt', 'r', encoding='utf-8') as my_file:
    for line in my_file:
        my_class = line.split(':')
        hours = [int(el.split('(')[0]) for el in my_class[1].split() if el.split('(')[0].isdigit()]
        c_dict[my_class[0]] = sum(hours)
print(c_dict)
