from common import *
import re
import time


class Part_2(BaseClass):

    def __init__(self):
        super().__init__()

    def execute_internal(self, filepath):

        MAX_X = 101
        MAX_Y = 103

        if "input.txt" not in filepath:
            MAX_X = 11
            MAX_Y = 7

        file_str = open_file(filepath)
        pattern = r"p=(\-*\d+),(\-*\d+) v=(\-*\d+),(\-*\d+)"
        guard_list = [[int(y) for y in x] for x in re.findall(pattern, file_str)]

        steps = 0
        while True:
            guard_set = set()
            for p_x, p_y, v_x, v_y in guard_list:
                end_x = (p_x + (v_x * steps)) % MAX_X
                end_y = (p_y + (v_y * steps)) % MAX_Y

                guard_set.add((end_x, end_y))

            print_map(MAX_X, MAX_Y, guard_set)
            print(steps)
            time.sleep(0.1)

            steps += 1

        return -1


def print_map(max_x, max_y, guard_set):
    print_error("-"*max_y)
    for y in range(max_y):
        for x in range(max_x):
            if (x, y) in guard_set:
                print_success("*", end="")
            else:
                print(" ", end="")
        print("")


p2 = Part_2()
p2.execute()
