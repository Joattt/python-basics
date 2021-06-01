# 3. Написать функцию thesaurus(), принимающую в качестве аргументов имена сотрудников и
# возвращающую словарь, в котором ключи — первые буквы имён, а значения — списки,
# содержащие имена, начинающиеся с соответствующей буквы. Например:
# >>> thesaurus("Иван", "Мария", "Петр", "Илья")
# {
# "И": ["Иван", "Илья"],
# "М": ["Мария"], "П": ["Петр"]
# }


def thesaurus(*args):
    my_dict = {}
    for name in args:
        if name[0] not in my_dict:
            my_dict.setdefault(name[0], [name])
        else:
            my_dict[name[0]].append(name)
    return my_dict


print(thesaurus('Иван', 'Мария', 'Петр', 'Илья'))
print()

# Подумайте: полезен ли будет вам оператор распаковки? Как поступить, если потребуется
# сортировка по ключам? Можно ли использовать словарь в этом случае?

my_dict = thesaurus('Иван', 'Мария', 'Петр', 'Илья', 'Алексей', 'Василий', 'Анна')
print(my_dict)

my_dict_sorted = {}
list_keys = list(my_dict)
list_keys.sort()
for key in list_keys:
    my_dict_sorted.setdefault(key, my_dict[key])
print(my_dict_sorted)
