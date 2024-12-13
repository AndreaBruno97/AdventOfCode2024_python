from common import *
import re
import sys


MAX_PRESS = 100


class Part_1(BaseClass):

    def __init__(self):
        super().__init__()

    def execute_internal(self, filepath):
        input_str = open_file(filepath)
        pattern = r"Button A: X\+(\d+), Y\+(\d+)\n" \
                  r"Button B: X\+(\d+), Y\+(\d+)\n" \
                  r"Prize: X=(\d+), Y=(\d+)"

        machine_list = [[int(y) for y in x]for x in re.findall(pattern, input_str)]

        total = 0
        for a_delta_x, a_delta_y, b_delta_x, b_delta_y, prize_x, prize_y in machine_list:
            cur_total = sys.maxsize
            for a in range(1, MAX_PRESS+1):
                x_a, y_a = a*a_delta_x, a*a_delta_y
                if x_a > prize_x or y_a > prize_y:
                    break

                b = (prize_x - x_a) / b_delta_x

                if not b.is_integer() or b > MAX_PRESS:
                    continue
                b = int(b)

                if y_a + (b * b_delta_y) != prize_y:
                    continue

                num_token = (3 * a) + b

                if num_token < cur_total:
                    cur_total = num_token

            if cur_total < sys.maxsize:
                total += cur_total

        return total


p1 = Part_1()
p1.test(480)
p1.execute()
