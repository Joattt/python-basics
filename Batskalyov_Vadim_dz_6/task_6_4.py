# 4. *(вместо 3) Решить задачу 3 для ситуации, когда объём данных в файлах превышает объём
# ОЗУ (разумеется, не нужно реально создавать такие большие файлы, это просто задел на
# будущее проекта). Только теперь не нужно создавать словарь с данными. Вместо этого нужно
# сохранить объединенные данные в новый файл (users_hobby.txt). Хобби пишем через
# двоеточие и пробел после ФИО:
# Иванов,Иван,Иванович: скалолазание,охота
# Петров,Петр,Петрович: горные лыжи

from itertools import zip_longest

with open('users.csv', encoding='utf-8') as f_1, open('hobby.csv', 'r', encoding='utf-8') as f_2:
    with open('users_hobby.txt', 'a', encoding='utf-8') as f_3:
        for line_1, line_2 in zip_longest(f_1, f_2):
            if line_1 !=None and line_2 !=None:
                f_3.writelines(f'{line_1.strip()}: {line_2.strip()}\n')
            elif line_2 == None:
                f_3.writelines(f'{line_1.strip()}: {None}\n')
            else:
                exit('1')
