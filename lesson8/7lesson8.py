# Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число», реализуйте перегрузку
# методов сложения и умножения комплексных чисел. Проверьте работу проекта, создав экземпляры класса (комплексные
# числа) и выполнив сложение и умножение созданных экземпляров. Проверьте корректность полученного результата.
import fourth as fourth


class ComplexNumber:
    def __init__(self, real: float, img: float):
        """
        Input of real and imaginary part of complex number
        :param real: float
        :param img: float
        """
        try:
            self.real = float(real)
            self.img = float(img)
        except ValueError:
            print('Программа ожидает на ввод только числа или дроби. Будьте внимательнее')

    def __str__(self):
        return f'{self.real} + {self.img}i'

    def __add__(self, other):
        """
        Additional of complex number
        :param other: ComplexNumber
        :return: ComplexNumber
        """
        return ComplexNumber(round(self.real + other.real, 2), round(self.img + other.img, 2))

    def __mul__(self, other):
        """
        Multiplication of complex number
        :param other: ComplexNumber
        :return: ComplexNumber
        """
        return ComplexNumber(round(self.real * other.real - self.img * other.img, 2),
                             round(self.img * other.real + self.real * other.img, 2))


if __name__ == '__main__':
    first = ComplexNumber(3.1, 1)
    print(first)
    second = ComplexNumber(1.1, 3.4)
    print(second)
    third = first + second
    print(third)
    fourth = first * third
    print(fourth)
