#Пользователь вводит время в секундах. Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс. Используйте форматирование строк.

time_sec = input('Введите время в секундах ')
if time_sec.isdigit() and int(time_sec) > 0:
    time_sec = int(time_sec)
    ss = time_sec % 60
    mm = time_sec // 60 % 60
    hh = time_sec // 60 // 60
else:
    print('Ничего не выйдет, должно быть введено целое положительное число')

print(f'{hh:02}:{mm:02}:{ss:02}')
