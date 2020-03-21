# Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов. Определить,
# кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников. Выполнить подсчет средней величины
# дохода сотрудников.


name_list = []
av_salary = 0
num = 1

with open(r'C:\\Users\\NELYUBINA\\git-project\\GB-homework\\lesson5\\3lesson5.txt', 'r', encoding='utf-8') as my_file:
    for line in my_file:
        if int(line.split()[1]) < 20000:
            name_list.append(line.split()[0])
        av_salary += int(line.split()[1])
        num += 1
av_salary = av_salary / num
print('Получают меньше 20 тыс рублей: ' + ', '.join(name_list) + '.\nСредняя зарплата по фирме - ' + str(av_salary))
