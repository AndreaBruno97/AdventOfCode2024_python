from common import *


class Part_1(BaseClass):

    def __init__(self):
        super().__init__()

    def execute_internal(self, filepath):
        input_list = open_file_lines(filepath)

        safe_report_num = 0

        for index, cur_list in enumerate(input_list):
            report = [int(x) for x in cur_list.split(" ")]
            if report[1] - report[0] > 0:
                # Increase
                min_difference = 1
                max_difference = 3
            else:
                # Decrease
                min_difference = -3
                max_difference = -1

            level_difference = [right - left for (left, right) in zip(report, report[1:])]

            if all(min_difference <= cur_difference <= max_difference for cur_difference in level_difference):
                safe_report_num += 1

        return safe_report_num


p1 = Part_1()
p1.test(2)
p1.execute()
