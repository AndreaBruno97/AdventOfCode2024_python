from common import *
import numpy as np


class Part_2(BaseClass):
    visited_char = "X"
    path_char = "."
    obstacle_char = "#"
    edge_char = "*"
    start_char = "^"
    # Directions:
    # 0 North
    # 1 East
    # 2 South
    # 3 West
    delta_dict = {
        0: (-1, 0),  # North: previous row, same column
        1: (0, 1),  # East: same row, next column
        2: (1, 0),  # South: next row, same column
        3: (0, -1)  # West: Same row, previous column
    }

    def __init__(self):
        super().__init__()

    def execute_internal(self, filepath):
        lab = np.array(open_file_str_matrix(filepath))
        # Adding a ring of obstacles around the map
        lab = np.pad(lab, pad_width=((1, 1), (1, 1)), mode='constant', constant_values=self.edge_char)
        start_row, start_col = [x[0] for x in np.where(lab == self.start_char)]

        # Getting the standard path
        _, path_history = self.is_loop(lab, start_row, start_col)

        # For each tile in the path, check if turning right creates a loop
        distinct_path_list = {(r, c) for (r, c, _) in path_history[1:]}
        cur_path_check = 1
        total_loop = 0

        for path_row, path_col in distinct_path_list:
            lab[path_row, path_col] = self.obstacle_char
            cur_path_check += 1

            is_loop, _ = self.is_loop(lab, start_row, start_col)
            if is_loop:
                total_loop += 1

            lab[path_row, path_col] = self.path_char

        return total_loop

    def is_loop(self, lab, start_row, start_col):
        cur_direction = 0
        cur_row, cur_col = start_row, start_col
        path_history = []

        while True:
            path_history.append((cur_row, cur_col, cur_direction))
            delta_row, delta_col = self.delta_dict[cur_direction]
            next_row = cur_row + delta_row
            next_col = cur_col + delta_col

            if lab[next_row, next_col] == self.edge_char:
                return False, path_history
            elif (next_row, next_col, cur_direction) in path_history:
                return True, path_history
            elif lab[next_row, next_col] == self.obstacle_char:
                cur_direction = (cur_direction + 1) % 4
            else:
                cur_row, cur_col = next_row, next_col


p2 = Part_2()
p2.test(6)
p2.execute()
