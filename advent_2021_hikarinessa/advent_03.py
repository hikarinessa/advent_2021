# https://adventofcode.com/2021/day/3
# region ---- imports and inputs ----
import os
import sys

with open(os.path.join(sys.path[0], "Inputs/advent_03_input.txt"), "r") as raw_input:
    INPUT = raw_input.read().splitlines()

TEST_INPUT = ['00100', '11110', '10110', '10111', '10101', '01111',
              '00111', '11100', '10000', '11001', '00010', '01010']
# TEST_INPUT results: part 1 = 198, part 2 = 230
# endregion -------------------------

# to convert binary to decimal: print(int('01001',2))


# region ---- part 1 instructions ----
# The power consumption can then be found by multiplying the gamma rate by the epsilon rate.
# The gamma rate can be determined by finding the most common bit in the corresponding position
# of all numbers in the diagnostic report.
# The epsilon rate can be determined by finding the least common bit (...)
# endregion --------------------------
def find_rates_one(input):
    gamma_rate = ''
    epsilon_rate = ''
    half_length = len(input)/2

    for i in range(0, len(input[0])):
        bit = 0
        for j in input:
            bit += int(j[i])
        if bit >= half_length:
            gamma_rate += '1'
            epsilon_rate += '0'
        else:
            gamma_rate += '0'
            epsilon_rate += '1'

    power_consumption = int(gamma_rate, 2) * int(epsilon_rate, 2)
    return power_consumption


# region ---- part 2 instructions ----
# Next verify the life support rating, which can be determined
# by multiplying the oxygen generator rating by the CO2 scrubber rating.
# - Keep only numbers selected by the bit criteria for the type of rating value for which you are searching.
# - Discard numbers which do not match the bit criteria.
#   If you only have one number left, stop; this is the rating value for which you are searching.
# - Otherwise, repeat the process, considering the next bit to the right.
# The bit criteria depends on which type of rating value you want to find:
# - To find oxygen generator rating, determine the most common value (0 or 1) in the current bit position,
#   and keep only numbers with that bit in that position.
#   If 0 and 1 are equally common, keep values with a 1 in the position being considered.
# - To find CO2 scrubber rating, determine the least common value (0 or 1) in the current bit position,
#   and keep only numbers with that bit in that position. If 0 and 1 are equally common,
#   keep values with a 0 in the position being considered
# endregion --------------------------
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

        oxygen_generator_rating = [k for k in oxygen_generator_rating if k]
        if len(oxygen_generator_rating) == 1:
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

        co2_scrubber_rating = [k for k in co2_scrubber_rating if k]
        if len(co2_scrubber_rating) == 1:
            break
    co2_scrubber_rating = int(co2_scrubber_rating[0], 2)
    # print("co2_scrubber_rating", co2_scrubber_rating)

    life_support_rating = oxygen_generator_rating * co2_scrubber_rating
    return life_support_rating


print('Part 1 =', find_rates_one(INPUT))  # 4174964
print('*'*30)
print('Part 2 =', find_rates_two(INPUT))  # 4474944
