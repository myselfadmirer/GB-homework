# Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить к какому времени года относится месяц (зима,
# весна, лето, осень). Напишите решения через list и через dict.

# Решение с использованием list и dict

list_year = [(12, 1, 2), (3, 4, 5), (6, 7, 8), (9, 10, 11)]
dict_year = {
    0: 'Зима',
    1: 'Весна',
    2: 'Лето',
    3: 'Осень'
    }
while True:
    month = input('Введите номер месяца от 1 до 12\n')
    if month.isdigit() and 0 < int(month) < 13:
        month = int(month)
        for key, season in enumerate(list_year):
            if month in season:
                print(dict_year.get(key))
        break
    else:
        print('Введенное значение неверно')

# Решение с использованием dict

dict_year = {
    ('12', '1', '2'): 'Зима',
    ('3', '4', '5'): 'Весна',
    ('6', '7', '8'): 'Лето',
    ('9', '10', '11'): 'Осень'
}
while True:
    month = input('Введите номер месяца от 1 до 12\n')
    if month.isdigit() and 0 < int(month) < 13:
        for key, season in dict_year.items():
            if month in key:
                print(dict_year.get(key))
        break
    else:
        print('Введенное значение неверно')

# Решение с использованием list

list_year = [('12', '1', '2'), 'Зима', ('3', '4', '5'), 'Весна', ('6', '7', '8'), 'Лето', ('9', '10', '11'), 'Осень']
while True:
    month = input('Введите номер месяца от 1 до 12\n')
    if month.isdigit() and 0 < int(month) < 13:
        for i in range(len(list_year)):
            if month in list_year[i]:
                print(list_year[i + 1])
        break
    else:
        print('Введенное значение неверно')
