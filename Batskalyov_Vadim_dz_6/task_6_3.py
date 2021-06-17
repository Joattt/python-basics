# 3. Есть два файла: в одном хранятся ФИО пользователей сайта, а в другом — данные об их хобби.
# Известно, что при хранении данных используется принцип: одна строка — один пользователь,
# разделитель между значениями — запятая. Написать код, загружающий данные из обоих файлов
# и формирующий из них словарь: ключи — ФИО, значения — данные о хобби. Сохранить словарь
# в файл. Проверить сохранённые данные. Если в файле, хранящем данные о хобби, меньше
# записей, чем в файле с ФИО, задаём в словаре значение None. Если наоборот — выходим из
# скрипта с кодом «1». При решении задачи считать, что объём данных в файлах во много раз
# меньше объема ОЗУ.
# Фрагмент файла с данными о пользователях (users.csv):
# Иванов,Иван,Иванович
# Петров,Петр,Петрович
# Фрагмент файла с данными о хобби (hobby.csv):
# скалолазание,охота
# горные лыжи

from itertools import zip_longest
import json

text_users = """Иванов,Иван,Иванович
Петров,Петр,Петрович
Бородач,Александр,Родионович"""
with open('users.csv', 'w', encoding='utf-8') as f_1:
    f_1.write(text_users)

text_hobby = """скалолазание,охота
горные лыжи"""
with open('hobby.csv', 'w', encoding='utf-8') as f_2:
    f_2.write(text_hobby)

users_list = []
with open('users.csv', encoding='utf-8') as f_1:
    for line in f_1:
        users_list.append(line.strip())
print(users_list)

hobby_list = []
with open('hobby.csv', encoding='utf-8') as f_2:
    for line in f_2:
        hobby_list.append(line.strip())
print(hobby_list)

if len(users_list) >= len(hobby_list):
    users_dict = dict(zip_longest(users_list, hobby_list))
    print(users_dict)
else:
    exit('1')

with open('users.json', 'w', encoding='utf-8') as f_3:
    json.dump(users_dict, f_3)

with open('users.json', 'r', encoding='utf-8') as f_3:
    print(json.load(f_3))
