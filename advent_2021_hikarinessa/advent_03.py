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
    oxygen_generator_rating = input.copy()
    co2_scrubber_rating = input.copy()

    for i in range(0, len(oxygen_generator_rating[0])):
        bit = 0

        for j in oxygen_generator_rating:
                bit += int(j[i])

        if bit >= len(oxygen_generator_rating)/2: # 1 is more prevalent
            for ind, k in enumerate(oxygen_generator_rating):
                if k is not None and int(k[i]) == 0:
                    oxygen_generator_rating[ind] = None
        else:  # 0 is more prevalent
            for ind, k in enumerate(oxygen_generator_rating):
                if k is not None and int(k[i]) == 1:
                    oxygen_generator_rating[ind] = None

        oxygen_generator_cleanup = [k for k in oxygen_generator_rating if k]
        oxygen_generator_rating = oxygen_generator_cleanup
        if len(oxygen_generator_cleanup) == 1:
            break
    oxygen_generator_rating = int(oxygen_generator_rating[0], 2)
    # print("oxygen_generator_rating", oxygen_generator_rating)

    for i in range(0, len(co2_scrubber_rating[0])):
        bit = 0

        for j in co2_scrubber_rating:
                bit += int(j[i])

        if bit >= len(co2_scrubber_rating)/2: # 1 is more prevalent
            for ind, k in enumerate(co2_scrubber_rating):
                if k is not None and int(k[i]) == 1:
                    co2_scrubber_rating[ind] = None
        else:  # 0 is more prevalent
            for ind, k in enumerate(co2_scrubber_rating):
                if k is not None and int(k[i]) == 0:
                    co2_scrubber_rating[ind] = None

        co2_scrubber_cleanup = [k for k in co2_scrubber_rating if k]
        co2_scrubber_rating = co2_scrubber_cleanup
        if len(co2_scrubber_rating) == 1:
            break
    co2_scrubber_rating = int(co2_scrubber_rating[0], 2)
    # print("co2_scrubber_rating", co2_scrubber_rating)


    life_support_rating = oxygen_generator_rating * co2_scrubber_rating
    return life_support_rating


print('Part 1 =', find_rates_one(INPUT))  # 4174964
print('*'*30)
print('Part 2 =', find_rates_two(INPUT))  # 4474944
