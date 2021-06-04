# 2. Написать функцию currency_rates(), принимающую в качестве аргумента код валюты
# (например, USD, EUR, GBP, ...) и возвращающую курс этой валюты по отношению к рублю.
# Использовать библиотеку requests. В качестве API можно использовать
# http://www.cbr.ru/scripts/XML_daily.asp. Рекомендация: выполнить предварительно запрос к API
# в обычном браузере, посмотреть содержимое ответа. Можно ли, используя только методы класса
# str, решить поставленную задачу? Функция должна возвращать результат числового типа,
# например float. Подумайте: есть ли смысл для работы с денежными величинами использовать
# вместо float тип Decimal? Сильно ли усложняется код функции при этом? Если в качестве
# аргумента передали код валюты, которого нет в ответе, вернуть None. Можно ли сделать работу
# функции не зависящей от того, в каком регистре был передан аргумент? В качестве примера
# выведите курсы доллара и евро.

from requests import get
from decimal import Decimal


def currency_rates(currency):
    response = get('http://www.cbr.ru/scripts/XML_daily.asp').text
    currency_idx = response.find((currency.upper()))
    if currency_idx != -1:
        rate_idx = response.find('</Value>', currency_idx)
        rate = Decimal(response[rate_idx - 7:rate_idx].replace(',', '.'))
        return rate
    else:
        return None


print(currency_rates('usd'))
print(currency_rates('Eur'))
print(currency_rates('тугрик'))
