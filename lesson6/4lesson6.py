# Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (
# булево). А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась,
# повернула (куда). Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый
# класс метод show_speed, который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar
# переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться
# сообщение о превышении скорости. Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к
# атрибутам, выведите результат. Выполните вызов методов и также покажите результат.


from random import randint, choice


class Car:

    def __init__(self, color: str, name: str, is_police: bool):
        self.color = color
        self.name = name
        self.is_police = is_police
        self.speed = randint(1, 160)
        self.direction = choice(('направо', 'налево'))

    def go(self):
        print(f'Автомобиль {self.name} тронулся')

    def stop(self):
        print(f'Автомобиль {self.name} остановился')

    def turn(self):
        print(f'Автомобиль {self.name} повернул {self.direction}')

    def show_speed(self):
        print(f'Текущая скорость {self.name} - {self.speed}')


class TownCar(Car):
    def __init__(self, color, name, is_police=False):
        super().__init__(color, name, is_police)

    def show_speed(self):
        if self.speed > 60:
            print(f'Скорость превышена. Скорость движения - {self.speed}')
        else:
            print(f'Скорость движения - {self.speed}')


class WorkCar(Car):
    def __init__(self, color, name, is_police=False):
        super().__init__(color, name, is_police)

    def show_speed(self):
        if self.speed > 40:
            print(f'Скорость превышена. Скорочть движения - {self.speed}')
        else:
            print(f'Скорость движения - {self.speed}')


class SportCar(Car):
    def __init__(self, color, name, is_police=False):
        super().__init__(color, name, is_police)


class PoliceCar(Car):
    def __init__(self, color, name, is_police=True):
        super().__init__(color, name, is_police)


car1 = TownCar('red', 'Nissan')
car1.show_speed()
car1.turn()
car2 = WorkCar('green', 'Mazda')
car2.go()
car2.stop()
car3 = SportCar('yellow', 'Ferrari')
car3.show_speed()
a = car3.is_police
car4 = PoliceCar('black', 'Ford')
b = car4.direction
car4.turn()
car4.show_speed()
print(a, b)
