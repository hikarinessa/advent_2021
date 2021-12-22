# https://adventofcode.com/2021/day/13
# region ---- imports ----
import os
import sys
import re
import pprint

with open(os.path.join(sys.path[0], "Inputs/advent_13_input.txt"), "r") as raw_input:
    INPUT = raw_input.read().splitlines()

TEST_INPUT = ['6,10', '0,14', '9,10', '0,3', '10,4', '4,11', '6,0', '6,12', '4,1',
              '0,13', '10,12', '3,4', '3,0', '8,4', '1,10', '2,14', '8,10', '9,0',
              '',
              'fold along y=7',
              'fold along x=5']
# endregion --------------
debug = True


def parse_input(input):
    # find the empty row and use it as a delimiter
    delimiter = 0
    for ind, line in enumerate(input):
        if line == '':
            delimiter = ind
    # the dots are before the delimiter, get coordinates and make them into a grid
    dots = input[:delimiter]
    dots = [i.split(',') for i in dots]
    dots = [[int(j) for j in i] for i in dots]
    # make the grid to the max size of inputs
    x_len = 0
    y_len = 0
    for item in dots:
        if item[0] > x_len:
            x_len = item[0]
        if item[1] > y_len:
            y_len = item[1]
    x_len, y_len = x_len+1, y_len+1
    dots_grid = ['.'*x_len]*y_len
    # add the dots to the grid
    for item in dots:
        my_string = dots_grid[item[1]]
        dots_grid[item[1]] = my_string[:item[0]] + '#' + my_string[item[0]+1:]
    # the folds are after the delimiter, tuples of (direction, line to fold)
    folds = input[delimiter+1:]
    for ind, fold in enumerate(folds):
        parse = re.search(r"(\w)=(\d+)", fold)
        folds[ind] = (parse.group(1), int(parse.group(2)))
    # return a list of coord tuples, and a list of instruction tuples
    return dots_grid, folds


def combine(a, b):
    for ind, line in enumerate(a):
        for i, char in enumerate(line):
            if b[ind][i] == '#':
                a[ind] = a[ind][:i] + '#' + a[ind][i+1:]
    return a


def magic(dots_grid, folds, nr=0):
    counter = 0
    wip_grid = dots_grid.copy()
    if nr == 0: nr = len(folds)
    for fold in range(0, nr):
        fold_dir = folds[fold][0]
        fold_line = folds[fold][1]
        if fold_dir == 'y':
            top = wip_grid[:fold_line]
            bottom = wip_grid[fold_line+1:]
            # fix for uneven lengths
            if len(top) > len(bottom):
                for i in range(0, len(top) - len(bottom)):
                    bottom.append('.'*len(top[0]))
            if len(top) < len(bottom):
                additional_lines = []
                for i in range(0, len(bottom) - len(top)):
                    additional_lines.append('.'*len(top[0]))
                top = additional_lines + top
            bottom.reverse()
            wip_grid = combine(top, bottom)

        else:
            left = [line[:fold_line] for line in wip_grid]
            right = [line[fold_line+1:] for line in wip_grid]
            right = [i[::-1] for i in right]
            wip_grid = combine(left, right)
    # count dots
    for i in wip_grid:
        for j in i:
            if j == '#':
                counter += 1

    return counter, wip_grid


if __name__ == "__main__":
    dots_grid, folds = parse_input(INPUT)
    # pprint.pprint(dots_grid)
    print('Part 1 =', magic(dots_grid, folds, 1)[0])  # 781
    print('*'*30)
    print('Part 2 vvvvv')  # PERCGJPB
    pprint.pprint(magic(dots_grid, folds)[1])
