# Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина). Значения данных 
# атрибутов должны передаваться при создании экземпляра класса. Атрибуты сделать защищенными. Определить метод 
# расчета массы асфальта, необходимого для покрытия всего дорожного полотна. Использовать формулу: длинаширинамасса 
# асфальта для покрытия одного кв метра дороги асфальтом, толщиной в 1 см*число см толщины полотна. Проверить работу 
# метода. Например: 20м*5000м*25кг*5см = 12500 т


class Road:

    def __init__(self, length: float, width: float):
        self.__length = length
        self.__width = width
        self.m = 25
        self.thickness = 5

    def asphalt_mass(self):
        asphalt_mass = self.__length * self.__width * self.m * self.thickness
        print(f'Масса асфальта составит {asphalt_mass / 1000} тонн')


any_road = Road(5000, 20)
any_road.asphalt_mass()
