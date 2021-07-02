# 1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде
# строки формата «день-месяц-год». В рамках класса реализовать два метода. Первый — с
# декоратором @classmethod. Он должен извлекать число, месяц, год и преобразовывать их тип
# к типу «Число». Второй — с декоратором @staticmethod, должен проводить валидацию числа,
# месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на
# реальных данных.

class Data:
    def __init__(self, date):
        self.date = date

    def __str__(self):
        return str(self.date)

    @classmethod
    def int_transform(cls, date):
        return list(map(int, date.split('-')))

    @staticmethod
    def validation(date):
        date_list = Data.int_transform(date)
        if date_list[0] > 31 or date_list[0] < 1:
            return f'{date_list[0]} - недопустимое число!'
        if date_list[1] > 12 or date_list[1] < 1:
            return f'{date_list[1]} - недопустимый месяц!'
        else:
            return 'Данные верны.'


d = Data('01-07-2021')
print(d)
print(Data.int_transform('01-07-2021'))
print(Data.validation('01-07-2021'))
