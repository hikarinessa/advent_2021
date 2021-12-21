# https://adventofcode.com/2021/day/2
# region ---- imports and inputs ----
import re
import os
import sys

with open(os.path.join(sys.path[0], "Inputs/advent_02_input.txt"), "r") as raw_input:
    INPUT = raw_input.read().splitlines()

TEST_INPUT = ['forward 5', 'down 5', 'forward 8', 'up 3', 'down 8', 'forward 2']
# TEST_INPUT results: part 1 = 150, part 2 = 900
# endregion -------------------------


# prep input
def prep_input(my_input):
    output = []
    for i in my_input:
        parse = re.search(r"(.*) (\d)", i)
        instruction = parse.group(1)
        amount = int(parse.group(2))
        output.append([instruction, amount])
    return output

# What do you get if you multiply your final horizontal position by your final depth?


# part 1
# - forward X increases the horizontal position by X units.
# - down X increases the depth by X units.
# - up X decreases the depth by X units.
def final_position_one(my_input):
    new_input = prep_input(my_input)
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
# - down X increases your aim by X units.
# - up X decreases your aim by X units.
# - forward X does two things:
#   - It increases your horizontal position by X units.
#   - It increases your depth by your aim multiplied by X.
def final_position_two(my_input):
    new_input = prep_input(my_input)
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


if __name__ == "__main__":
    print('Part 1 =', final_position_one(INPUT))  # 1451208
    print('*'*30)
    print('Part 2 =', final_position_two(INPUT))  # 1620141160
