import math
import sys

from common import *
import numpy as np

WALL = "#"
CLEAR = "."
START = "S"
END = "E"

RIGHT = 0
DOWN = 1
LEFT = 2
UP = 3

delta_directions = dict({
    RIGHT: (0, 1),
    DOWN: (1, 0),
    LEFT: (0, -1),
    UP: (-1, 0)
})


direction_from_delta_dict = dict({
    (0, 1): RIGHT,
    (1, 0): DOWN,
    (0, -1): LEFT,
    (-1, 0): UP
})


class Part_1(BaseClass):

    def __init__(self):
        super().__init__()

    def execute_internal(self, filepath):
        matrix = open_file_str_matrix(filepath)
        rows, cols = len(matrix), len(matrix[0])
        start_pos = (0, 0)
        end_pos = (0, 0)
        direction_dict = dict()

        for r in range(rows):
            for c in range(cols):
                cur_coord = (r, c)
                cur_tile = matrix[r][c]

                if cur_tile == WALL:
                    continue

                if cur_tile == START:
                    start_pos = cur_coord
                    direction_dict[cur_coord] = RIGHT

                if cur_tile == END:
                    end_pos = cur_coord

        def get_neighbors(cur_pos):
            possible_neighbors = [((cur_pos[0] + delta[0], cur_pos[1] + delta[1]), direct)
                                  for direct, delta in delta_directions.items()]

            return [
                ((nei_r, nei_col), 1 if direction_dict[cur_pos] == direct else 1001)
                for (nei_r, nei_col), direct in possible_neighbors if
                0 <= nei_r < rows and
                0 <= nei_col < cols and
                matrix[nei_r][nei_col] != WALL]

        def update_direction(cur_pos, new_pos):
            delta = (new_pos[0] - cur_pos[0], new_pos[1] - cur_pos[1])
            direction_dict[new_pos] = direction_from_delta_dict[delta]

        distance_dict, previous_dict = dijkstra(start_pos, get_neighbors, update_direction)

        """
        path_list = []
        last_pos = end_pos
        while previous_dict[last_pos] != last_pos:
            path_list.append(last_pos)
            last_pos = previous_dict[last_pos]
        path_list.append(start_pos)
        path_len = len(path_list) - 1

        turns = 0
        prev_dir = RIGHT
        prev = path_list[0]
        for cur in path_list[1:]:
            delta = (cur[0] - prev[0], cur[1] - prev[1])
            cur_dir = direction_from_delta_dict[delta]
            if cur_dir != prev_dir:
                turns += 1

            prev_dir = cur_dir
            prev = cur

        print(turns, path_len)
        print_distances_matrix(distance_dict, rows, cols)
        print_matrix(matrix, highlight_list=path_list)
        return (turns * 1000) + path_len
        """

        return distance_dict[end_pos]


p1 = Part_1()
p1.test(7036, [("example_2.txt", 11048)])
p1.execute()
