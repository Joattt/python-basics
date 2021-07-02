# 7. Реализовать проект «Операции с комплексными числами». Создать класс «Комплексное
# число». Реализовать перегрузку методов сложения и умножения комплексных чисел.
# Проверить работу проекта. Для этого создать экземпляры класса (комплексные числа),
# выполнить сложение и умножение созданных экземпляров. Проверить корректность
# полученного результата.

class ComplexNumber:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, other):
        return f'({self.a} + {self.b}i) + ({other.a} + {other.b}i) = {self.a + other.a} + {self.b + other.b}i'

    def __mul__(self, other):
        return f'({self.a} + {self.b}i) * ({other.a} + {other.b}i) = {(self.a * other.a - self.b * other.b)} + ' \
               f'{(self.a * other.b + self.b * other.a)}i'


x = ComplexNumber(2, 3)
y = ComplexNumber(5, 9)
print(x + y)
print(x * y)
