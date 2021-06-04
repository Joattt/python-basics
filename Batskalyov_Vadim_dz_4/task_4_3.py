# 3. *(вместо 2) Доработать функцию currency_rates(): теперь она должна возвращать кроме курса
# дату, которая передаётся в ответе сервера. Дата должна быть в виде объекта date. Подумайте,
# как извлечь дату из ответа, какой тип данных лучше использовать в ответе функции?

from requests import get
from decimal import Decimal
from datetime import date


def currency_rates(currency):
    response = get('http://www.cbr.ru/scripts/XML_daily.asp').text
    currency_idx = response.find((currency.upper()))
    if currency_idx != -1:
        rate_idx = response.find('</Value>', currency_idx)
        rate = Decimal(response[rate_idx - 7:rate_idx].replace(',', '.'))
        date_idx = response.find('Date="')
        day = int(response[date_idx + 6:date_idx + 8])
        month = int(response[date_idx + 9:date_idx + 11])
        year = int(response[date_idx + 12:date_idx + 16])
        rate_date = date(year, month, day)
        return f'{rate}, {rate_date}'
    else:
        return None


print(currency_rates('usd'))
print(currency_rates('Eur'))
print(currency_rates('тугрик'))
