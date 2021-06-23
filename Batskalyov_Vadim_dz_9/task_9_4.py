# 4. Реализуйте базовый класс Car:
# ● у класса должны быть следующие атрибуты: speed, color, name, is_police (булево). А
# также методы: go, stop, turn(direction), которые должны сообщать, что машина
# поехала, остановилась, повернула (куда);
# ● опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
# ● добавьте в базовый класс метод show_speed, который должен показывать текущую
# скорость автомобиля;
# ● для классов TownCar и WorkCar переопределите метод show_speed. При значении
# скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о
# превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам,
# выведите результат. Вызовите методы и покажите результат.

class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'Автомобиль {self.name} поехал.')

    def stop(self):
        print(f'Автомобиль {self.name} остановился.')

    def turn(self, direction):
        if direction == 'left':
            print(f'Автомобиль {self.name} повернул налево.')
        elif direction == 'right':
            print(f'Автомобиль {self.name} повернул направо.')

    def show_speed(self):
        print(f'Скорость автомобиля {self.name} - {self.speed} км/ч.')


class TownCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed > 60:
            print('Превышение скорости!')


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed > 40:
            print('Превышение скорости!')


class PoliceCar(Car):
    pass


town_car = TownCar(80, 'черный', 'Nissan', False)
sports_car = SportCar(250, 'красный', 'Ferrari', False)
work_car = WorkCar(25, 'синий', 'Камаз', False)
police_car = PoliceCar(70, 'белый', 'УАЗ', True)

town_car.show_speed()
sports_car.show_speed()
work_car.go()
police_car.turn('left')
print(police_car.speed)
print(town_car.name)
