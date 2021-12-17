# https://adventofcode.com/2021/day/10
# region ---- imports ----
import os
import sys
import math

with open(os.path.join(sys.path[0], "Inputs/advent_10_input.txt"), "r") as raw_input:
    INPUT = raw_input.read().splitlines()

TEST_INPUT = ['[({(<(())[]>[[{[]{<()<>>',
              '[(()[<>])]({[<{<<[]>>(',
              '{([(<{}[<>[]}>{[]{[(<()>',
              '(((({<>}<{<{<>}{[]{[]{}',
              '[[<[([]))<([[{}[[()]]]',
              '[{[{({}]{}}([{[{{{}}([]',
              '{<[[]]>}<{[{[{[]{()[[[]',
              '[<(<(<(<{}))><([]([]()',
              '<{([([[(<>()){}]>(<<{{',
              '<{([{{}}[<[[[<>{}]]]>[]]']
# endregion --------------

PARENTH = 3  # )
BRACKET = 57  # ]
CURLYBR = 1197  # }
CHEVRON = 25137  # >


def part_one(input):
    score = 0
    valid_lines = []

    for line in input:
        opening_list = []
        valid = True
        for char in line:
            if char == '(' or char == '[' or char == '{' or char == '<':
                opening_list.append(char)
            else:
                prev = opening_list.pop()
                if char == ')':
                    if prev == '(':
                        pass
                    else:
                        score += PARENTH
                        valid = False
                elif char == ']':
                    if prev == '[':
                        pass
                    else:
                        score += BRACKET
                        valid = False
                elif char == '}':
                    if prev == '{':
                        pass
                    else:
                        score += CURLYBR
                        valid = False
                elif char == '>':
                    if prev == '<':
                        pass
                    else:
                        score += CHEVRON
                        valid = False
        if valid:
            valid_lines.append(line)

    return score, valid_lines


def part_two(input):
    score_list = []

    for line in input:
        score = 0
        opening_list = []
        for char in line:
            if char == '(' or char == '[' or char == '{' or char == '<':
                opening_list.append(char)
            else:
                opening_list.pop()

        while len(opening_list) > 0:
            item = opening_list.pop()
            if item == '(':
                score = score*5 + 1
            if item == '[':
                score = score*5 + 2
            if item == '{':
                score = score*5 + 3
            if item == '<':
                score = score*5 + 4

        score_list.append(score)

    score_list.sort()
    final_score = score_list[math.floor(len(score_list)/2)]

    return final_score


if __name__ == "__main__":
    score, valid_lines = part_one(INPUT)
    print('Part 1 =', score)  # 392043
    print('*'*30)
    print('Part 2 =', part_two(valid_lines))  # 1605968119
