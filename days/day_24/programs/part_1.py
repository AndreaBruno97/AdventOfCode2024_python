from common import *
import re


class Part_1(BaseClass):

    def __init__(self):
        super().__init__()

    def execute_internal(self, filepath):
        input_value_str, input_connection_str = open_file(filepath).split("\n\n")

        input_dict = dict()
        for line in input_value_str.split("\n"):
            name, val_str = line.split(": ")
            input_dict[name] = int(val_str)

        pattern = r"(\w{3}) (AND|OR|XOR) (\w{3}) -> (\w{3})"
        connection_list = re.findall(pattern, input_connection_str)

        while len(connection_list) > 0:
            cur_index = [index for index, val in enumerate(connection_list) if val[0] in input_dict and val[2] in input_dict][0]
            in1, operation, in2, out = connection_list.pop(cur_index)

            val1 = input_dict[in1]
            val2 = input_dict[in2]

            if operation == "AND":
                input_dict[out] = val1 & val2
            elif operation == "OR":
                input_dict[out] = val1 | val2
            elif operation == "XOR":
                input_dict[out] = val1 ^ val2

        result_list = [x for x in input_dict.items() if x[0][0] == "z"]
        result_list.sort(reverse=True, key=lambda x: x[0])
        result_str = "".join([str(x[1]) for x in result_list])

        return int(result_str, 2)


p1 = Part_1()
p1.test(4, [("example_2.txt", 2024)])
p1.execute()
