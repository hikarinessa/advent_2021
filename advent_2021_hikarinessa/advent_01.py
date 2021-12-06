# https://adventofcode.com/2021/day/1
# region ---- imports ----
import os
import sys

with open(os.path.join(sys.path[0], "Inputs/advent_01_input.txt"), "r") as raw_input:
    INPUT = raw_input.read().splitlines()
INPUT = [int(i) for i in INPUT]

TEST_INPUT = [199,
              200,
              208,
              210,
              200,
              207,
              240,
              269,
              260,
              263]
# endregion --------------


# part 1
def slope_increase(INPUT):
    prev = 0
    count = -1
    for i in INPUT:
        if i > prev:
            count += 1
        prev = i
    return count


print('Part 1 =', slope_increase(INPUT))  # 1301
print('*'*30)

# part 2
newlist = []

for i in range(0, len(INPUT)-2):
    foo = INPUT[i] + INPUT[i+1] + INPUT[i+2]
    newlist.append(foo)

print('Part 2 =', slope_increase(newlist))  # 1346
