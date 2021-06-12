# 5. **(вместо 4) Решить задачу 4 и реализовать интерфейс командной строки, чтобы можно было
# задать имя обоих исходных файлов и имя выходного файла. Проверить работу скрипта.

from itertools import zip_longest
import sys


def f_users_hobby(file_users, file_hobby, file_final):
    with open(file_users, encoding='utf-8') as f_1, open(file_hobby, 'r', encoding='utf-8') as f_2:
        with open(file_final, 'a', encoding='utf-8') as f_3:
            for line_1, line_2 in zip_longest(f_1, f_2):
                if line_1 != None and line_2 != None:
                    f_3.writelines(f'{line_1.strip()}: {line_2.strip()}\n')
                elif line_2 == None:
                    f_3.writelines(f'{line_1.strip()}: {None}\n')
                else:
                    exit('1')


f_users_hobby(sys.argv[1], sys.argv[2], sys.argv[3])
