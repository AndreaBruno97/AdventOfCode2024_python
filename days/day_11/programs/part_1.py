from common import *


ROUNDS = 25


class Part_1(BaseClass):

    def __init__(self):
        super().__init__()

    def execute_internal(self, filepath):
        stone_line = [int(x) for x in open_file(filepath).split(" ")]

        for cur_round in range(ROUNDS):
            i = 0
            while i in range(len(stone_line)):
                stone_val = stone_line[i]
                num_digits = len(str(stone_val))

                if stone_val == 0:
                    stone_line[i] = 1
                elif num_digits % 2 == 0:
                    # Even number of digits
                    middle_power_ten = pow(10, int(num_digits / 2))
                    stone_line[i] = int(stone_val / middle_power_ten)
                    stone_line.insert(0, int(stone_val % middle_power_ten))
                    i += 1
                else:
                    # Odd number of digits
                    stone_line[i] = stone_val * 2024
                i += 1
            print("Round ", cur_round + 1)

        return len(stone_line)


p1 = Part_1()
p1.test(55312)
p1.execute()
