# https://adventofcode.com/2021/day/6
# region ---- imports ----
TEST_INPUT = '3,4,3,1,2'
INPUT = '3,4,1,1,5,1,3,1,1,3,5,1,1,5,3,2,4,2,2,2,1,1,1,1,5,1,1,1,1,1,3,1,1,5,4,1,1,1,4,1,1,1,1,2,3,2,5,1,5,1,2,1,1,' \
        '1,4,1,1,1,1,3,1,1,3,1,1,1,1,1,1,2,3,4,2,1,3,1,1,2,1,1,2,1,5,2,1,1,1,1,1,1,4,1,1,1,1,5,1,4,1,1,1,3,3,1,3,1,' \
        '3,1,4,1,1,1,1,1,4,5,1,1,3,2,2,5,5,4,3,1,2,1,1,1,4,1,3,4,1,1,1,1,2,1,1,3,2,1,1,1,1,1,4,1,1,1,4,4,5,2,1,1,1,' \
        '1,1,2,4,2,1,1,1,2,1,1,2,1,5,1,5,2,5,5,1,1,3,1,4,1,1,1,1,1,1,1,4,1,1,4,1,1,1,1,1,2,1,2,1,1,1,5,1,1,3,5,1,1,' \
        '5,5,3,5,3,4,1,1,1,3,1,1,3,1,1,1,1,1,1,5,1,3,1,5,1,1,4,1,3,1,1,1,2,1,1,1,2,1,5,1,1,1,1,4,1,3,2,3,4,1,3,5,3,' \
        '4,1,4,4,4,1,3,2,4,1,4,1,1,2,1,3,1,5,5,1,5,1,1,1,5,2,1,2,3,1,4,3,3,4,3'
# endregion --------------


class Lanternfishes:
    def __init__(self, initial_age, number):
        self.curr_age = initial_age
        self.number = number

    def reproduce(self):
        self.curr_age -= 1
        if self.curr_age < 0:
            self.curr_age = 6
            return True
        else:
            return False


def calculate_population(input, days:int):
    lst = [int(i) for i in input.split(',')]
    fish = []
    for i in range(1, 6):
        fishcount = lst.count(i)
        fish.append(Lanternfishes(i, fishcount))

    for day in range(days):
        additional_fish = []
        for i in fish:
            if i.reproduce():
                additional_fish.append(Lanternfishes(8, i.number))

        fish = fish + additional_fish

        if day % 10 == 0:  # regular cleanup of duplicate ages and merging of populations
            curr_fish = 0
            while True:
                for ind, val in enumerate(fish):
                    if ind != curr_fish:
                        if val and fish[curr_fish] and val.curr_age == fish[curr_fish].curr_age:
                            fish[curr_fish].number += val.number
                            fish[ind] = None

                curr_fish += 1
                fish = [i for i in fish if i]
                if curr_fish >= len(fish):
                    break

    final_fish_count = 0
    for i in fish:
        final_fish_count += i.number
    return final_fish_count


if __name__ == "__main__":
    print('Part 1 =', calculate_population(INPUT, 80))  # 379414
    print('*'*30)
    print('Part 2 =', calculate_population(INPUT, 256))  # 1705008653296
