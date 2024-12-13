from common import *
import re
import sys


class Part_2(BaseClass):

    def __init__(self):
        super().__init__()

    def execute_internal(self, filepath):
        input_str = open_file(filepath)
        pattern = r"Button A: X\+(\d+), Y\+(\d+)\n" \
                  r"Button B: X\+(\d+), Y\+(\d+)\n" \
                  r"Prize: X=(\d+), Y=(\d+)"

        machine_list = [[int(y) for y in x]for x in re.findall(pattern, input_str)]

        total = 0
        for a_x, a_y, b_x, b_y, prize_x, prize_y in machine_list:
            prize_x += 10000000000000
            prize_y += 10000000000000

            delta = (a_x * b_y) - (a_y * b_x)

            if delta == 0:
                continue

            b = ((a_x * prize_y) - (a_y * prize_x)) / delta

            if not b.is_integer():
                continue

            b = int(b)

            a = (prize_x - (b_x * b)) / a_x

            if not a.is_integer():
                continue

            a = int(a)

            total += (3 * a) + b

        return total


p2 = Part_2()
p2.test(0)
p2.execute()
