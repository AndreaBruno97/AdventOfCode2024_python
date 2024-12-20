from common import *
import numpy as np


WALL = "#"
CLEAR = "."
START = "S"
END = "E"


UP = (-1, 0)
RIGHT = (0, 1)
DOWN = (1, 0)
LEFT = (0, -1)

dir_list = [UP, RIGHT, DOWN, LEFT]


def move(cur_pos, delta):
    return (cur_pos[0] + delta[0], cur_pos[1] + delta[1])


class Part_2(BaseClass):

    def __init__(self):
        super().__init__()

    def execute_internal(self, filepath):
        matrix = np.array(open_file_str_matrix(filepath))
        rows = len(matrix)
        cols = len(matrix[0])

        start_pos = [*zip(*np.where(matrix == START))][0]
        end_pos = [*zip(*np.where(matrix == END))][0]

        def get_neighbor(cur_node):
            possible_neighbors = [move(cur_node, delta) for delta in dir_list]

            return [(cur_nei, 1) for cur_nei in possible_neighbors if
                    0 <= cur_nei[0] < rows and 0 <= cur_nei[1] < cols and matrix[cur_nei] != WALL]

        distance_dict, previous_dict = dijkstra(start_pos, get_neighbor)

        path_list = []
        last_pos = end_pos
        while previous_dict[last_pos] != last_pos:
            path_list.append(last_pos)
            last_pos = previous_dict[last_pos]
        path_list.append(start_pos)

        path_list.reverse()
        # cheat_dict = dict()  # Key: couple start-end pos, Value: max time saved
        max_len = len(path_list) - 1
        total = 0

        for start_cheat_i in range(len(path_list)):
            start_cheat_pos = path_list[start_cheat_i]

            for end_cheat_i in range(start_cheat_i + 1, len(path_list)):
                end_cheat_pos = path_list[end_cheat_i]

                # Manhattan distance
                distance = abs(end_cheat_pos[0] - start_cheat_pos[0]) + abs(end_cheat_pos[1] - start_cheat_pos[1])
                if distance <= 20:
                    start_len = start_cheat_i
                    remaining_len = max_len - end_cheat_i
                    time_saved = max_len - (start_len + remaining_len + distance)
                    #  cheat_dict[(start_cheat_pos, end_cheat_pos)] = time_saved
                    if time_saved >= 100:
                        total += 1

        return total


p2 = Part_2()
p2.test(0)
p2.execute()
