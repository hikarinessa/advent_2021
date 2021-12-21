# https://adventofcode.com/2021/day/12
# region ---- imports ----
import os
import sys
import pprint

with open(os.path.join(sys.path[0], "Inputs/advent_12_input.txt"), "r") as raw_input:
    INPUT = raw_input.read().splitlines()

TEST_INPUT = ['start-A',
              'start-b',
              'A-c',
              'A-b',
              'b-d',
              'A-end',
              'b-end']
# endregion --------------


def parse_input(input):
    instructions = {}
    for line in input:
        var = line.split('-')
        if var[0] in instructions.keys():
            instructions[var[0]].append(var[1])
        else:
            instructions[var[0]] = [var[1]]
        if var[1] in instructions.keys():
            instructions[var[1]].append(var[0])
        else:
            instructions[var[1]] = [var[0]]
    # pprint.pprint(instructions)
    return instructions


def part_one(instructions):
    chains = [['start']]
    finished_chains= []

    while len(chains) > 0:
        chain = chains.pop()
        last = chain[-1]
        if last == 'end':
            finished_chains.append(chain)
        else:
            for instr in instructions[last]:
                if instr not in chain or instr.isupper():
                    temp = chain.copy()
                    temp.append(instr)
                    chains.append(temp)

    # pprint.pprint(finished_chains)

    return len(finished_chains)


def part_two(instructions):
    chains = [['start']]
    finished_chains= []

    while len(chains) > 0:
        chain = chains.pop()
        exception = True

        # check for exception
        temp = chain.copy()
        while len(temp) > 0:
            i = temp.pop()
            if i.islower():
                if i != 'start' and i != 'end':
                    if i in temp:
                        exception = False

        last = chain[-1]
        if last == 'end':
            finished_chains.append(chain)
        else:
            for instr in instructions[last]:
                if instr not in chain or instr.isupper():
                    temp = chain.copy()
                    temp.append(instr)
                    chains.append(temp)
                elif instr != 'start' and instr != 'end':
                    if exception:
                        temp = chain.copy()
                        temp.append(instr)
                        chains.append(temp)

    return len(finished_chains)


if __name__ == "__main__":
    print('Part 1 =', part_one(parse_input(INPUT)))  # 3802
    print('*'*30)
    print('Part 2 =', part_two(parse_input(INPUT)))  # 99448
