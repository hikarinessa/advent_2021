# https://adventofcode.com/2021/day/3
# region ---- imports ----
import re
import os
import sys

with open(os.path.join(sys.path[0], "Inputs/advent_03_input.txt"), "r") as raw_input:
    INPUT = raw_input.read().splitlines()

TEST_INPUT = ['00100',
              '11110',
              '10110',
              '10111',
              '10101',
              '01111',
              '00111',
              '11100',
              '10000',
              '11001',
              '00010',
              '01010']
# endregion --------------

# to convert binary to decimal: print(int('01001',2))


# part 1
def find_rates_one(input):
    gamma_rate = ''
    epsilon_rate = ''
    halflength = len(input)/2

    for i in range(0, len(input[0])):
        bit = 0
        for j in input:
            bit += int(j[i])
        if bit >= halflength:
            gamma_rate += '1'
            epsilon_rate += '0'
        else:
            gamma_rate += '0'
            epsilon_rate += '1'

    power_consumption = int(gamma_rate, 2) * int(epsilon_rate, 2)
    return power_consumption


# part 2
def find_rates_two(input):
    oxygen_generator_rating = input.duplicate()
    co2_scrubber_rating = input.duplicate()
    halflength = len(input)/2

    for i in range(0, len(input[0])):
        bit = 0

        for j in input:
            bit += int(j[i])

        for k in input:
            if bit >= halflength:
                oxygen_generator_rating[k].pop()
            else:
                co2_scrubber_rating

    life_support_rating = ''
    return life_support_rating


print('Part 1 =', find_rates_one(INPUT))  # 4174964
print('*'*30)
print('Part 2 =', '')  #
