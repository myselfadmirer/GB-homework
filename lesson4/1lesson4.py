# Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника. В расчете
# необходимо использовать формулу: (выработка в часах * ставка в час) + премия. Для выполнения расчета для конкретных
# значений необходимо запускать скрипт с параметрами.

from sys import argv


def salary(hours: float, rate: float, bonus: float):
    """
    Calculation of an employee's salary
    :param hours: float number of working hours
    :param rate: float salary rate per hour
    :param bonus: float bonus
    :return: float employee's salary
    """
    return hours * rate + bonus


_, hours, rate, bonus = argv

try:
    hours, rate, bonus = float(hours), float(rate), float(bonus)
except ValueError as e:
    print(e)
    raise ValueError('Должны передаваться значения типа float')

print(f' Зарплата сотрудника составит: {salary(hours, rate, bonus)}')
