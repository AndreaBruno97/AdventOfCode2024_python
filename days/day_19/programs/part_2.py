from common import *


class Part_2(BaseClass):

    def __init__(self):
        super().__init__()

    def execute_internal(self, filepath):
        towel_list_str, pattern_list_str = open_file(filepath).split("\n\n")
        towel_list = towel_list_str.split(", ")
        pattern_list = pattern_list_str.split("\n")


        towel_dict = dict()

        total = 0
        for i, pattern in enumerate(pattern_list):
            total += count_pattern(pattern, towel_list, towel_dict)

        return total


def count_pattern(pattern, towel_list, towel_dict):
    if pattern in towel_dict:
        return towel_dict[pattern]

    if len(pattern) == 0:
        return 1

    total_count = 0
    for towel in towel_list:
        tow_len = len(towel)
        if pattern[:tow_len] == towel:
            total_count += count_pattern(pattern[tow_len:], towel_list, towel_dict)

    towel_dict[pattern] = total_count
    return total_count


p2 = Part_2()
p2.test(16)
p2.execute()
