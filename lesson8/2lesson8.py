# Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль. Проверьте его работу на данных,
# вводимых пользователем. При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту
# ситуацию и не завершиться с ошибкой.


class MyZeroDivisionError(Exception):
    def __init__(self, txt):
        """
        Zero division exception
        :param txt: str Input output message
        """
        self.txt = txt


c = None

while not c:
    a = input('Введите делимое\n')
    b = input('Введите делитель\n')
    try:
        a = float(a)
        b = float(b)
        if b == 0:
            raise MyZeroDivisionError('Делитель = 0. На 0 делить нельзя')
    except MyZeroDivisionError as e:
        print(e)
    except ValueError:
        print('Введите числовые значения')
    else:
        c = a / b
        print(f'Результат деления: {c}')
