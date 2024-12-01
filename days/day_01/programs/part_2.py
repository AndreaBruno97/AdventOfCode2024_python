from collections import Counter

from common import *


class Part_2(BaseClass):

    def __init__(self):
        super().__init__()

    def execute_internal(self, filepath):
        file_lines = open_file_lines(filepath)

        # Get a list of pairs of numbers.
        # Inner comprehension casts the strings to integers.
        pair_list = [[int(y) for y in x.split("   ")] for x in file_lines]

        # Split the left and right lists
        left_list = [x[0] for x in pair_list]
        right_list = [x[1] for x in pair_list]

        # Create a dictionary with the number of occurrences
        # of each number in the second list
        occurrences_dictionary = Counter(right_list)

        similarity_list = [x * occurrences_dictionary[x] for x in left_list]

        return sum(similarity_list)


p2 = Part_2()
p2.test(31)
p2.execute()
