# 2. Реализовать проект расчёта суммарного расхода ткани на производство одежды. Основная
# сущность (класс) этого проекта — одежда, которая может иметь определённое название. К
# типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют
# параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H
# соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто
# (V/6.5 + 0.5), для костюма (2*H + 0.3). Проверить работу этих методов на реальных данных.
# Выполнить общий подсчёт расхода ткани. Проверить на практике полученные на этом уроке
# знания. Реализовать абстрактные классы для основных классов проекта и проверить работу
# декоратора @property.

from abc import ABC, abstractmethod


class Clothes(ABC):
    @abstractmethod
    def fabric_usage(self):
        pass

    def __add__(self, other):
        summ = self.fabric_usage + other.fabric_usage
        return summ

class Coat(Clothes):
    def __init__(self, name, size):
        self.name = name
        self.v = size

    @property
    def fabric_usage(self):
        usage = self.v / 6.5 + 0.5
        return usage


class Suit(Clothes):
    def __init__(self, name, height):
        self.name = name
        self.h = height

    @property
    def fabric_usage(self):
        usage = 2 * self.h + 0.3
        return usage


c1 = Coat('Большевичка', 54)
print(c1.fabric_usage)

s1 = Suit('Модник', 1.8)
print(s1.fabric_usage)

print(c1 + s1)
