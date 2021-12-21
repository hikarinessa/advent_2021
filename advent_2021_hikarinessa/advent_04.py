# https://adventofcode.com/2021/day/4
# region ---- imports and inputs ----
import os
import sys
import pprint
import copy

with open(os.path.join(sys.path[0], "Inputs/advent_04_input.txt"), "r") as raw_input:
    INPUT = raw_input.read().splitlines()

TEST_INPUT = ['7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1',
              '',
              '22 13 17 11  0',
              '8  2 23  4 24',
              '21  9 14 16  7',
              '6 10  3 18  5',
              '1 12 20 15 19',
              '',
              '3 15  0  2 22',
              '9 18 13 17  5',
              '19  8  7 25 23',
              '20 11 10 24  4',
              '14 21 16 12  6',
              '',
              '10 16 15  9 19',
              '14 21 17 24  4',
              '18  8 23 26 20',
              '22 11 13  6  5',
              '2  0 12  3  7']
# endregion -------------------------
debug = False

# BINGO
# The score of the board is calculated by finding the sum of all unmarked numbers on that board.
# Then, multiply that sum by the number that was just called when the board won.


class Board:
    def __init__(self, input):
        self.original = input
        self.rows_columns = copy.deepcopy(input)
        for i in range(0, len(input[0])):
            column = []
            for row in input:
                column.append(row[i])
            self.rows_columns.append(column)

    def check_num(self, number):
        for row in self.rows_columns:
            for i, item in enumerate(row):
                if item == number:
                    row[i] = None

    def check_win(self):
        for row in self.rows_columns:
            victory = [k for k in row if k is not None]
            if len(victory) == 0:
                return True
            else:
                pass

    def score(self, number):
        score = 0
        rows = self.rows_columns[0:5]
        if debug: self.print_original()
        if debug: self.print_state()
        for row in rows:
            for col in row:
                if col is not None:
                    score += col
        score = score * number
        return score

    def print_original(self):
        pprint.pprint(self.original)

    def print_state(self):
        rows = self.rows_columns[0:5]
        pprint.pprint(rows)


def process_input(input):
    input.reverse()  # pop operates back to front, so I reverse the order
    bingo_list = input.pop()
    bingo_list = [int(i) for i in bingo_list.split(',')]
    input.pop()  # deletes the first empty line
    boards = []
    wip_board = []
    while len(input) > 0:
        item = input.pop()
        if item != '':
            item = [int(i) for i in item.split(' ') if i]
            wip_board.append(item)
        else:
            boards.append(Board(wip_board))
            wip_board = []
    boards.append(Board(wip_board))
    return bingo_list, boards


# part 1
# Get the score of the board that wins
def find_winner(numbers, boards):
    for number in numbers:
        if debug: print(number)
        for board in boards:
            board.check_num(number)
            if board.check_win():
                return board.score(number)


# part 2
# Get the score of the board that loses
def find_loser(numbers, boards):
    boards_copy = boards.copy()
    while len(boards_copy) > 1:
        for number in numbers:
            if debug: print(number)
            for i, board in enumerate(boards_copy):
                board.check_num(number)
                if board.check_win():
                    if len(boards_copy) == 1:
                        return board.score(number)
                    else:
                        boards_copy[i] = None
            boards_copy = [i for i in boards_copy if i is not None]


if __name__ == "__main__":
    bingo_list, boards = process_input(INPUT)
    # boards[0].print_original()
    print('Part 1 =', find_winner(bingo_list, boards))  # 69579
    print('*'*30)
    print('Part 2 =', find_loser(bingo_list, boards))  # 14877
