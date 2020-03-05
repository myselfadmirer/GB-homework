#Поработайте с переменными, создайте несколько, выведите на экран, запросите у пользователя несколько чисел и строк и сохраните в переменные, выведите на экран.

my_int = 3
my_float = 2.4
my_str = 'Good morning!'
my_bool = True
print(my_int, my_float, my_str, my_bool, sep='\n')
print(type(my_int))
print(type(my_float))
print(type(my_str))
print(type(my_bool))
user_name = input('Введите свое имя ')
user_age = input('Введите свой возраст ')
user_town = input('Введите город проживания ')
print(f'Первый пользователь: {user_name}, {user_age} лет, из города {user_town}. Привет, {user_name}!')
