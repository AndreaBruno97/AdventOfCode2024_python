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


class Part_1(BaseClass):

    def __init__(self):
        super().__init__()

    def execute_internal(self, filepath):
        matrix = np.array(open_file_str_matrix_guarded(filepath, border_value=WALL, border_size=2))

        start_pos = [*zip(*np.where(matrix == START))][0]
        end_pos = [*zip(*np.where(matrix == END))][0]

        def get_neighbor(cur_node):
            possible_neighbors = [move(cur_node, delta) for delta in dir_list]

            return [(cur_nei, 1) for cur_nei in possible_neighbors if matrix[cur_nei] != WALL]

        distance_dict, previous_dict = dijkstra(start_pos, get_neighbor)

        path_list = []
        last_pos = end_pos
        while previous_dict[last_pos] != last_pos:
            path_list.append(last_pos)
            last_pos = previous_dict[last_pos]
        path_list.append(start_pos)

        path_list.reverse()
        max_len = len(path_list) - 1

        total = 0
        for cur_pos in path_list:
            cur_len = path_list.index(cur_pos)
            for first_cheat_delta in dir_list:
                first_cheat = move(cur_pos, first_cheat_delta)
                if matrix[first_cheat] != WALL:
                    continue

                for second_cheat_delta in dir_list:
                    second_cheat = move(first_cheat, second_cheat_delta)
                    if second_cheat == cur_pos or matrix[second_cheat] == WALL:
                        continue

                    remaining_len = max_len - path_list.index(second_cheat)

                    time_saved = max_len - (cur_len + remaining_len + 2)
                    if time_saved >= 100:
                        total += 1

        #print({k: v for k, v in sorted(cheat_dict.items(), key=lambda item: -item[1])})

        return total


p1 = Part_1()
p1.test(0)
p1.execute()
