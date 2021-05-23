# 2. Создать список, состоящий из кубов нечётных чисел от 1 до 1000:

my_list = []

for number in range(1, 1000):
    if number % 2:
        my_list.append(number ** 3)
print(my_list)


# a. Вычислить сумму тех чисел из этого списка, сумма цифр которых делится нацело на 7.
# Например, число «19 ^ 3 = 6859» будем включать в сумму, так как 6 + 8 + 5 + 9 = 28 –
# делится нацело на 7. Внимание: использовать только арифметические операции!


def sum_digits(num):
    sum_dig = 0
    while num > 0:
        sum_dig += num % 10
        num //= 10
    return sum_dig


sum_numbers = 0

for number in my_list:
    if not sum_digits(number) % 7:
        sum_numbers += number
print(sum_numbers)

# b. К каждому элементу списка добавить 17 и заново вычислить сумму тех чисел из этого
# списка, сумма цифр которых делится нацело на 7.

new_list = []

for number in my_list:
    new_list.append(number + 17)
print(new_list)

sum_numbers = 0

for number in new_list:
    if not sum_digits(number) % 7:
        sum_numbers += number
print(sum_numbers)

# c. * Решить задачу под пунктом b, не создавая новый список.

sum_numbers_2 = 0

for number in my_list:
    if not sum_digits(number + 17) % 7:
        sum_numbers_2 += number + 17
print(sum_numbers_2)
