# 3. *(вместо задачи 2) Решить задачу 2 не создавая новый список (как говорят, in place). Эта задача
# намного серьёзнее, чем может сначала показаться.

my_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']


def is_number(my_str):
    try:
        int(my_str)
        return True
    except ValueError:
        return False


index_count = 0
pass_count = 0

for element in my_list:
    if pass_count == 0:
        if is_number(element):
            if element[0] != '+':
                popped_element = my_list.pop(my_list.index(element, index_count))
                my_list.insert(index_count, '"')
                my_list.insert(index_count, f'{int(popped_element):02d}')
                my_list.insert(index_count, '"')
                index_count += 1
                pass_count += 2
            else:
                popped_element = my_list.pop(my_list.index(element, index_count))
                my_list.insert(index_count, '"')
                my_list.insert(index_count, f'+{int(popped_element):02d}')
                my_list.insert(index_count, '"')
                index_count += 1
                pass_count += 2
        else:
            popped_element = my_list.pop(my_list.index(element, index_count))
            my_list.insert(index_count, popped_element)
            index_count += 1
    elif pass_count == 2:  # пропускаем одну итерацию, после того как добавили в список число с кавычками
        pass_count -= 1
        index_count += 1
    elif pass_count == 1:  # пропускаем еще одну итерацию
        pass_count -= 1
        index_count += 1

print(my_list)
print()

# Сформировать из обработанного списка строку:
# в "05" часов "17" минут температура воздуха была "+05" градусов

index_count = 0

for element in my_list:
    if element != '"':
        index_count += 1
    else:
        my_list.remove('"')
        my_list.remove('"')
        popped_element = my_list.pop(index_count)
        my_list.insert(index_count, f'"{popped_element}"')
        index_count += 1
print(' '.join(my_list))
