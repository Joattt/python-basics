# 2. Создать собственный класс-исключение, обрабатывающий ситуацию деления на ноль.
# Проверить его работу на данных, вводимых пользователем. При вводе нуля в качестве
# делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.

class DivZerExcept(Exception):
    def __init__(self, dividend, divisor):
        self.dividend = dividend
        self.divisor = divisor
        print()

    @staticmethod
    def zero_div(dividend, divisor):
        try:
            return dividend / divisor
        except ZeroDivisionError:
            return 'Делить на ноль нельзя!'


print(DivZerExcept.zero_div(10, int(input('Введите число:'))))
0