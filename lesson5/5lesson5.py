# Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами. Программа
# должна подсчитывать сумму чисел в файле и выводить ее на экран.


with open(r'C:\\Users\\NELYUBINA\\git-project\\GB-homework\\lesson5\\5lesson5.txt', 'w', encoding='utf-8') as my_file:
    while True:
        numbers = input('Введите числа через пробел\n')
        try:
            list(map(int, numbers.split()))
        except ValueError:
            print('Обнаружен тип str. Требуется ввести целые числа через пробел')
        else:
            my_file.write(numbers)
            break
with open(r'C:\\Users\\NELYUBINA\\git-project\\GB-homework\\lesson5\\5lesson5.txt', 'r', encoding='utf-8') as sum_file:
    read_numbers = sum_file.read()
    my_sum = sum(list(map(int, read_numbers.split())))
print(f'Сумма чисел равна {my_sum}')
