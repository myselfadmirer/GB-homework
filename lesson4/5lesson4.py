# Реализовать формирование списка, используя функцию range() и возможности генератора. В список должны войти четные
# числа от 100 до 1000 (включая границы). Необходимо получить результат вычисления произведения всех элементов
# списка. Подсказка: использовать функцию reduce()


from functools import reduce


my_list = [i for i in range(100, 1001) if not i % 2]


# Решение с функцией

def my_func(prev_el: int, el: int) -> int:
    """
    Returns product of the arguments

    (prev_el, el) -> prod

    :param prev_el: int a number
    :param el: int a number
    :return: int the multiplication of prev_el and el
    """
    return prev_el * el


print(reduce(my_func, my_list))

# Решение с использованием lambda функциии

print(reduce(lambda prev_el, el: prev_el * el, my_list))
