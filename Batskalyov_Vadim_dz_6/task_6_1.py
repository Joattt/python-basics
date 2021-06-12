# 1. Не используя библиотеки для парсинга, распарсить (получить определённые данные) файл логов
# web-сервера nginx_logs.txt
# (https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs)
# — получить список кортежей вида: (<remote_addr>, <request_type>,
# <requested_resource>). Например:
# [
# ...
# ('141.138.90.60', 'GET', '/downloads/product_2'),
# ('141.138.90.60', 'GET', '/downloads/product_2'),
# ('173.255.199.22', 'GET', '/downloads/product_2'),
# ...
# ]

logs_list = []

with open('nginx_logs.txt', encoding='utf-8') as f:
    for line in f:
        remote_addr = line[:line.find(' ')]
        request_type = line[line.find('"') + 1:line.find(' ', line.find('"'))]
        requested_resource = line[line.find('/', line.find('"')):line.find(' ', line.find('/', line.find('"')))]
        logs_list.append((remote_addr, request_type, requested_resource))

print(logs_list)
