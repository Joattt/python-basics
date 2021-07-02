# == Лото ==
# Правила игры в лото.
# Игра ведется с помощью спе циальных карточек, на которых отмечены числа,
# и фишек (бочонков) с цифрами.
# Количество бочонков — 90 штук (с цифрами от 1 до 90).
# Каждая карточка содержит 3 строки по 9 клеток. В каждой строке по 5 случайных цифр,
# расположенных по возрастанию. Все цифры в карточке уникальны. Пример карточки:
#
# --------------------------
#     9 43 62          74 90
#  2    27    75 78    82
#    41 56 63     76      86
# --------------------------
#
# В игре 2 игрока: пользователь и компьютер. Каждому в начале выдается
# случайная карточка.
#
# Каждый ход выбирается один случайный бочонок и выводится на экран.
# Также выводятся карточка игрока и карточка компьютера.
#
# Пользователю предлагается зачеркнуть цифру на карточке или продолжить.
# Если игрок выбрал "зачеркнуть":
#     Если цифра есть на карточке - она зачеркивается и игра продолжается.
#     Если цифры на карточке нет - игрок проигрывает и игра завершается.
# Если игрок выбрал "продолжить":
#     Если цифра есть на карточке - игрок проигрывает и игра завершается.
#     Если цифры на карточке нет - игра продолжается.
#
# Побеждает тот, кто первый закроет все числа на своей карточке.
# Пример одного хода:
# Новый бочонок: 70 (осталось 76)
# ------ Ваша карточка -----
#  6  7          49    57 58
#    14 26     -    78    85
# 23 33    38    48    71
# --------------------------
# -- Карточка компьютера ---
#  7 87     - 14    11
#       16 49    55 88    77
#    15 20     -       76  -
# --------------------------
# Зачеркнуть цифру? (y/n)
#
# Подсказка: каждый следующий случайный бочонок из мешка удобно получать
# с помощью функции-генератора.
#
# Подсказка: для работы с псевдослучайными числами удобно использовать
# модуль random: http://docs.python.org/3/library/random.html

import random


class LottoCard:
    def __init__(self, player_type):
        self.player_type = player_type
        self._card = [
            [],
            [],
            []
        ]
        self._MAX_NUMBER = 90
        self._MAX_NUMBER_IN_CARD = 15
        self._numbers_stroked = 0
        NEED_SPACES = 4
        NEED_NUMBERS = 5
        self._numbers = random.sample(range(1, self._MAX_NUMBER), self._MAX_NUMBER_IN_CARD)

        for line in self._card:
            for _ in range(NEED_SPACES):
                line.append(' ')
            for _ in range(NEED_NUMBERS):
                line.append(self._numbers.pop())

        def check_sort_item(item):
            if isinstance(item, int):
                return item
            else:
                return random.randint(1, self._MAX_NUMBER)

        for index, line in enumerate(self._card):
            self._card[index] = sorted(line, key=check_sort_item)

    def has_number(self, number):
        for i in range(len(self._card)):
            if number in self._card[i]:
                return True
            elif i == len(self._card) - 1:
                return False

    @staticmethod
    def stroke(player_card):
        for line in player_card:
            for number in line:
                if number == game.current_barrel:
                    player_card[player_card.index(line)][line.index(number)] = ' -'

    @staticmethod
    def check_stroked_all(player_card, player_flag):
        player_nums = []
        for line in player_card:
            for number in line:
                if type(number) is int:
                    player_nums.append(number)
        if len(player_nums) == 0:
            if player_flag == 'hum':
                game.human_stroked_all = 1
            elif player_flag == 'comp':
                game.computer_stroked_all = 1

    def __str__(self):
        self.str_card = [[str(el) if len(str(el)) == 2 else f' {str(el)}' for el in line] for line in self._card]
        n1 = "\n"
        return f'{"-" * 26}\n{n1.join([" ".join(line) for line in self.str_card])}\n{"-" * 26}'


class LottoGame:

    def __init__(self, human, computer):
        self.human = human
        self.computer = computer
        self.turn_count = 1
        self.total_turns = 90
        self.current_barrel = 0
        self.human_stroked_all = 0
        self.computer_stroked_all = 0

    def start(self):
        print('Игра началась!')
        barrels = list(range(1, 91))
        random.shuffle(barrels)
        for barrel in barrels:
            self.current_barrel = barrel
            print(f'{self.human.player_type}:')
            print(self.human)
            print(f'{self.computer.player_type}:')
            print(self.computer)
            print(f'Новый бочонок: {barrel}, осталось: {self.total_turns - self.turn_count}.')
            print('Хотите зачеркнуть? y/n:')
            user_answer = input()
            while user_answer != 'y' and user_answer != 'n':
                user_answer = input('Вы ввели неверное значение, введите "y" либо "n":')
            if user_answer == 'y' and self.human.has_number(barrel) is False:
                return print('У вас не было такого номера! Вы проиграли!')
            elif user_answer == 'n' and self.human.has_number(barrel) is True:
                return print('У вас был такой номер! Вы проиграли!')
            if self.human.has_number(self.current_barrel):
                LottoCard.stroke(game.human._card)
                LottoCard.check_stroked_all(game.human._card, 'hum')
            if self.computer.has_number(self.current_barrel):
                LottoCard.stroke(game.computer._card)
                LottoCard.check_stroked_all(game.computer._card, 'comp')
            if self.human_stroked_all == 1 and self.computer_stroked_all == 1:
                print('Ничья!')
                break
            elif self.human_stroked_all == 1:
                print('Вы победили!')
                break
            elif self.computer_stroked_all == 1:
                print(f'{self.computer.player_type} победил!')
                break
            else:
                self.turn_count += 1


game = LottoGame(LottoCard('Игрок Валера'), LottoCard('Робот Федор'))
game.start()
