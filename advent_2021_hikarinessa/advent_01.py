# https://adventofcode.com/2021/day/1
# region ---- imports and inputs ----
import os
import sys

with open(os.path.join(sys.path[0], "Inputs/advent_01_input.txt"), "r") as raw_input:
    INPUT = raw_input.read().splitlines()
    INPUT = [int(i) for i in INPUT]

TEST_INPUT = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]
# TEST_INPUT results: part 1 = 7, part 2 = 5
# endregion -------------------------


# part 1
# Count the number of times a depth measurement increases from the previous measurement.
def slope_increase(my_input):
    """counts the number of times that a number is larger than the previous number in a list"""
    prev = 0
    count = -1
    for i in my_input:
        if i > prev:
            count += 1
        prev = i
    return count


# part 2
# Instead, consider sums of a three-measurement sliding window.
# Cunt the number of times the sum of measurements in this sliding window increases from the previous sum.
def part_two(my_input):
    # prep the input list into three-measurement segments
    new_list = []
    for i in range(0, len(my_input) - 2):
        foo = my_input[i] + my_input[i + 1] + my_input[i + 2]
        new_list.append(foo)
    # calculate the slope increase using the existing function from part 1
    return slope_increase(new_list)


if __name__ == "__main__":
    print('Part 1 =', slope_increase(INPUT))  # 1301
    print('*'*30)
    print('Part 2 =', part_two(INPUT))  # 1346
