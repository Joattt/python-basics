# 4. Написать свой модуль utils и перенести в него функцию currency_rates() из предыдущего
# задания. Создать скрипт, в котором импортировать этот модуль и выполнить несколько вызовов
# функции currency_rates(). Убедиться, что ничего лишнего не происходит.

import utils

print(utils.currency_rates('usd'))
print(utils.currency_rates('Eur'))
print(utils.currency_rates('тугрик'))
