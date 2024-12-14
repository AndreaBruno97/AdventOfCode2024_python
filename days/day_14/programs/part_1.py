from common import *
import math
import re
from functools import reduce
from operator import mul


class Part_1(BaseClass):

    def __init__(self):
        super().__init__()

    def execute_internal(self, filepath):

        MAX_X = 101
        MAX_Y = 103
        STEP_NUM = 100

        if "input.txt" not in filepath:
            MAX_X = 11
            MAX_Y = 7

        file_str = open_file(filepath)
        pattern = r"p=(\-*\d+),(\-*\d+) v=(\-*\d+),(\-*\d+)"
        guard_list = [[int(y) for y in x] for x in re.findall(pattern, file_str)]

        quadrant_dict = dict({
            ((False, False), 0),
            ((False, True), 0),
            ((True, False), 0),
            ((True, True), 0)
        })

        middle_x = math.floor(MAX_X/2)
        middle_y = math.floor(MAX_Y/2)

        for p_x, p_y, v_x, v_y in guard_list:
            end_x = (p_x + (v_x * STEP_NUM)) % MAX_X
            end_y = (p_y + (v_y * STEP_NUM)) % MAX_Y

            if end_x == middle_x or end_y == middle_y:
                continue

            quadrant_dict[(end_x < middle_x, end_y < middle_y)] += 1

        return reduce(mul, quadrant_dict.values())


p1 = Part_1()
p1.test(12)
p1.execute()
