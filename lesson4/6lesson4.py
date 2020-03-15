# Реализовать два небольших скрипта:
# а) итератор, генерирующий целые числа, начиная с указанного,
# б) итератор, повторяющий элементы некоторого списка, определенного заранее.
# Подсказка: использовать функцию count() и cycle() модуля itertools.

from itertools import count, cycle

for i in count(3):
    if i > 20:
        break
    else:
        print(i)


my_list = [2, 4, 1, 8, 3, 6, 10, 33, 5]
num = 1
for i in cycle(my_list):
    if num > 15:
        break
    else:
        print(i)
        num += 1
