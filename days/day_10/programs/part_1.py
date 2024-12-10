from common import *
import numpy as np


class Part_1(BaseClass):

    def __init__(self):
        super().__init__()

    def execute_internal(self, filepath):
        _map = np.array(open_file_int_matrix(filepath))
        _map = np.pad(_map, pad_width=((1, 1), (1, 1)), mode='constant', constant_values=20)
        trailhead_list = [*zip(*np.where(_map == 0))]

        total = 0
        for cur_trailhead in trailhead_list:
            cur_top_set = set()
            search_trail(cur_trailhead, _map, cur_top_set)
            total += len(cur_top_set)

        return total


def search_trail(cur_pos, _map, top_set: set):
    cur_x, cur_y = cur_pos
    cur_val = _map[cur_x, cur_y]

    if cur_val == 9:
        top_set.add(cur_pos)
        return

    for delta_x, delta_y in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        new_x = cur_x + delta_x
        new_y = cur_y + delta_y
        next_val = _map[new_x, new_y]
        if next_val == cur_val + 1:
            search_trail((new_x, new_y), _map, top_set)

    return


p1 = Part_1()
p1.test(36, [("example_2.txt", 1)])
p1.execute()
