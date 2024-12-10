from common import *
import numpy as np


class Part_2(BaseClass):

    def __init__(self):
        super().__init__()

    def execute_internal(self, filepath):
        _map = np.array(open_file_int_matrix(filepath))
        _map = np.pad(_map, pad_width=((1, 1), (1, 1)), mode='constant', constant_values=20)
        trailhead_list = [*zip(*np.where(_map == 0))]

        total = 0
        for cur_trailhead in trailhead_list:
            total += search_trail(cur_trailhead, _map)

        return total


def search_trail(cur_pos, _map):
    total = 0
    cur_x, cur_y = cur_pos
    cur_val = _map[cur_x, cur_y]

    if cur_val == 9:
        return 1

    for delta_x, delta_y in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        new_x = cur_x + delta_x
        new_y = cur_y + delta_y
        next_val = _map[new_x, new_y]
        if next_val == cur_val + 1:
            total += search_trail((new_x, new_y), _map)

    return total


p2 = Part_2()
p2.test(81)
p2.execute()
