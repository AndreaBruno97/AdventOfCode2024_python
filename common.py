import math
import sys
from enum import Enum
import numpy as np
from colorama import Fore, Style
from typing import Callable


class FileType(Enum):
    INPUT = 1
    TEST = 2
    OTHER = 3


# region Print Functions with colors

def print_error(*text, end="\n"):
    print_colored(text, color=Fore.RED, end=end)


def print_success(*text, end="\n"):
    print_colored(text, color=Fore.GREEN, end=end)


def print_title(*text, end="\n"):
    print_colored(text, color=Fore.BLUE, end=end)


def print_result(*text, end="\n"):
    print_colored(text, color=Fore.YELLOW, end=end)


def print_debug(*text, end="\n"):
    print_colored(text, color=Fore.LIGHTBLUE_EX, end=end)


def print_colored(*text, color: Fore, end="\n"):
    print(*[color + str(x) + Style.RESET_ALL for x in text[0]], end=end)


# endregion


# region File Read functions

def open_file(filename) -> str:
    with open(filename) as f:
        content = f.read()
    return content


def open_file_lines(filename) -> list[str]:
    with open(filename) as f:
        content = f.readlines()
    return [x.replace("\n", "") for x in content]


def open_file_char_array(filename) -> list[str]:
    return list(open_file(filename))


def open_file_digit_array(filename) -> list[int]:
    return [int(x) for x in open_file_char_array(filename)]


def open_file_str_matrix(filename) -> list[list[str]]:
    return [list(x) for x in open_file_lines(filename)]


def open_file_int_array(filename) -> list[int]:
    return [int(x) for x in open_file_lines(filename)]


def open_file_int_matrix(filename) -> list[list[int]]:
    return [[int(y) for y in x.strip()] for x in open_file_lines(filename)]


def open_file_str_matrix_guarded(filename, border_value="", border_size=1) -> np.array:
    return guard_matrix(open_file_str_matrix(filename), border_value, border_size)


def open_file_int_matrix_guarded(filename, border_value=0) -> np.array:
    return guard_matrix(open_file_int_matrix(filename), border_value)


# endregion


# region Utility

def guard_matrix(matrix, border_value, border_size=1) -> np.array:
    return np.pad(
        matrix,
        pad_width=((border_size, border_size), (border_size, border_size)),
        mode='constant',
        constant_values=border_value
    )


def print_matrix(matrix: list[list[any]], highlight_point: tuple[int, int] = None, highlight_list: list[tuple[int, int]] = None):
    rows = len(matrix)
    cols = len(matrix[0])

    for r in range(rows):
        for c in range(cols):
            cur_val = matrix[r][c]
            if (r, c) == highlight_point or (r, c) in highlight_list:
                print_result(cur_val, end="")
            else:
                print(cur_val, end="")

        print()


# INPUT
# get_neighbors: for a single node, retrieves all neighbors with their weights
#       input: current node    example: (0, 0)
#       output: list of neighbors with
#               - neighbor node
#               - weight to reach that node
#                example [[(0,1), 1], [(0, 2), 2]]
#
# update_on_path_find: when a new node is updated, call a lambda to allow the caller
#                       to perform additional actions
#       input: current node     example: (0, 0)
#              new node     example: (0, 0)
#
# OUTPUT
# distance_dict: dictionary with each visited node as key and its minimum
#               distance from the starting point as value
# previous_dict: dictionary with each visited node as key and its previous
#               node in the minimum path as value
#
#
def dijkstra(
        start_pos: tuple[int, int],
        get_neighbors: Callable[[tuple[int, int]], list[tuple[tuple[int, int], int]]],
        update_on_path_find: Callable[[tuple[int, int], tuple[int, int]], None] = None
) -> tuple[dict[tuple[int, int], int], dict[tuple[int, int], tuple[int, int]]]:
    unvisited_set = set()
    visited_set = set()
    distance_dict = dict()
    previous_dict = dict()

    unvisited_set.add(start_pos)
    distance_dict[start_pos] = 0
    previous_dict[start_pos] = start_pos

    def get_distance(cur_pos):
        return distance_dict[cur_pos] if cur_pos in distance_dict else sys.maxsize

    while len(unvisited_set) > 0:
        unvisited_distance_dict = {key: val for key, val in distance_dict.items() if key in unvisited_set}
        min_distance = min(unvisited_distance_dict.values())
        cur_node = [key for key, val in unvisited_distance_dict.items() if val == min_distance][0]
        unvisited_set.remove(cur_node)
        visited_set.add(cur_node)

        for new_node, new_node_weight in get_neighbors(cur_node):
            if new_node in visited_set:
                continue

            unvisited_set.add(new_node)
            cur_distance = get_distance(new_node)
            new_distance = get_distance(cur_node) + new_node_weight

            if new_distance < cur_distance:
                distance_dict[new_node] = new_distance
                previous_dict[new_node] = cur_node
                if update_on_path_find:
                    update_on_path_find(cur_node, new_node)

    return distance_dict, previous_dict


def print_distances_matrix(distance_dict, rows, cols):
    size = math.ceil(math.log10(max([x for x in distance_dict.values() if x != sys.maxsize])))
    for r in range(rows):
        for c in range(cols):
            if (r, c) in distance_dict.keys():
                print(" " + str(distance_dict[(r, c)]).zfill(size) + " ", end="")
            else:
                print("." * (size + 2), end="")

        print("")


# endregion


class BaseClass:
    def __init__(self):
        pass

    # region Execution Functions

    def execute_internal(self, filepath) -> int:
        raise NotImplementedError('Method "executeInternal" not implemented.')

    def execute(self, filetype=FileType.INPUT, filename='', solution_in_new_line=False) -> int:
        if filetype == FileType.OTHER and filename == '':
            raise Exception('File name not specified')

        if filetype == FileType.INPUT:
            filename = "input.txt"
        elif filetype == FileType.TEST:
            filename = "example.txt"

        complete_filename = f"../input_files/{filename}"

        print(f"Start Execution {filename}:")
        result = self.execute_internal(complete_filename)

        print(f"End Execution {filename}, result: ", end="\n" if solution_in_new_line else "")
        print_result(f"{result}")
        return result

    def test(self,
             expected_result,
             additional_test_list: list[(str, int)] = [],
             solution_in_new_line=False):

        print_title("Test:")

        if expected_result is not None:
            main_test_result = self.execute(FileType.TEST, solution_in_new_line=solution_in_new_line)
            if main_test_result != expected_result:
                print_error("Main test failed")
            else:
                print_success("Main test succeeded")

        for cur_filename, cur_expected_value in additional_test_list:
            cur_test_result = self.execute(FileType.OTHER, cur_filename, solution_in_new_line=solution_in_new_line)
            if cur_test_result != cur_expected_value:
                print_error(f"Test {cur_filename} failed")
            else:
                print_success(f"Test {cur_filename} succeeded")
        print_title("End test\n")
    # endregion
