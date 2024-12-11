from common import *


ROUNDS = 75
stone_dict = dict()


class Part_2(BaseClass):

    def __init__(self):
        super().__init__()

    def execute_internal(self, filepath):
        stone_line = [int(x) for x in open_file(filepath).split(" ")]

        total = 0
        for stone in stone_line:
            total += search_stone(stone, 0)

        return total


def search_stone(stone_val, depth):
    if depth == ROUNDS:
        return 1

    if (stone_val, depth) in stone_dict.keys():
        return stone_dict[(stone_val, depth)]

    num_digits = len(str(stone_val))
    total = 0
    if stone_val == 0:
        total = search_stone(1, depth + 1)
    elif num_digits % 2 == 0:
        # Even number of digits
        middle_power_ten = pow(10, int(num_digits / 2))

        total += search_stone(int(stone_val / middle_power_ten), depth + 1)
        total += search_stone( int(stone_val % middle_power_ten), depth + 1)
    else:
        # Odd number of digits
        total = search_stone(stone_val * 2024, depth + 1)

    stone_dict[(stone_val, depth)] = total
    return total

p2 = Part_2()
#p2.test(0)
p2.execute()
