# Завдання 2
#
# Створіть абстрактний клас "Фігура" з абстрактними методами для отримання площі та периметру.
# Наслідуйте від нього декілька (> 2) інших фігур, та реалізуйте математично вірні для них методи для площі та периметру.
# Властивості по типу “довжина сторони” й т.д. повинні бути приватними, та ініціалізуватись через конструктор.
# Створіть Декілька різних об’єктів фігур, та у циклі порахуйте та виведіть в консоль площу та периметр кожної.

from abc import ABC, abstractmethod
import math

class Figure(ABC):
    @abstractmethod
    def perimeter(self):
        pass

    @abstractmethod
    def area(self):
        pass

class Square(Figure):
    def __init__(self, side):
        self.__side = side   # приватне поле

    def perimeter(self):
        return 4 * self.__side

    def area(self):
        return self.__side ** 2

class Rectangle(Figure):
    def __init__(self, sideA, sideB):
        self.__sideA = sideA
        self.__sideB = sideB

    def perimeter(self):
        return (self.__sideA + self.__sideB) * 2

    def area(self):
        return self.__sideA * self.__sideB

class Circle(Figure):
    def __init__(self, radius):
        self.__radius = radius

    def perimeter(self):
        return math.pi * self.__radius * 2

    def area(self):
        return math.pi * self.__radius * self.__radius

figures = [
    Square(5),
    Rectangle(4, 6),
    Circle(3)
]

# for f in figures:
#     print(f'{f.__class__.__name__} perimeter: {f.perimeter():.2f}, and area: {f.area():.2f}')

for figure in figures:
    print(
        f'{figure.__class__.__name__}: '
        f'area = {figure.area():.2f}, '
        f'perimeter = {figure.perimeter():.2f}'
    )