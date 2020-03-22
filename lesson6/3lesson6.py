# Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность),
# income (доход). Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы: оклад и
# премия, например, {"wage": wage, "bonus": bonus}. Создать класс Position (должность) на базе класса Worker. В
# классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учетом премии (
# get_total_income). Проверить работу примера на реальных данных (создать экземпляры класса Position,
# передать данные, проверить значения атрибутов, вызвать методы экземпляров).


class Worker:
    _income = {'wage': input('Введите оклад\n'), 'bonus': input('Введите бонус\n')}

    def __init__(self, name: str, surname: str, position: str):
        self.name = name
        self.surname = surname
        self.position = position


class Position(Worker):

    def __init__(self, name, surname, position):
        super().__init__(name, surname, position)

    def get_full_name(self):
        return f'{self.name} {self.surname}, должность - {self.position}'

    def get_total_income(self):
        total_income = float(self._income.get('wage')) + float(self._income.get('bonus'))
        return f'Доход: {total_income} рублей'


worker1 = Position('Александр', 'Ветров', 'Инженер')
print(worker1.get_full_name())
print(worker1.get_total_income())
print(worker1._income)
