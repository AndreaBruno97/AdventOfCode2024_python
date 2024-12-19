from common import *


class Part_1(BaseClass):

    def __init__(self):
        super().__init__()

    def execute_internal(self, filepath):
        towel_list_str, pattern_list_str = open_file(filepath).split("\n\n")
        towel_set = set(towel_list_str.split(", "))
        pattern_list = pattern_list_str.split("\n")
        impossible_pattern_set = set()

        total = 0
        for i, pattern in enumerate(pattern_list):
            is_possible = create_pattern(pattern, towel_set, impossible_pattern_set)
            if is_possible:
                total += 1

        return total


def create_pattern(pattern, towel_set, impossible_pattern_set):
    if len(pattern) == 0 or pattern in towel_set:
        return True

    if pattern in impossible_pattern_set:
        return False

    for towel in towel_set:
        tow_len = len(towel)
        if pattern[:tow_len] == towel:
            is_possible = create_pattern(pattern[tow_len:], towel_set, impossible_pattern_set)
            if is_possible:
                towel_set.add(pattern)
                return True

    impossible_pattern_set.add(pattern)
    return False


p1 = Part_1()
p1.test(6)
p1.execute()
