# 7. *(вместо 6) Добавить возможность редактирования данных при помощи отдельного скрипта:
# передаём ему номер записи и новое значение. При этом файл не должен читаться целиком —
# обязательное требование. Предусмотреть ситуацию, когда пользователь вводит номер записи,
# которой не существует.

import sys

line_num = sys.argv[1]
new_amount = sys.argv[2]

with open('bakery.csv', encoding='utf-8') as f:
    if not 0 < int(line_num) <= sum(1 for line in f):
        exit('Вы ввели несуществующий номер записи!')
    else:
        f.seek(0)
        for num, line in enumerate(f, 1):
            if num == int(line_num):
                old_amount = line
        f.seek(0)
        list_original = [line for line in f]
        list_corrected = [line if line != old_amount else f'{new_amount}\n' for line in list_original]

with open('bakery.csv', 'w', encoding='utf-8') as f:
    for line in list_corrected:
        f.write(line)
