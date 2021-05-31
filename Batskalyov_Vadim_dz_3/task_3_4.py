# 4. *(вместо задачи 3) Написать функцию thesaurus_adv(), принимающую в качестве аргументов
# строки в формате «Имя Фамилия» и возвращающую словарь, в котором ключи — первые буквы
# фамилий, а значения — словари, реализованные по схеме предыдущего задания и содержащие
# записи, в которых фамилия начинается с соответствующей буквы. Например:
# >>> thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр
# Алексеев", "Илья Иванов", "Анна Савельева")
# {
# "А": {
# "П": ["Петр Алексеев"]
# },
# "С": {
# "И": ["Иван Сергеев", "Инна Серова"],
# "А": ["Анна Савельева"]
# }
# }


def thesaurus(*args):
    my_dict = {}
    for name in args:
        surname_letter = name.split(' ')[1][0]
        if surname_letter not in my_dict:
            dict_2 = {}
            dict_2.setdefault(name[0], [name])
            my_dict.setdefault(surname_letter, dict_2)
        else:
            if name[0] not in my_dict[surname_letter]:
                my_dict[surname_letter].setdefault(name[0], [name])
            else:
                my_dict[surname_letter][name[0]].append(name)
    return my_dict


print(thesaurus('Иван Сергеев', 'Инна Серова', 'Петр Алексеев', 'Илья Иванов', 'Анна Савельева'))
print()

# Как поступить, если потребуется сортировка по ключам?

my_dict = thesaurus('Иван Сергеев', 'Инна Серова', 'Петр Алексеев', 'Илья Иванов', 'Анна Савельева', 'Дмитрий Кузнецов',
                    'Константин Воронов', 'Василий Власов', 'Виктор Воробьев')
print(my_dict)

my_dict_sorted = {}
list_keys = list(my_dict)
list_keys.sort()
for key in list_keys:
    my_dict_sorted.setdefault(key, my_dict[key])
print(my_dict_sorted)
