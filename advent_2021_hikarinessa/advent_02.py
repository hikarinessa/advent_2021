# https://adventofcode.com/2021/day/2
# region ---- imports ----
import re
import os
import sys

with open(os.path.join(sys.path[0], "Inputs/advent_02_input.txt"), "r") as raw_input:
    INPUT = raw_input.read().splitlines()

TEST_INPUT = ['forward 5',
              'down 5',
              'forward 8',
              'up 3',
              'down 8',
              'forward 2']
# endregion --------------


# prep input
def prep_input(input):
    output = []
    for i in input:
        parse = re.search(r"(.*) (\d)", i)
        instruction = parse.group(1)
        amount = int(parse.group(2))
        output.append([instruction, amount])
    return output


# part 1
def final_position_one(input):
    new_input = prep_input(input)
    horizontal = 0
    depth = 0

    for i in new_input:
        if i[0] == "forward":
            horizontal += i[1]
        elif i[0] == "down":
            depth += i[1]
        elif i[0] == "up":
            depth -= i[1]

    return horizontal*depth


# part 2
def final_position_two(input):
    new_input = prep_input(input)
    horizontal = 0
    aim = 0
    depth = 0

    for i in new_input:
        if i[0] == "forward":
            horizontal += i[1]
            depth += i[1]*aim
        elif i[0] == "down":
            aim += i[1]
        elif i[0] == "up":
            aim -= i[1]

    return horizontal*depth


print('Part 1 =', final_position_one(INPUT))  # 1451208
print('*'*30)
print('Part 2 =', final_position_two(INPUT))  # 1620141160
