# 5. *(вместо 4) Написать скрипт, который выводит статистику для заданной папки в виде словаря,
# в котором ключи те же, а значения — кортежи вида (<files_quantity>,
# [<files_extensions_list>]), например:
# {
# 100: (15, ['txt']),
# 1000: (3, ['py', 'txt']),
# 10000: (7, ['html', 'css']),
# 100000: (2, ['png', 'jpg'])
# }
# Сохраните результаты в файл <folder_name>_summary.json в той же папке, где запустили
# скрипт.

import os
import json

folder_path = r'./'

stat_dict = {
    100: 0,
    1000: 0,
    10000: 0,
    100000: 0
}

count_100 = 0
count_1000 = 0
count_10000 = 0
count_100000 = 0
ext_100 = []
ext_1000 = []
ext_10000 = []
ext_100000 = []

for root, dirs, files in os.walk(folder_path):
    for file in files:
        if os.stat(os.path.join(root, file)).st_size <= 100:
            count_100 += 1
            ext_100.append(os.path.splitext(file)[1].strip('.'))
        elif 100 < os.stat(os.path.join(root, file)).st_size <= 1000:
            count_1000 += 1
            ext_1000.append(os.path.splitext(file)[1].strip('.'))
        elif 1000 < os.stat(os.path.join(root, file)).st_size <= 10000:
            count_10000 += 1
            ext_10000.append(os.path.splitext(file)[1].strip('.'))
        else:
            count_100000 += 1
            ext_100000.append(os.path.splitext(file)[1].strip('.'))

stat_dict[100] = (count_100, list(set(ext_100)))
stat_dict[1000] = (count_1000, list(set(ext_1000)))
stat_dict[10000] = (count_10000, list(set(ext_10000)))
stat_dict[100000] = (count_100000, list(set(ext_100000)))

print(stat_dict)

with open(f'{os.path.basename(os.getcwd())}_summary.json', 'w') as f:
    json.dump(stat_dict, f)
