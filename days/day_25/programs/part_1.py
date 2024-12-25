import itertools

from common import *


FILLED = "#"
EMPTY = "."
ROWS = 7
COLS = 5


class Part_1(BaseClass):

    def __init__(self):
        super().__init__()

    def execute_internal(self, filepath):
        input_str = open_file(filepath)
        input_matrix_list = [[list(rows) for rows in matr_str.split("\n")] for matr_str in input_str.split("\n\n")]

        lock_list = []
        key_list = []

        for matrix in input_matrix_list:
            is_lock = matrix[0][0] == FILLED
            pin_list = []

            for c in range(COLS):
                for r in range(1, ROWS):
                    if (is_lock and matrix[r][c] == EMPTY) or (not is_lock and matrix[r][c] == FILLED):
                        if is_lock:
                            pin_height = r-1
                        else:
                            pin_height = ROWS - r - 1
                        pin_list.append(pin_height)
                        break

            if is_lock:
                lock_list.append(pin_list)
            else:
                key_list.append(pin_list)

        total = 0
        for cur_lock in lock_list:
            for cur_key in key_list:
                is_match = True
                for i in range(COLS):
                    if cur_lock[i] + cur_key[i] > 5:
                        is_match = False
                        break

                if is_match:
                    total += 1

        return total


p1 = Part_1()
p1.test(3)
p1.execute()
