# Создать список и заполнить его элементами различных типов данных. Реализовать скрипт проверки типа данных каждого
# элемента. Использовать функцию type() для проверки типа. Элементы списка можно не запрашивать у пользователя,
# а указать явно, в программе.

my_list = [1, 43, 2.3, 'abc', False, (3, 2), {'c': 'blue'}, {3, 6}]
for i in my_list:
    print(type(i))
