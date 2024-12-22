from common import *


MUL_1_CONST = 64
DIV_CONST = 32
MUL_2_CONST = 2048
PRUNE_CONST = 16777216

ROUND_NUM = 2000


class Part_1(BaseClass):

    def __init__(self):
        super().__init__()

    def execute_internal(self, filepath):
        secret_list = open_file_int_array(filepath)

        total = 0
        for secret in secret_list:
            for i in range(ROUND_NUM):
                mul_1 = secret * MUL_1_CONST
                secret ^= mul_1
                secret %= PRUNE_CONST

                div = math.floor(secret / DIV_CONST)
                secret ^= div
                secret %= PRUNE_CONST

                mul_2 = secret * MUL_2_CONST
                secret ^= mul_2
                secret %= PRUNE_CONST

            total += secret

        return total


p1 = Part_1()
p1.test(37327623)
p1.execute()
