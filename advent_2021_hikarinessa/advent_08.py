# https://adventofcode.com/2021/day/8
# region ---- imports ----
import os
import sys

with open(os.path.join(sys.path[0], "Inputs/advent_08_input.txt"), "r") as raw_input:
    INPUT = raw_input.read().splitlines()

TEST_INPUT = ['acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab | cdfeb fcadb cdfeb cdbaf']
TEST_INPUT2 = ['be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe',
               'edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc',
               'fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg',
               'fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb',
               'aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea',
               'fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb',
               'dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe',
               'bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef',
               'egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb',
               'gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce']
# endregion --------------

'''!!!!!!!!!! THERE'S A BUNCH OF USELESS SHIT IN THIS FILE !!!!!!!!!!'''


class Line:
    def __init__(self, signal_patterns, output):
        self.signal_patterns = signal_patterns
        self.output = output


def parse_input(input):
    """returns a list of objects of type Line"""
    line_collection = []
    for line in input:
        line_separated = line.split(' | ')
        signal_patterns = line_separated[0].split(' ')
        output = line_separated[1].split(' ')
        line_collection.append(Line(signal_patterns, output))
    return line_collection


# part 1
def part_one(input):
    counter = 0
    for line in parse_input(input):
        for num in line.output:
            if len(num) == 2 or len(num) == 3 or len(num) == 4 or len(num) == 7:
                counter += 1
    return counter


# part 2
class Segment:
    def __init__(self, name, numbers):
        self.possibilities = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
        self.name = name
        self.numbers = numbers
        self.letter = ''

    def has_collapsed(self):
        if len(self.possibilities) == 1:
            self.letter = self.possibilities[0]
            return True
        else: return False

    def collapse_from(self, string):
        for char in string:
            self.possibilities = [i for i in self.possibilities if i != char]
        self.has_collapsed()

    def collapse_to(self, string):
        self.possibilities = [i for i in string if i in self.possibilities]
        self.has_collapsed()


def part_two(input):
    result = 0
    for line in parse_input(input):
        seg_top = Segment('seg_top', [0, 2, 3, 5, 6, 7, 8, 9])  # .   seg_top
        seg_tle = Segment('seg_tle', [0, 4, 5, 6, 8, 9])  # .  seg   seg
        seg_tri = Segment('seg_tri', [0, 1, 2, 3, 4, 7, 8, 9])  # .  tle   tri
        seg_mid = Segment('seg_mid', [2, 3, 4, 5, 6, 8, 9])  # .   seg_mid
        seg_ble = Segment('seg_ble', [0, 2, 6, 8])  # .  seg   seg
        seg_bri = Segment('seg_bri', [0, 1, 3, 4, 5, 6, 7, 8, 9])  # .  ble   bri
        seg_bot = Segment('seg_bot', [0, 2, 3, 5, 6, 8, 9])  # .   seg_bot

        one = [seg_tri, seg_bri]  #
        seven = [seg_top, seg_tri, seg_bri]  #
        four = [seg_tle, seg_mid, seg_tri, seg_bri]  #
        two = [seg_top, seg_tri, seg_mid, seg_ble, seg_bot]  # ble
        three = [seg_top, seg_tri, seg_mid, seg_bri, seg_bot]  # bri
        five = [seg_top, seg_tle, seg_mid, seg_bri, seg_bot]  # tle
        six = [seg_top, seg_tle, seg_mid, seg_ble, seg_bri, seg_bot]  # -tri
        nine = [seg_top, seg_tle, seg_tri, seg_mid, seg_bri, seg_bot]  # -ble
        zero = [seg_top, seg_tle, seg_tri, seg_ble, seg_bri, seg_bot]  # -mid
        eight = [seg_top, seg_tle, seg_tri, seg_mid, seg_ble, seg_bri, seg_bot]  #

        # first collapse
        # num_one = [i for i in line.signal_patterns if len(i) == 2][0]

        for seg in one:
            seg.collapse_to( [i for i in line.signal_patterns if len(i) == 2][0] )
        for seg in eight:
            if seg is not seg_tri and seg is not seg_bri:
                seg.collapse_from(''.join(seg_tri.possibilities))

        for seg in seven:
            seg.collapse_to( [i for i in line.signal_patterns if len(i) == 3][0] )
        for seg in eight:
            if seg is not seg_top:
                seg.collapse_from(''.join(seg_top.possibilities))

        for seg in four:
            seg.collapse_to( [i for i in line.signal_patterns if len(i) == 4][0] )
        for seg in eight:
            if seg is not seg_tle and seg is not seg_mid:
                seg.collapse_from(''.join(seg_tle.possibilities))

        for string in line.signal_patterns:  # three
            if len(string) == 5:
                is_three = True
                for i in seg_tri.possibilities:
                    if i not in string:
                        is_three = False
                if is_three:
                    seg_bot.collapse_to(string)
        for seg in eight:
            if seg is not seg_bot:
                seg.collapse_from(''.join(seg_bot.possibilities))

        for string in line.signal_patterns:  # six
            if len(string) == 6:
                is_six = True
                j = ''.join(seg_ble.possibilities + seg_mid.possibilities)
                for i in j:
                    if i not in string:
                        is_six = False
                if is_six:
                    seg_bri.collapse_to(string)
        for seg in eight:
            if seg is not seg_bri:
                seg.collapse_from(''.join(seg_bri.possibilities))

        for string in line.signal_patterns:  # zero
            if len(string) == 6:
                j = ''.join(seg_mid.possibilities)
                counter = 0
                for i in j:
                    if i in string:
                        counter += 1
                if counter == 1:
                    seg_tle.collapse_to(string)
        for seg in eight:
            if seg is not seg_tle:
                seg.collapse_from(''.join(seg_tle.possibilities))

        numstring = ''
        for i in line.output:
            numstring += str(find_number(i, seg_ble, seg_tri, seg_tle, seg_mid))

        # print(numstring)
        # print('*'*5)
        # for seg in eight:
        #     print(seg.name, seg.possibilities)
        result += int(numstring)

    return result


def find_number(string, seg_ble, seg_tri, seg_tle, seg_mid):
    if len(string) == 2: return 1
    if len(string) == 3: return 7
    if len(string) == 4: return 4
    if len(string) == 7: return 8
    if len(string) == 5:
        if seg_ble.letter in string: return 2
        if seg_tri.letter in string: return 3
        if seg_tle.letter in string: return 5
    if len(string) == 6:
        if seg_mid.letter not in string: return 0
        if seg_ble.letter not in string: return 9
        if seg_tri.letter not in string: return 6


if __name__ == "__main__":
    print('Part 1 =', part_one(INPUT))  # 479
    print('*'*30)
    print('Part 2 =', part_two(INPUT))  # 1041746
