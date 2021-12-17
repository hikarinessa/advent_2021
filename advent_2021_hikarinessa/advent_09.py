# https://adventofcode.com/2021/day/9
# region ---- imports ----
import os
import sys

with open(os.path.join(sys.path[0], "Inputs/advent_09_input.txt"), "r") as raw_input:
    INPUT = raw_input.read().splitlines()
    # INPUT = [int(i) for i in INPUT]

TEST_INPUT = ['2199943210',
              '3987894921',
              '9856789892',
              '8767896789',
              '9899965678']
# endregion --------------


def part_one(input):
    sum_pt1 = 0
    basin_start_points = {}  # for part 2

    for row, line in enumerate(input):
        for col, element in enumerate(line):
            neighbours = []
            neighbour_coords = []  # for part 2
            if col != 0:
                neighbours.append(input[row][col-1])
                if input[row][col-1] != '9':
                    neighbour_coords.append((row, col-1))  # for part 2
            if row != 0:
                neighbours.append(input[row-1][col])
                if input[row-1][col] != '9':
                    neighbour_coords.append((row-1, col))  # for part 2
            if col < len(line)-1:
                neighbours.append(input[row][col+1])
                if input[row][col+1] != '9':
                    neighbour_coords.append((row, col+1))  # for part 2
            if row < len(input)-1:
                neighbours.append(input[row+1][col])
                if input[row+1][col] != '9':
                    neighbour_coords.append((row+1, col))  # for part 2

            low_count = 0
            for i in neighbours:
                if int(element) < int(i):
                    low_count += 1
            if low_count == len(neighbours):
                sum_pt1 += int(element) + 1
                basin_start_points[(row, col)] = neighbour_coords  # for part 2

    return sum_pt1, basin_start_points


def part_two(input, basin_start_points):
    basin_sizes = []

    for key, val in basin_start_points.items():
        while True:  # while the basin is not surrounded
            neighbours = []
            for coord in val:
                row = coord[0]
                col = coord[1]
                if col != 0:
                    if input[row][col-1] != '9':
                        if (row, col-1) not in val:
                            neighbours.append((row, col-1))
                if row != 0:
                    if input[row-1][col] != '9':
                        if (row-1, col) not in val:
                            neighbours.append((row-1, col))
                if col < len(input[0])-1:
                    if input[row][col+1] != '9':
                        if (row, col+1) not in val:
                            neighbours.append((row, col+1))
                if row < len(input)-1:
                    if input[row+1][col] != '9':
                        if (row+1, col) not in val:
                            neighbours.append((row+1, col))
            if len(neighbours) != 0:
                val = val + neighbours
            else:
                val = list(dict.fromkeys(val))
                basin_start_points[key] = val
                break

        basin_sizes.append(len(basin_start_points[key]))

    final_product = 1
    for i in range(0,3):
        j = max(basin_sizes)
        final_product *= j
        basin_sizes.remove(j)

    return final_product


if __name__ == "__main__":
    sum_pt1, basin_start_points = part_one(INPUT)
    print('Part 1 =', sum_pt1)  # 564
    print('*'*30)
    print('Part 2 =', part_two(INPUT, basin_start_points))  # 1038240
