# 1. Реализовать вывод информации о промежутке времени в зависимости от его
# продолжительности duration в секундах:
# a. до минуты: <s> сек;
# b. до часа: <m> мин <s> сек;
# c. до суток: <h> час <m> мин <s> сек;
# d. * в остальных случаях: <d> дн <h> час <m> мин <s> сек.

duration = int(input('Введите количество секунд: '))

if 0 <= duration < 60:
    print(duration, 'сек')
elif 60 <= duration < 3600:
    minutes = duration // 60
    seconds = duration % 60
    print(minutes, 'мин', seconds, 'сек')
elif 3600 <= duration < 86400:
    hours = duration // 3600
    minutes = (duration - hours * 3600) // 60
    seconds = (duration - hours * 3600 - minutes * 60) % 60
    print(hours, 'час', minutes, 'мин', seconds, 'сек')
else:
    days = duration // 86400
    hours = (duration - days * 86400) // 3600
    minutes = (duration - days * 86400 - hours * 3600) // 60
    seconds = (duration - days * 86400 - hours * 3600 - minutes * 60) % 60
    print(days, 'дн', hours, 'час', minutes, 'мин', seconds, 'сек')

