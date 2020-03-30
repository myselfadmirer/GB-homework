# Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление. Числа запрашивать у
# пользователя, предусмотреть обработку ситуации деления на ноль


def my_division(x, y):
    try:
        x / y
    except ZeroDivisionError:
        return print('Деление на 0')
    else:
        return x / y


result = None
while not result:
    x = input('Введите делимое\n')
    y = input('Введите делитель\n')
    try:
        x = float(x)
        y = float(y)
    except ValueError:
        print('Введите корректное значение')
    else:
        result = my_division(x, y)
print(f'Результат деления - {result}')
