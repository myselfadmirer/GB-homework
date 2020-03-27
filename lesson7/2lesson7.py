# Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная сущность (класс) этого проекта
# — одежда, которая может иметь определенное название. К типам одежды в этом проекте относятся пальто и костюм. У
# этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и
# H, соответственно. Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 +
# 0.5), для костюма (2 * H + 0.3). Проверить работу этих методов на реальных данных. Реализовать общий подсчет
# расхода ткани. Проверить на практике полученные на этом уроке знания: реализовать абстрактные классы для основных
# классов проекта, проверить на практике работу декоратора @property.


from abc import ABC, abstractmethod


class Clothes(ABC):
    _main_len = 0

    def __init__(self):
        self._main_len = Clothes._main_len

    @abstractmethod
    def clothes_param(self):
        pass


class Coat(Clothes):

    def __init__(self, size: int):
        self.size = size
        self.__length = round((size / 6.5 + 0.5), 1)
        super().__init__()
        Clothes._main_len += self.__length

    def clothes_param(self):
        return f'Для пошива пальто размера {self.size} требуется {self.__length} м ткани'

    @property
    def length(self):
        return self.__length

    @length.setter
    def length(self, new_size):
        Clothes._main_len -= self.__length
        self.__length = round((new_size / 6.5 + 0.5), 1)
        Clothes._main_len += self.__length


class Suit(Clothes):
    def __init__(self, height: float):
        self.height = height
        self.__length = round((2 * height + 0.3), 1)
        super().__init__()
        Clothes._main_len += self.__length

    def clothes_param(self):
        return f'Для пошива костюма на рост {self.height} требуется {self.__length} м ткани'

    @property
    def length(self):
        return self.__length

    @length.setter
    def length(self, new_height):
        Clothes._main_len -= self.__length
        self.__length = round((2 * new_height + 0.3), 1)
        Clothes._main_len += self.__length


my_coat = Coat(42)
my_suit = Suit(1.6)
my_coat_2 = Coat(56)
print(my_suit.length)
print(my_coat.length)
print(my_coat_2.length)
print(Clothes._main_len)
print(my_coat.clothes_param())
print(my_suit.clothes_param())
