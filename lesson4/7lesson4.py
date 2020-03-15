# Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное значение. При вызове функции
# должен создаваться объект-генератор. Функция должна вызываться следующим образом: for el in fibo_gen(). Функция
# отвечает за получение факториала числа, а в цикле необходимо выводить только первые 15 чисел. Подсказка: факториал
# числа n — произведение чисел от 1 до n. Например, факториал четырёх 4! = 1 * 2 * 3 * 4 = 24.

from _collections_abc import Iterable
from itertools import count


# Так как условие задачи в методичке и на странице с задаием GB отличаются, представляю 2 варианта решения.
# Функция my_fact(n), принимающая на входе n, ограничивающая расчет до n!

def my_fact(n: int) -> Iterable:
    """
    function generate factorials values numbers up to param
    :param n: int last factorial value in generator
    :return: Iterable next factorial value up to param
    """
    fact = 1
    for i in count(1):
        if i > n:
            break
        else:
            fact *= i
            yield fact


for el in my_fact(10):
    print(el)


# Функция my_gen(), не принимающая на входе аргументы, бесконечно расчитывает значения факториала. Ограничение задается
# в теле программы.

def my_gen() -> Iterable:
    """
    function generate factorials values numbers
    :return: Iterable next factorial value
    """
    fact = 1
    for i in count(1):
        fact *= i
        yield fact

i = 1
for el in my_gen():
    if i > 15:
        break
    else:
        print(el)
        i += 1
