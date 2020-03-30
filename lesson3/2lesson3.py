# Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя: имя, фамилия, год рождения,
# город проживания, email, телефон. Функция должна принимать параметры как именованные аргументы. Реализовать вывод
# данных о пользователе одной строкой.


def person_func(**kwargs):
    print(f'{kwargs.get("surname", "")} {kwargs.get("name", "")} {kwargs.get("age", "")} лет, город {kwargs.get("city", "")}. Контактные данные: email: {kwargs.get("email", "")}, номер телефона: {kwargs.get("tel", "")}')


user = {
    'name': ('Имя', str),
    'surname': ('Фамилия', str),
    'age': ('Возраст', int),
    'city': ('Город', str),
    'email': ('Адрес почты', str),
    'tel': ('Телефон', int),
    }
for key, value in user.items():
    while True:
        user_input = input(f'{value[0]}\n')
        try:
            user_input = value[1](user_input)
        except ValueError:
            print('Введено некорректное значение')
            continue
        user[key] = user_input
        break
person_func(**user)
