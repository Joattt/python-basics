# 6. Реализовать простую систему хранения данных о суммах продаж булочной. Должно быть два
# скрипта с интерфейсом командной строки: для записи данных и для вывода на экран
# записанных данных. При записи передавать из командной строки значение суммы продаж.

import sys


def add_s(amount):
    with open('bakery.csv', 'a', encoding='utf-8') as f:
        f.writelines(f'{amount}\n')


add_s(sys.argv[1])
