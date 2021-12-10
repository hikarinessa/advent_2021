# https://adventofcode.com/2021/day/5
# region ---- imports ----
import re
import os
import sys
import pprint

with open(os.path.join(sys.path[0], "Inputs/advent_05_input.txt"), "r") as raw_input:
    INPUT = raw_input.read().splitlines()

TEST_INPUT = ['0,9 -> 5,9',
              '8,0 -> 0,8',
              '9,4 -> 3,4',
              '2,2 -> 2,1',
              '7,0 -> 7,4',
              '6,4 -> 2,0',
              '0,9 -> 2,9',
              '3,4 -> 1,4',
              '0,0 -> 8,8',
              '5,5 -> 8,2']
# endregion --------------
debug = False


class HydrothermalVent:
    def __init__(self, input):
        parse = re.search(r"(\d+),(\d+) -> (\d+),(\d+)", input)
        self.x1 = int(parse.group(1))
        self.y1 = int(parse.group(2))
        self.x2 = int(parse.group(3))
        self.y2 = int(parse.group(4))
        self.orthogonal = self.is_orthogonal()
        self.coords = self.coordinates2()

    def print_vent(self):
        print(self.x1, ",", self.y1, " -> ", self.x2, ",", self.y2)
        print(self.coords)

    def is_orthogonal(self):
        if self.x1 == self.x2:
            return True
        elif self.y1 == self.y2:
            return True
        else:
            return False

    def coordinates(self):
        coord_list = []
        step = 1
        if self.x1 == self.x2:
            if self.y1 > self.y2: step = -1
            for i in range(self.y1, self.y2, step):
                coord_list.append((self.x1, i))
            coord_list.append((self.x2, self.y2))
        elif self.y1 == self.y2:
            if self.x1 > self.x2: step = -1
            for i in range(self.x1, self.x2, step):
                coord_list.append((i, self.y1))
            coord_list.append((self.x2, self.y2))
        else:
            step_y = 1
            if self.x1 > self.x2: step = -1
            if self.y1 > self.y2: step_y = -1
            j = self.y1
            for i in range(self.x1, self.x2, step):
                coord_list.append((i, j))
                j += step_y
            coord_list.append((self.x2, self.y2))
        return coord_list


# part 1
def overlap_orthogonal(input):
    grid = {}
    counter = 0

    for i in input:
        vent = HydrothermalVent(i)
        if vent.orthogonal:  # only line different from part 2
            for coord in vent.coords:
                if coord not in grid:
                    grid[coord] = 1
                else:
                    grid[coord] += 1

    for value in grid.values():
        if value >= 2:
            counter += 1

    return counter


# part 2
def overlap_all(input):
    grid = {}
    counter = 0

    for i in input:
        vent = HydrothermalVent(i)
        for coord in vent.coords:
            if coord not in grid:
                grid[coord] = 1
            else:
                grid[coord] += 1

    for value in grid.values():
        if value >= 2:
            counter += 1

    return counter


if __name__ == "__main__":
    print('Part 1 =', overlap_orthogonal(INPUT))  # 4826
    print('*'*30)
    print('Part 2 =', overlap_all(INPUT))  # 16793
