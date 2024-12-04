from common import *
import numpy as np


class Part_2(BaseClass):

    def __init__(self):
        super().__init__()

    def execute_internal(self, filepath):
        xmas = np.array([
            ["M", "", "S"],
            ["", "A", ""],
            ["M", "", "S"]
        ])

        matrix = np.array(open_file_str_matrix(filepath))
        rows = len(matrix)
        cols = len(matrix[0])
        xmas_rows = len(xmas)
        xmas_cols = len(xmas[0])

        # All possible orientations of X-MAS matrix
        # Then each matrix is flattened, to help future checks
        xmas_list = [
            xmas.flatten(),
            xmas.transpose().flatten(),
            xmas[:, ::-1].flatten(),
            xmas[:, ::-1].transpose().flatten()
        ]
        total_xmas = 0

        for r in range(rows - xmas_rows + 1):
            for c in range(cols - xmas_cols + 1):
                sub_matrix = matrix[r:r+xmas_rows, c:c+xmas_cols]
                sub_matrix_flat = sub_matrix.flatten()
                for cur_xmas in xmas_list:
                    if np.all([ref == "" or ref == sub for ref, sub in zip(cur_xmas, sub_matrix_flat)]):
                        total_xmas += 1
        return total_xmas


p2 = Part_2()
p2.test(9)
p2.execute()
