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


class Part_1(BaseClass):

    def __init__(self):
        super().__init__()

    def execute_internal(self, filepath):
        matrix = open_file_str_matrix(filepath)
        rows, cols = len(matrix), len(matrix[0])
        start_pos = (0, 0)
        end_pos = (0, 0)
        visited_set = set()
        unvisited_set = set()
        distance_dict = dict()
        previous_dict = dict()
        direction_dict = dict()

        for r in range(rows):
            for c in range(cols):
                cur_coord = (r, c)
                cur_tile = matrix[r][c]

                if cur_tile == WALL:
                    continue

                unvisited_set.add(cur_coord)
                distance_dict[cur_coord] = sys.maxsize

                if cur_tile == START:
                    start_pos = cur_coord
                    distance_dict[cur_coord] = 0
                    previous_dict[cur_coord] = cur_coord
                    direction_dict[cur_coord] = RIGHT

                if cur_tile == END:
                    end_pos = cur_coord

        while len(unvisited_set) > 0:
            unvisited_distance_dict = {key: val for key, val in distance_dict.items() if key in unvisited_set}
            min_distance = min(unvisited_distance_dict.values())
            cur_node = [key for key, val in unvisited_distance_dict.items() if val == min_distance][0]
            unvisited_set.remove(cur_node)

            for direction, delta_coord in delta_directions.items():
                delta_r, delta_c = delta_coord
                new_r, new_c = cur_node[0] + delta_r, cur_node[1] + delta_c
                new_node = (new_r, new_c)
                if (matrix[new_r][new_c] == WALL) or (new_node not in unvisited_set):
                    continue
                cur_distance = distance_dict[new_node]
                new_distance = distance_dict[cur_node] + 1
                if direction_dict[cur_node] != direction:
                    new_distance += 1000

                if new_distance < cur_distance:
                    distance_dict[new_node] = new_distance
                    previous_dict[new_node] = cur_node
                    direction_dict[new_node] = direction
        #print_distances(distance_dict, rows, cols)
        return distance_dict[end_pos]


def print_distances(distance_dict, rows, cols):
    size = math.ceil(math.log10(max([x for x in distance_dict.values() if x != sys.maxsize])))
    for r in range(rows):
        for c in range(cols):
            if (r, c) in distance_dict.keys():
                print(" " + str(distance_dict[(r, c)]).zfill(size) + " ", end="")
            else:
                print("." * (size + 2), end="")

        print("")


p1 = Part_1()
p1.test(7036, [("example_2.txt", 11048)])
p1.execute()
