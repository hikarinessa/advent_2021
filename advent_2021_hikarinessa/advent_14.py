# https://adventofcode.com/2021/day/14
# region ---- imports ----
import os
import sys

with open(os.path.join(sys.path[0], "Inputs/advent_14_input.txt"), "r") as raw_input:
    INPUT = raw_input.read().splitlines()

TEST_INPUT = ['NNCB',
              '',
              'CH -> B', 'HH -> N', 'CB -> H', 'NH -> C', 'HB -> C', 'HC -> B', 'HN -> C', 'NN -> C',
              'BH -> H', 'NC -> B', 'NB -> B', 'BN -> B', 'BB -> N', 'BC -> B', 'CC -> N', 'CN -> C']
# endregion --------------
debug = False


def parse_input(my_input):
    polymer_template = my_input[0]
    pair_insertions = {}
    for line in my_input[2:]:
        pair_insertions[line[:2]] = line[-1]
    return polymer_template, pair_insertions


def calculate_chain(my_input, steps):
    polymer_template, pair_insertions = parse_input(my_input)
    for i in range(0, steps):
        temp_list = []
        for j in range(0, len(polymer_template)-1):
            temp_list.append(polymer_template[j:j+2])
        polymer_template = polymer_template[0]
        for k in temp_list:
            polymer_template += pair_insertions[k] + k[1]
    return polymer_template


def most_minus_least(my_input, steps):
    polymer = calculate_chain(my_input, steps)
    unique_chars = ''.join(set(polymer))
    occurrences = []
    for i in unique_chars:
        occurrences.append(polymer.count(i))
    return max(occurrences) - min(occurrences)


# part 2
def part_two(my_input, steps):
    polymer_template, pair_insertions = parse_input(my_input)
    # prep final values dict
    char_occurrences = {}
    values = []
    for val in pair_insertions.values():
        values.append(val)
    unique_chars = ''.join(set(values))
    for char in unique_chars:
        char_occurrences[char] = 0
    # prep pair occurrences dict
    pair_occurrences = {key: 0 for key in pair_insertions.keys()}
    for i in range(0, len(polymer_template)-1):
        pair = polymer_template[i] + polymer_template[i+1]
        pair_occurrences[pair] += 1
    # step and find all pair value combos
    for i in range(0, steps):
        # print('polymer before', polymer_template)
        # print('pairs before', pair_occurrences)
        temp_dict = {key: 0 for (key,val) in pair_occurrences.items()}
        for key, val in pair_occurrences.items():
            if val > 0:
                if debug: print(key)
                new_str = key[0] + pair_insertions[key] + key[1]
                if debug: print (new_str)
                temp_dict[new_str[:2]] += val
                temp_dict[new_str[1:]] += val
        pair_occurrences = temp_dict
        # delete below
        if debug:
            temp_list = []
            for j in range(0, len(polymer_template)-1):
                temp_list.append(polymer_template[j:j+2])
            polymer_template = polymer_template[0]
            for k in temp_list:
                polymer_template += pair_insertions[k] + k[1]
            temp_pairs = []
            for l in range(0, len(polymer_template)-1):
                temp_pairs.append(polymer_template[l] + polymer_template[l+1])
        if debug: print('polymer after', polymer_template)
        if debug: print('polymer after', temp_pairs)
        if debug: print('pairs after', pair_occurrences)

    # find char occurrences from pair occurrences
    for char in char_occurrences.keys():
        for key, val in pair_occurrences.items():
            for letter in key:
                if char == letter:
                    char_occurrences[char] += val
    char_occurrences[polymer_template[0]] += 1
    char_occurrences[polymer_template[-1]] += 1
    char_occurrences = {key:int(val/2) for (key,val) in char_occurrences.items()}

    if debug: print(polymer_template)
    if debug: print(pair_occurrences)
    if debug: print(char_occurrences)
    # calculate final result
    occurrences = [val for val in char_occurrences.values()]
    return max(occurrences) - min(occurrences)


if __name__ == "__main__":
    print('Part 1 =', most_minus_least(INPUT, 10))  # 3831
    print('*'*30)
    print('Part 2 =', part_two(INPUT, 40))  #
