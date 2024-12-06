from common import *
import numpy as np


class Part_1(BaseClass):
    visited_char = "X"
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
        3: (0, -1)   # West: Same row, previous column
    }

    def __init__(self):
        super().__init__()

    def execute_internal(self, filepath):
        lab = np.array(open_file_str_matrix(filepath))
        # Adding a ring of obstacles around the map
        lab = np.pad(lab, pad_width=((1, 1), (1, 1)), mode='constant', constant_values=self.edge_char)
        start_row, start_col = [x[0] for x in np.where(lab == self.start_char)]

        cur_direction = 0
        cur_row, cur_col = start_row, start_col

        is_complete = False
        while not is_complete:
            lab[cur_row, cur_col] = self.visited_char
            delta_row, delta_col = self.delta_dict[cur_direction]
            next_row = cur_row + delta_row
            next_col = cur_col + delta_col

            if lab[next_row, next_col] == self.edge_char:
                is_complete = True
            elif lab[next_row, next_col] == self.obstacle_char:
                cur_direction = (cur_direction + 1) % 4
            else:
                cur_row, cur_col = next_row, next_col

        return np.count_nonzero(lab == self.visited_char)


p1 = Part_1()
p1.test(41)
p1.execute()
