from common import *


class Part_1(BaseClass):

    def __init__(self):
        super().__init__()

    def execute_internal(self, filepath):
        if "input.txt" in filepath:
            MAX_X = 70
            MAX_Y = 70
            FALL_SIZE = 1024
        else:
            MAX_X = 6
            MAX_Y = 6
            FALL_SIZE = 12

        START_NODE = (0, 0)
        END_NODE = (MAX_X, MAX_Y)

        byte_list = [(int(x), int(y)) for x, y in [line.split(",") for line in open_file_lines(filepath)]]
        corrupted_node_list = byte_list[:min(len(byte_list), FALL_SIZE)]

        def get_neighbor(cur_node):
            possible_neighbors = [(cur_node[0] + delta_x, cur_node[1] + delta_y)
                                  for delta_x, delta_y in [(0, 1), (0, -1), (1, 0), (-1, 0)]]

            return [(cur_nei, 1) for cur_nei in possible_neighbors if
                    0 <= cur_nei[0] <= MAX_X and
                    0 <= cur_nei[1] <= MAX_Y and
                    cur_nei not in corrupted_node_list]

        distance_dict, previous_dict = dijkstra(START_NODE, get_neighbor)

        return distance_dict[END_NODE]


p1 = Part_1()
p1.test(22)
p1.execute()
