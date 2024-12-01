from common import *


class Part_1(BaseClass):

    def __init__(self):
        super().__init__()

    def execute_internal(self, filepath):
        file_lines = open_file_lines(filepath)

        # Get a list of pairs of numbers.
        # Inner comprehension casts the strings to integers.
        pair_list = [[int(y) for y in x.split("   ")] for x in file_lines]

        # Split and sort the left and right lists
        left_list = [x[0] for x in pair_list]
        right_list = [x[1] for x in pair_list]
        left_list.sort()
        right_list.sort()

        difference_list = [abs(left_value - right_value) for left_value, right_value in zip(left_list, right_list)]

        return sum(difference_list)


p1 = Part_1()
p1.test(11)
p1.execute()
