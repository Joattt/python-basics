# 3. Реализовать склонение слова «процент» для чисел до 20. Например, задаем число 5 —
# получаем «5 процентов», задаем число 2 — получаем «2 процента». Вывести все склонения
# для проверки.


def number_percent(num):
    if num == 1:
        percent_word = 'процент'
    elif 2 <= num <= 4:
        percent_word = 'процента'
    else:
        percent_word = 'процентов'
    return f'{num} {percent_word}'


number = int(input('Введите процент от 0 до 20: '))
print('Результат:', number_percent(number))


print('Все склонения:')
for number in range(0, 21):
    print(number_percent(number))
