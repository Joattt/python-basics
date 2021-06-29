# 1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод
# __init__()), который должен принимать данные (список списков) для формирования матрицы.
# Подсказка: матрица — система некоторых математических величин, расположенных в виде
# прямоугольной схемы.
# Примеры матриц: 3 на 2, 3 на 3, 2 на 4.
# 31 22
# 37 43
# 51 86
# 3 5 32
# 2 4 6
# -1 64 -8
# 3 5 8 3
# 8 3 7 1
# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном
# виде.
# Далее реализовать перегрузку метода __add__() для сложения двух объектов класса Matrix
# (двух матриц). Результатом сложения должна быть новая матрица.
# Подсказка: сложение элементов матриц выполнять поэлементно. Первый элемент первой
# строки первой матрицы складываем с первым элементом первой строки второй матрицы и пр.

from copy import deepcopy


class Matrix:
    def __init__(self, *args):
        self.matrix = []
        for arg in args:
            self.matrix.append(arg)

    def __str__(self):
        self.my_list = []
        for line in deepcopy(self.matrix):
            for i, el in enumerate(line):
                line[i] = str(el)
            self.my_list.append(' '.join(line))
        return '\n'.join(self.my_list)

    def __add__(self, other):
        try:
            summ = [[self.matrix[i][j] + other.matrix[i][j] for j in range(len(self.matrix[0]))] for i in range(len(self.matrix))]
            return Matrix([summ])
        except IndexError:
            return 'Размерности матриц не совпадают!'


m1 = Matrix([1, 2, 3], [4, 5, 6])
print(m1.matrix)
print(m1, end='\n\n')

m2 = Matrix([7, 8, 9], [10, 11, 12])
print(m2.matrix)
print(m2, end='\n\n')

print(m1 + m2)
