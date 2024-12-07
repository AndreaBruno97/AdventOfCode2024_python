from common import *


class Part_1(BaseClass):

    def __init__(self):
        super().__init__()

    def execute_internal(self, filepath):
        str_list = [x.split(": ") for x in open_file_lines(filepath)]
        eq_list = [
            [
                int(tot),
                [
                    int(param)
                    for param in param_str.split(" ")
                ]
            ] for tot, param_str in str_list
        ]

        total_sum = 0
        for total, param_list in eq_list:
            cur_total_results = check_operators(total, param_list[0], param_list[1:])
            if cur_total_results > 0:
                total_sum += total

        return total_sum


def check_operators(total, cur_total, param_list):
    if len(param_list) == 0:
        if total == cur_total:
            return 1
        else:
            return 0

    cur_total_results = 0
    cur_total_results += check_operators(total, cur_total + param_list[0], param_list[1:])
    cur_total_results += check_operators(total, cur_total * param_list[0], param_list[1:])

    return cur_total_results


p1 = Part_1()
p1.test(3749)
p1.execute()
