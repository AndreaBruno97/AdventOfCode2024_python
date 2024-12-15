from common import *

WALL = "#"
CLEAR = "."
BOX = "O"
ROBOT = "@"

UP = "^"
DOWN = "v"
LEFT = "<"
RIGHT = ">"

DELTA_DICT = dict({
    UP: (-1, 0),
    DOWN: (1, 0),
    LEFT: (0, -1),
    RIGHT: (0, 1)
})


class Part_1(BaseClass):

    def __init__(self):
        super().__init__()

    def execute_internal(self, filepath):
        matrix_str, move_list_str = open_file(filepath).split("\n\n")
        matrix = [[ch for ch in row] for row in matrix_str.split("\n")]

        rows = len(matrix)
        cols = len(matrix[0])

        map_dict = dict()
        for r in range(rows):
            for c in range(cols):
                cur_element = matrix[r][c]
                if cur_element != CLEAR:
                    map_dict[(r, c)] = cur_element

        move_list = [move for move in move_list_str.replace("\n", "")]

        for cur_move in move_list:
            robot_pos = [key for key, value in map_dict.items() if value == ROBOT][0]
            push(robot_pos, cur_move, map_dict)

        box_coord_list = [key for key, value in map_dict.items() if value == BOX]

        return sum([(100 * row) + col for row, col in box_coord_list])


def push(cur_pos, direction, map_dict):
    if cur_pos not in map_dict:
        # Clear tile
        return

    cur_value = map_dict[cur_pos]
    if cur_value == WALL:
        return

    delta_dir = DELTA_DICT[direction]
    new_pos = (cur_pos[0] + delta_dir[0], cur_pos[1] + delta_dir[1])

    # Recursively push next element
    push(new_pos, direction, map_dict)

    if new_pos not in map_dict:
        del map_dict[cur_pos]
        map_dict[new_pos] = cur_value


p1 = Part_1()
p1.test(2028, [("example_2.txt", 10092)])
p1.execute()
