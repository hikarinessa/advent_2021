# https://adventofcode.com/2021/day/11
# region ---- imports ----
import pprint
import copy

TEST_INPUT = [[5, 4, 8, 3, 1, 4, 3, 2, 2, 3],
              [2, 7, 4, 5, 8, 5, 4, 7, 1, 1],
              [5, 2, 6, 4, 5, 5, 6, 1, 7, 3],
              [6, 1, 4, 1, 3, 3, 6, 1, 4, 6],
              [6, 3, 5, 7, 3, 8, 5, 4, 7, 8],
              [4, 1, 6, 7, 5, 2, 4, 6, 4, 5],
              [2, 1, 7, 6, 8, 4, 1, 7, 2, 1],
              [6, 8, 8, 2, 8, 8, 1, 1, 3, 4],
              [4, 8, 4, 6, 8, 4, 8, 5, 5, 4],
              [5, 2, 8, 3, 7, 5, 1, 5, 2, 6]]
TEST_INPUT2 = [[1, 1, 1, 1, 1],
               [1, 9, 9, 9, 1],
               [1, 9, 1, 9, 1],
               [1, 9, 9, 9, 1],
               [1, 1, 1, 1, 1]]
INPUT = [[2, 6, 8, 2, 5, 5, 1, 6, 5, 1],
         [3, 2, 2, 3, 1, 3, 4, 2, 6, 3],
         [5, 8, 4, 8, 4, 7, 1, 4, 1, 2],
         [7, 4, 3, 8, 3, 3, 4, 8, 6, 2],
         [8, 7, 3, 1, 3, 2, 1, 5, 7, 3],
         [6, 4, 1, 5, 2, 3, 3, 5, 7, 4],
         [5, 5, 6, 4, 7, 2, 6, 8, 4, 3],
         [6, 6, 8, 3, 4, 5, 6, 4, 4, 5],
         [8, 5, 8, 2, 3, 4, 6, 1, 1, 2],
         [4, 6, 1, 7, 5, 8, 8, 2, 3, 6]]

# (-1, -1)  (-1,  0)  (-1, +1)
# ( 0, -1)  ( 0,  0)  ( 0, +1)
# (+1, -1)  (+1,  0)  (+1, +1)

# endregion --------------
debug = False


# part 1
def part_one(input, iterations):
    flashes = 0
    curr_list = copy.deepcopy(input)

    if debug:
        print('Before any steps:')
        pprint.pprint(curr_list)

    for i in range(0, iterations):
        # increase all by 1
        for row, line in enumerate(curr_list):
            for col, element in enumerate(line):
                curr_list[row][col] = element + 1

        # propagation
        while True:
            num_nines = 0
            temp_list = curr_list.copy()
            for row, line in enumerate(curr_list):
                for col, element in enumerate(line):
                    if 100 > element > 9:
                        num_nines += 1
                        temp_list[row][col] = 100
                        if col != 0 and row != 0:
                            temp_list[row-1][col-1] = temp_list[row-1][col-1]+1   # top left
                        if col != 0 and row < len(curr_list)-1:
                            temp_list[row+1][col-1] = temp_list[row+1][col-1]+1   # bottom left
                        if col != 0:
                            temp_list[row][col-1] = temp_list[row][col-1]+1       # left
                        if row != 0:
                            temp_list[row-1][col] = temp_list[row-1][col]+1       # top
                        if col < len(line)-1 and row != 0:
                            temp_list[row-1][col+1] = temp_list[row-1][col+1]+1   # top right
                        if col < len(line)-1 and row < len(curr_list)-1:
                            temp_list[row+1][col+1] = temp_list[row+1][col+1]+1   # bottom right
                        if col < len(line)-1:
                            temp_list[row][col+1] = temp_list[row][col+1]+1       # right
                        if row < len(curr_list)-1:
                            temp_list[row+1][col] = temp_list[row+1][col]+1       # bottom

            curr_list = temp_list.copy()
            if num_nines == 0:
                break

        # count flashes
        for row, line in enumerate(curr_list):
            for col, element in enumerate(line):
                if element > 9:
                    flashes += 1
                    curr_list[row][col] = 0

        # if debug:
        #     print('After step {}:'.format(i))
        #     pprint.pprint(curr_list)

    return flashes


# part 2
def part_two(input):
    curr_list = copy.deepcopy(input)
    i = 1

    while True:
        # increase all by 1
        for row, line in enumerate(curr_list):
            for col, element in enumerate(line):
                curr_list[row][col] = element + 1

        # propagation
        while True:
            num_nines = 0
            temp_list = curr_list.copy()
            for row, line in enumerate(curr_list):
                for col, element in enumerate(line):
                    if 100 > element > 9:
                        num_nines += 1
                        temp_list[row][col] = 100
                        if col != 0 and row != 0:
                            temp_list[row-1][col-1] = temp_list[row-1][col-1]+1   # top left
                        if col != 0 and row < len(curr_list)-1:
                            temp_list[row+1][col-1] = temp_list[row+1][col-1]+1   # bottom left
                        if col != 0:
                            temp_list[row][col-1] = temp_list[row][col-1]+1       # left
                        if row != 0:
                            temp_list[row-1][col] = temp_list[row-1][col]+1       # top
                        if col < len(line)-1 and row != 0:
                            temp_list[row-1][col+1] = temp_list[row-1][col+1]+1   # top right
                        if col < len(line)-1 and row < len(curr_list)-1:
                            temp_list[row+1][col+1] = temp_list[row+1][col+1]+1   # bottom right
                        if col < len(line)-1:
                            temp_list[row][col+1] = temp_list[row][col+1]+1       # right
                        if row < len(curr_list)-1:
                            temp_list[row+1][col] = temp_list[row+1][col]+1       # bottom

            curr_list = temp_list.copy()
            if num_nines == 0:
                break

        # check flash all
        flashes = 0
        for row, line in enumerate(curr_list):
            for col, element in enumerate(line):
                if element > 9:
                    flashes += 1
                    curr_list[row][col] = 0

        if flashes == len(curr_list)*len(curr_list[0]):
            return i
        i += 1


if __name__ == "__main__":
    print('Part 1 =', part_one(INPUT, 100))  # 1594
    print('*'*30)
    print('Part 2 =', part_two(INPUT))  # 437
