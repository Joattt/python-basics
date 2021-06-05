from requests import get
from decimal import Decimal
from datetime import date


def currency_rates(currency):
    response = get('http://www.cbr.ru/scripts/XML_daily.asp').text
    currency_idx = response.find((currency.upper()))
    if currency_idx != -1:
        rate_str = response[response.find('<Value>', currency_idx) + 7:response.find('</Value>', currency_idx)]
        rate = Decimal(rate_str.replace(',', '.'))
        date_idx = response.find('Date="')
        day = int(response[date_idx + 6:date_idx + 8])
        month = int(response[date_idx + 9:date_idx + 11])
        year = int(response[date_idx + 12:date_idx + 16])
        rate_date = date(year, month, day)
        return f'{rate}, {rate_date}'
    else:
        return None
