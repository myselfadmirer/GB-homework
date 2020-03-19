# Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме: название,
# форма собственности, выручка, издержки. Пример строки файла: firm_1 ООО 10000 5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль. Если фирма получила
# убытки, в расчет средней прибыли ее не включать. Далее реализовать список. Он должен содержать словарь с фирмами и их
# прибылями, а также словарь со средней прибылью. Если фирма получила убытки, также добавить ее в словарь (со значением
# убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}]. Итоговый
# список сохранить в виде json-объекта в соответствующий файл. Пример json-объекта: [{"firm_1": 5000, "firm_2": 3000,
# "firm_3": 1000}, {"average_profit": 2000}]
# Подсказка: использовать менеджеры контекста.


import json

my_list = []
dict_profit = {}
dict_av_profit = {}
sum = 0
num_firms = 1

with open(r'C:\\Users\\NELYUBINA\\git-project\\GB-homework\\lesson5\\7lesson5.txt', 'r', encoding='utf-8') as my_file:
    for line in my_file:
        profit = int(line.split()[2]) - int(line.split()[3])
        if profit > 0:
            sum += profit
            num_firms += 1
        dict_profit[line.split()[0]] = profit
    my_list.append(dict_profit)
dict_av_profit['average_profit'] = sum / num_firms
my_list.append(dict_av_profit)
print(my_list)

with open(r'C:\\Users\\NELYUBINA\\git-project\\GB-homework\\lesson5\\7_1lesson5.txt', 'w', encoding='utf-8') as j_file:
    json.dump(my_list, j_file)
