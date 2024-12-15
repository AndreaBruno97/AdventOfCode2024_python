from common import *


WALL = "#"
CLEAR = "."
BOX = "O"
BOX_L = "["
BOX_R = "]"
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


class Part_2(BaseClass):

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
                left_coord = (r, 2*c)
                right_coord = (r, (2*c)+1)

                if cur_element == CLEAR:
                    continue
                elif cur_element == WALL:
                    map_dict[left_coord] = WALL
                    map_dict[right_coord] = WALL
                elif cur_element == BOX:
                    map_dict[left_coord] = BOX_L
                    map_dict[right_coord] = BOX_R
                elif cur_element == ROBOT:
                    map_dict[left_coord] = ROBOT

        cols *= 2

        move_list = [move for move in move_list_str.replace("\n", "")]

        for cur_move in move_list:
            robot_pos = [key for key, value in map_dict.items() if value == ROBOT][0]
            can_push = push(robot_pos, cur_move, map_dict, allow_push=False)
            if can_push:
                push(robot_pos, cur_move, map_dict, allow_push=True)

        box_coord_list = [key for key, value in map_dict.items() if value == BOX_L]

        return sum([(100 * row) + col for row, col in box_coord_list])


def print_map(map_dict, rows, cols, highlight=(-1, -1)):
    for r in range(rows):
        for c in range(cols):
            char_to_print = CLEAR
            if (r, c) in map_dict:
                char_to_print = map_dict[(r, c)]

            if (r, c) == highlight:
                print_result(char_to_print, end="")
            else:
                print(char_to_print, end="")
        print("")


def push(cur_pos, direction, map_dict, allow_push=True):
    if cur_pos not in map_dict:
        # Clear tile
        return True

    cur_value = map_dict[cur_pos]
    if cur_value == WALL:
        return False

    delta_dir = DELTA_DICT[direction]
    new_pos = (cur_pos[0] + delta_dir[0], cur_pos[1] + delta_dir[1])

    can_push = True
    if allow_push is False:
        # Recursively check if next element can be pushed
        can_push = push(new_pos, direction, map_dict, allow_push=False)
        if (direction == UP or direction == DOWN) and (cur_value == BOX_R or cur_value == BOX_L):
            if cur_value == BOX_R:
                can_push = can_push and push((new_pos[0], new_pos[1]-1), direction, map_dict, allow_push=False)
            if cur_value == BOX_L:
                can_push = can_push and push((new_pos[0], new_pos[1]+1), direction, map_dict, allow_push=False)
    else:
        push(new_pos, direction, map_dict, allow_push=True)
        del map_dict[cur_pos]
        map_dict[new_pos] = cur_value

        if (direction == UP or direction == DOWN) and (cur_value == BOX_R or cur_value == BOX_L):
            if cur_value == BOX_R:
                left_pos = (cur_pos[0], cur_pos[1]-1)
                push(left_pos, direction, map_dict, allow_push=True)
            if cur_value == BOX_L:
                right_pos = (cur_pos[0], cur_pos[1]+1)
                push(right_pos, direction, map_dict, allow_push=True)

    return can_push


p2 = Part_2()
p2.test(None, [("example_2.txt", 9021)])
p2.execute()
