# https://adventofcode.com/2021/day/7
# region ---- imports ----
import os
import sys

with open(os.path.join(sys.path[0], "Inputs/advent_07_input.txt"), "r") as raw_input:
    INPUT = raw_input.read().split(',')
INPUT = [int(i) for i in INPUT]

TEST_INPUT = [16,1,2,0,4,2,7,1,2,14]
# endregion --------------


def get_min_fuel_one(input):
    positions_fuel = []

    for position in range(min(input), max(input)):
        fuel = 0
        for i in input:
            fuel += abs(i-position)
        positions_fuel.append(fuel)

    return min(positions_fuel)


def get_min_fuel_two(input):
    positions_fuel = []

    for position in range(min(input), max(input)):
        fuel = 0
        for i in input:
            difference = abs(i-position)
            fuel += int( ((difference**2)+difference)/2 )
        positions_fuel.append(fuel)

    return min(positions_fuel)


if __name__ == "__main__":
    print('Part 1 =', get_min_fuel_one(INPUT))  # 326132
    print('*'*30)
    print('Part 2 =', get_min_fuel_two(INPUT))  # 88612508
