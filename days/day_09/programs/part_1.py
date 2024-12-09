from common import *
import math


class Part_1(BaseClass):

    def __init__(self):
        super().__init__()

    def execute_internal(self, filepath):
        disk_map = open_file_digit_array(filepath)

        last_i = len(disk_map) - 1
        cur_i = 0
        block_pos = 0

        checksum = 0

        while cur_i <= last_i:
            block_size = disk_map[cur_i]
            block_id = math.floor(cur_i/2)

            if cur_i % 2 == 0:
                # Even index: occupied blocks
                checksum += get_local_checksum(block_pos, block_size, block_id)
                block_pos += block_size
            else:
                # Odd index: empty blocks
                while cur_i <= last_i and block_size > 0:
                    last_block_size = disk_map[last_i]
                    last_block_id = math.floor(last_i/2)

                    if last_block_size > 0:
                        size_to_compute = min(last_block_size, block_size)
                        checksum += get_local_checksum(block_pos, size_to_compute, last_block_id)
                        block_pos += size_to_compute

                        block_size -= size_to_compute
                        disk_map[last_i] -= size_to_compute
                    else:
                        # Go to the previous occupied block set
                        last_i -= 2

            cur_i += 1

        return checksum


def get_local_checksum(block_pos, block_size, block_id):
    position_sum = sum(range(block_pos, block_pos + block_size))
    return position_sum * block_id


p1 = Part_1()
p1.test(1928, [("example_2.txt", 60)])
p1.execute()
