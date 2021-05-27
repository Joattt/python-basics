# 2. Дан список:
# ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха',
# 'была', '+5', 'градусов']
# Необходимо его обработать — обособить каждое целое число (вещественные не трогаем)
# кавычками (добавить кавычку до и кавычку после элемента списка, являющегося числом) и
# дополнить нулём до двух целочисленных разрядов:
# ['в', '"', '05', '"', 'часов', '"', '17', '"', 'минут',
# 'температура', 'воздуха', 'была', '"', '+05', '"', 'градусов']

my_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
new_list = []


def is_number(my_str):
    try:
        int(my_str)
        return True
    except ValueError:
        return False


for element in my_list:
    if is_number(element):
        if element[0] != '+':
            new_list.append('"')
            new_list.append(f'{int(element):02d}')
            new_list.append('"')
        else:
            new_list.append('"')
            new_list.append(f'+{int(element):02d}')
            new_list.append('"')
    else:
        new_list.append(element)

print(new_list)
print()

# Сформировать из обработанного списка строку:
# в "05" часов "17" минут температура воздуха была "+05" градусов
# Подумать, какое условие записать, чтобы выявить числа среди элементов списка? Как
# модифицировать это условие для чисел со знаком?
# Примечание: если обособление чисел кавычками не будет получаться - можете вернуться к его
# реализации позже. Главное: дополнить числа до двух разрядов нулём!

index_count = 0

for element in new_list:
    if element != '"':
        index_count += 1
    else:
        new_list.remove('"')
        new_list.remove('"')
        popped_element = new_list.pop(index_count)
        new_list.insert(index_count, f'"{popped_element}"')
        index_count += 1

print(new_list)  # объединили число и кавычки в один элемент списка
print(' '.join(new_list))
