from common import *
import itertools
import numpy as np


MUL_1_CONST = 64
DIV_CONST = 32
MUL_2_CONST = 2048
PRUNE_CONST = 16777216

ROUND_NUM = 2000


class Part_2(BaseClass):

    def __init__(self):
        super().__init__()

    def execute_internal(self, filepath):
        secret_list = open_file_int_array(filepath)
        price_list_list = []
        diff_list_list = []
        price_dict_list = []

        for secret in secret_list:
            last_price = secret % 10
            cur_price_list = []
            cur_diff_list = []
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

                cur_price = secret % 10
                cur_price_list.append(cur_price)
                cur_diff_list.append((cur_price - last_price))
                last_price = cur_price

            price_list_list.append(cur_price_list)
            diff_list_list.append(cur_diff_list)

            price_dict = dict()
            for i in range(4, ROUND_NUM - 1):
                price_key = tuple(cur_diff_list[i - 4:i])
                if price_key not in price_dict:
                    price_dict[price_key] = cur_price_list[i-1]
            price_dict_list.append(price_dict)

        total = 0

        for cur_diff_sequence in itertools.product(range(-9, 10), repeat=4):
            print(cur_diff_sequence)
            cur_total = 0

            for price_dict in price_dict_list:
                if cur_diff_sequence in price_dict:
                    cur_total += price_dict[cur_diff_sequence]
            total = max(total, cur_total)

        return total


p2 = Part_2()
p2.test(None, [("example_2.txt", 9), ("example_3.txt", 23)])
p2.execute()
