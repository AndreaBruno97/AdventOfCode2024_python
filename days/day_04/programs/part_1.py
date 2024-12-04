from common import *
import numpy as np
import re



class Part_1(BaseClass):

    def __init__(self):
        super().__init__()

    def execute_internal(self, filepath):
        matrix = np.array(open_file_str_matrix(filepath))
        rows = len(matrix)
        cols = len(matrix[0])

        total_xmas = 0

        # Horizontal
        for cur_row in ["".join(matrix[i]) for i in range(rows)]:
            total_xmas += count_xmas(cur_row)

        # Vertical
        for cur_col in ["".join(matrix[:, i]) for i in range(cols)]:
            total_xmas += count_xmas(cur_col)

        # Diagonal NE-SW
        for cur_diag in range(rows + cols):
            coord_range = range(cur_diag + 1)
            diag_coordinates = zip(coord_range, coord_range[::-1])

            cur_string = "".join([
                matrix[r, c] for r, c in diag_coordinates if 0 <= r < rows and 0 <= c < cols
            ])

            total_xmas += count_xmas(cur_string)

        # Diagonal NW-SE
        for cur_diag in range(rows + cols):
            coord_range = range(cur_diag + 1)
            diag_coordinates = zip(coord_range, coord_range[::-1])

            cur_string = "".join([
                matrix[rows-1 - r, c] for r, c in diag_coordinates if 0 <= r < rows and 0 <= c < cols
            ])

            total_xmas += count_xmas(cur_string)

        return total_xmas


def count_xmas(cur_string):
    return len(re.findall("XMAS", cur_string) + re.findall("SAMX", cur_string))


p1 = Part_1()
p1.test(18)
p1.execute()
