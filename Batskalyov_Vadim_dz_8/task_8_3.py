# 3. Написать декоратор для логирования типов позиционных аргументов функции, например:
# def type_logger...
# ...
# @type_logger
# def calc_cube(x):
# return x ** 3
# >>> a = calc_cube(5)
# 5: <class 'int'>

def type_logger(func):
    def wrapper(arg):
        return f'{arg}: {type(arg)}'

    return wrapper


@type_logger
def calc_cube(x):
    return x ** 3


print(calc_cube(5))

# Примечание: если аргументов несколько - выводить данные о каждом через запятую; можете
# ли вы вывести тип значения функции? Сможете ли решить задачу для именованных
# аргументов? Сможете ли вы замаскировать работу декоратора? Сможете ли вывести имя
# функции, например, в виде:
# >>> a = calc_cube(5)
# calc_cube(5: <class 'int'>)

from functools import wraps


def type_logger(func):
    @wraps(func)
    def wrapper(*args):
        for arg in args:
            print(f'{func.__name__}({arg}: {type(arg)})', end=', ')
        return func(*args)
    return wrapper


@type_logger
def calc_cube(x, y):
    return x ** y


print(calc_cube(5, 2))
