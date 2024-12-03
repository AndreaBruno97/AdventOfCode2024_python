from common import *
import re


class Part_1(BaseClass):

    def __init__(self):
        super().__init__()

    def execute_internal(self, filepath):
        memory = open_file(filepath)
        pattern = r"mul\((\d+),(\d+)\)"
        match_list = re.findall(pattern, memory)
        result_list = [int(first) * int(second) for (first, second) in match_list]

        return sum(result_list)


p1 = Part_1()
p1.test(161)
p1.execute()
