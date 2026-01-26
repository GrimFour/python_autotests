# Створіть клас геометричної фігури "Ромб". Клас повинен мати наступні атрибути:
#
# сторона_а (довжина сторони a).
# кут_а (кут між сторонами a і b).
# кут_б (суміжний з кутом кут_а).
# Необхідно реалізувати наступні вимоги:
#
# Значення сторони сторона_а повинно бути більше 0.
# Кути кут_а та кут_б повинні задовольняти умову: кут_а + кут_б = 180
# Протилежні кути ромба завжди рівні, тому при заданому значенні кут_а, значення кут_б обчислюється автоматично.
# Для встановлення значень атрибутів використовуйте метод __setattr__.


class Diamond:

    def __init__(self, sideA, angleA):
        self.sideA = sideA
        self.angleA = angleA

    def __setattr__(self, name, value):
        if name == "sideA":
            if value <= 0:
                raise ValueError("сторона а повинна бути більшою за 0")
            super().__setattr__(name, value)

        elif name == "angleA":
            if not (0 < value < 180):
                raise ValueError("angleA повинен бути в межах (0, 180)")
            super().__setattr__(name, value)
            super().__setattr__("angleB", 180 - value)

        elif name == "angleB":
            raise AttributeError("angleB обчислюється автоматично і не може бути заданий напряму")

        else:
            super().__setattr__(name, value)

r1 = Diamond(5, 60)
print(r1.sideA)
print(r1.angleA)
print(r1.angleB)

print(f'='*20)
r2 = Diamond(7, 85)
print(r2.sideA)
print(r2.angleA)
print(r2.angleB)

# print(f'='*20)
# r3 = Diamond(0, 35)
# print(r3.sideA)

print(f'='*20)
r4 = Diamond(3, 47)
r4.angleB = 60
print(r4.angleB)