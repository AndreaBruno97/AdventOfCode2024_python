from common import *


class Part_2(BaseClass):

    def __init__(self):
        super().__init__()

    def execute_internal(self, filepath):
        input_list = open_file_lines(filepath)

        safe_report_num = 0

        for index, cur_list in enumerate(input_list):
            original_report = [int(x) for x in cur_list.split(" ")]

            for report in [original_report] + [original_report[0:x] + original_report[x+1:] for x in range(len(original_report))]:
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
                    break

        return safe_report_num


p2 = Part_2()
p2.test(4)
p2.execute()
