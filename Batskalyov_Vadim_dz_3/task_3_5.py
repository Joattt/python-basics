# 5. Реализовать функцию get_jokes(), возвращающую n шуток, сформированных из трех
# случайных слов, взятых из трёх списков (по одному из каждого):
# nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
# adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
# adjectives = ["веселый", "яркий", "зеленый", "утопичный",
# "мягкий"]
# Например:
# >>> get_jokes(2)
# ["лес завтра зеленый", "город вчера веселый"]
# Документировать код функции.
# Сможете ли вы добавить еще один аргумент — флаг, разрешающий или запрещающий повторы
# слов в шутках (когда каждое слово можно использовать только в одной шутке)? Сможете ли вы
# сделать аргументы именованными?

from random import choice


def get_jokes(n=0, repeat=True):
    """Composes a list of stupid jokes"""
    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
    count = n
    jokes = []
    while count > 0:
        if repeat:
            jokes.append(f'{choice(nouns)} {choice(adverbs)} {choice(adjectives)}')
            count -= 1
        else:
            joke = f'{choice(nouns)} {choice(adverbs)} {choice(adjectives)}'
            jokes.append(joke)
            nouns.remove(joke.split(' ')[0])
            adverbs.remove(joke.split(' ')[1])
            adjectives.remove(joke.split(' ')[2])
            count -= 1
    return jokes


print(get_jokes(5, False))
