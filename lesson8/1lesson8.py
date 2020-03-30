# Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата
# «день-месяц-год». В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать
# число, месяц, год и преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить
# валидацию числа, месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных
# данных.

from datetime import date


class Data:

    def __init__(self, my_date: str):
        """

        :param my_date: str Input date 'dd-mm-yy'
        """
        self.my_date = my_date

    @classmethod
    def get_date(cls, my_date: str):
        """
        Class method takes string date 'dd-mm-yy'
        :param my_date: str
        :return: int
        """
        try:
            d, m, y = map(int, my_date.split('-'))
        except ValueError:
            print('Неверный формат ввода. дд-мм-гг')
        else:
            return d, m, y

    @staticmethod
    def validation(d, m, y):
        """
        Static method of the date validation
        :param d: int day
        :param m: int month
        :param y: int year
        :return: str valid date or exception
        """
        if 1900 < y < 2021:
            try:
                date(y, m, d)
            except ValueError:
                print('Неверный формат ввода')
            print(f'{d:02}.{m:02}.{y}')
        else:
            print('Год должен быть в промежутке от 1901 до 2020')


if __name__ == '__main__':
    day, month, year = Data.get_date('28-02-2019')
    print(day)
    print(month)
    print(year)
    Data.validation(day, month, year)
