from common import *
import re


class Part_2(BaseClass):

    def __init__(self):
        super().__init__()

    def execute_internal(self, filepath):
        memory = open_file(filepath)
        mul_pattern = r"mul\((\d+),(\d+)\)"
        do_pattern = r"do\(\)"
        dont_pattern = r"don't\(\)"
        match_list = re.findall(rf"{mul_pattern}|({do_pattern})|({dont_pattern})", memory)

        is_enabled = True
        result = 0
        for first, second, do, dont in match_list:
            if do != "":
                is_enabled = True
            elif dont != "":
                is_enabled = False
            elif is_enabled:
                result += int(first) * int(second)

        return result


p2 = Part_2()
p2.test(161, [("example_2.txt", 48)])
p2.execute()
