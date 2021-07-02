# 4. Начать работу над проектом «Склад оргтехники». Создать класс, описывающий склад. А также
# класс «Оргтехника», который будет базовым для классов-наследников. Эти классы —
# конкретные типы оргтехники (принтер, сканер, ксерокс). В базовом классе определить
# параметры, общие для приведённых типов. В классах-наследниках реализовать параметры,
# уникальные для каждого типа оргтехники.
# 5. Продолжить работу над предыдущим заданием. Разработать методы, которые отвечают за
# приём оргтехники на склад и передачу в определённое подразделение компании. Для
# хранения данных о наименовании и количестве единиц оргтехники, а также других данных,
# можно использовать любую подходящую структуру (например, словарь).
# 6. Продолжить работу над предыдущим заданием. Реализовать механизм валидации вводимых
# пользователем данных. Например, для указания количества принтеров, отправленных на
# склад, нельзя использовать строковый тип данных.
# Подсказка: постарайтесь реализовать в проекте «Склад оргтехники» максимум возможностей,
# изученных на уроках по ООП.

class Warehouse:
    storage = {'Принтеры': [],
               'Сканеры': [],
               'Копиры': []}

    @staticmethod
    def show_storage():
        for key, value in Warehouse.storage.items():
            print(f'-----{key}-----')
            for val in value:
                print(val)


class OfficeEquipment:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.set_quantity(quantity)

    def set_quantity(self, quantity):
        if type(quantity) is not str:
            self.quantity = quantity
        else:
            raise Exception('Количество не должно быть строкой!')


class Printer(OfficeEquipment):
    def __init__(self, brand, price, quantity, print_speed):
        super().__init__(brand, price, quantity)
        self.print_speed = print_speed

    def __str__(self):
        return f'Модель: {self.name}, Скорость печати: {self.print_speed} стр./мин., Цена: {self.price} долл., ' \
               f'Кол-во: {self.quantity} шт.'

    def printer_add(self):
        return Warehouse.storage['Принтеры'].append(self.__str__())


class Scanner(OfficeEquipment):
    def __init__(self, brand, price, quantity, resolution):
        super().__init__(brand, price, quantity)
        self.resolution = resolution

    def __str__(self):
        return f'Модель: {self.name}, Разрешение: {self.resolution} точ./дюйм, Цена: {self.price} долл., ' \
               f'Кол-во: {self.quantity} шт.'

    def scanner_add(self):
        return Warehouse.storage['Сканеры'].append(self.__str__())


class Copier(OfficeEquipment):
    def __init__(self, brand, price, quantity, copy_speed):
        super().__init__(brand, price, quantity)
        self.copy_speed = copy_speed

    def __str__(self):
        return f'Модель: {self.name}, Скорость копирования: {self.copy_speed} стр./мин., Цена: {self.price} долл., ' \
               f'Кол-во: {self.quantity} шт.'

    def copier_add(self):
        return Warehouse.storage['Копиры'].append(self.__str__())


hp1 = Printer('HP 107a', 100, 3, 20)
kc1 = Printer('Kyocera P2335d', 200, 2, 35)
hp2 = Printer('HP M406', 500, 1, 40)
Printer.printer_add(hp1)
Printer.printer_add(kc1)
Printer.printer_add(hp2)

ep1 = Scanner('Epson V19', 100, 2, 4800)
cn1 = Scanner('Canon P-215', 200, 1, 600)
Scanner.scanner_add(ep1)
Scanner.scanner_add(cn1)

br1 = Copier('Brother L2500', 250, 2, 26)
xe1 = Copier('Xerox 3025V', 150, 1, 20)
Copier.copier_add(br1)
Copier.copier_add(xe1)

Warehouse.show_storage()
