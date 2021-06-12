# 2. *(вместо 1) Найти IP адрес спамера и количество отправленных им запросов по данным файла
# логов из предыдущего задания.
# Примечание: спамер — это клиент, отправивший больше всех запросов; код должен работать
# даже с файлами, размер которых превышает объем ОЗУ компьютера.

from collections import Counter

logs_list = []

with open('nginx_logs.txt', encoding='utf-8') as f:
    for line in f:
        remote_addr = line[:line.find(' ')]
        logs_list.append(remote_addr)

addr_count = Counter(logs_list)
print(addr_count)
max_requests = max(addr_count.values())
max_requests_addr = list(addr_count.keys())[list(addr_count.values()).index(max_requests)]
print(f'Адрес спамера: {max_requests_addr}, количество запросов: {max_requests}.')
