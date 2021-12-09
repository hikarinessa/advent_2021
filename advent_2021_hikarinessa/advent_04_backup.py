# https://adventofcode.com/2021/day/4
# region ---- imports ----
import os
import sys

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
              '14 21 17 24  4',
              '10 16 15  9 19',
              '18  8 23 26 20',
              '22 11 13  6  5',
              '2  0 12  3  7']
# endregion --------------


class Board:
    def __init__(self, input):
        self.rows_columns = input.copy()
        for i in range(0, len(input[0])):
            column = []
            for row in input:
                column.append(row[i])
            self.rows_columns.append(column)

    def check_num(self, number):
        for j, row in enumerate(self.rows_columns):
            print(row)
            for i, item in enumerate(row):
                if item == number:
                    row[i] = None
            print(number, row)
            self.rows_columns[j] = [k for k in row if k is not None]
        # print(number)
        # print(self.rows_columns)

    def check_win(self):
        for row in self.rows_columns:
            if len(row) == 0:
                return True
            else:
                return False

    def score(self, number):
        score = 0
        for row in self.rows_columns:
            if len(row) > 0:
                for col in row:
                    score += col
        score = int(score/2)*number
        return score


# part 1
def process_input(input):
    input.reverse()  # pop operates back to front, so I reverse the order
    bingo_list = input.pop()
    bingo_list = [int(i) for i in bingo_list.split(',')]
    input.pop()  # deletes the first empty line
    boards = []
    board = []
    while len(input) > 0:
        item = input.pop()
        if item != '':
            item = [int(i) for i in item.split(' ') if i != '']
            board.append(item)
        else:
            boards.append(Board(board))
            board = []
    boards.append(Board(board))
    return bingo_list, boards


def call_nums(numbers, boards):
    for number in numbers:
        for board in boards:
            board.check_num(number)
            if board.check_win():
                return board.score(number)


if __name__ == "__main__":
    bingo_list, boards = process_input(INPUT)
    print('Part 1 =', call_nums(bingo_list, boards))  # 37240 is low
    print('*'*30)
    print('Part 2 =', '')  #
