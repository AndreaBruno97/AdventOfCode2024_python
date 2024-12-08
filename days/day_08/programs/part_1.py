from common import *
from itertools import combinations


class Part_1(BaseClass):

    def __init__(self):
        super().__init__()

    def execute_internal(self, filepath):
        matrix = open_file_str_matrix(filepath)
        rows = len(matrix)
        cols = len(matrix[0])

        antenna_dict = {}
        for r in range(rows):
            for c in range(cols):
                cur_tile = matrix[r][c]
                if cur_tile != ".":
                    # If first antenna of that type, create empty array
                    if cur_tile not in antenna_dict:
                        antenna_dict[cur_tile] = []

                    # Populate dictionary
                    antenna_dict[cur_tile].append((r, c))

        antinode_set = set()
        for antenna_list in antenna_dict.values():
            antenna_pairs = list(combinations(antenna_list, 2))

            for (first_x, first_y), (second_x, second_y) in antenna_pairs:

                first_antinode_x = first_x + (first_x - second_x)
                first_antinode_y = first_y + (first_y - second_y)
                second_antinode_x = second_x + (second_x - first_x)
                second_antinode_y = second_y + (second_y - first_y)

                if 0 <= first_antinode_x < rows and 0 <= first_antinode_y < cols:
                    antinode_set.add((first_antinode_x, first_antinode_y))

                if 0 <= second_antinode_x < rows and 0 <= second_antinode_y < cols:
                    antinode_set.add((second_antinode_x, second_antinode_y))

        return len(antinode_set)


p1 = Part_1()
p1.test(14)
p1.execute()
