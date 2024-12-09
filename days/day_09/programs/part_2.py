from common import *
import math


class Node:
    def __init__(self, size: int, index: int, is_file: bool):
        super().__init__()
        self.size = size
        self.index = index
        self.is_file = is_file
        self.next = None
        self.prev = None


class Part_2(BaseClass):

    def __init__(self):
        super().__init__()

    def execute_internal(self, filepath):
        disk_map = open_file_digit_array(filepath)

        # Create starting linked list with id and size of each file and space block
        # at the starting position.
        head = None
        tail = None
        for index, block in enumerate(disk_map):
            cur_node = Node(block, math.floor(index / 2), index % 2 == 0)
            cur_node.prev = tail

            if head is None:
                # first element
                head = cur_node

            if tail is not None:
                tail.next = cur_node

            tail = cur_node

        file_to_move = tail
        while file_to_move is not None:
            next_file_to_check = file_to_move.prev
            if file_to_move.is_file is False:
                file_to_move = file_to_move.prev
            else:
                file_index = file_to_move.index
                space_to_fill = head
                while space_to_fill is not None and space_to_fill != file_to_move:
                    if space_to_fill.is_file is False and space_to_fill.size >= file_to_move.size:
                        space_to_fill.size -= file_to_move.size

                        new_file = Node(file_to_move.size, file_to_move.index, True)
                        file_to_move.is_file = False

                        if space_to_fill.prev is not None:
                            space_to_fill.prev.next = new_file
                        new_file.prev = space_to_fill.prev
                        space_to_fill.prev = new_file
                        new_file.next = space_to_fill

                        break
                    else:
                        space_to_fill = space_to_fill.next

                file_to_move = next_file_to_check

        checksum = 0
        cur_pos = 0
        cur_file = head
        while cur_file is not None:
            if cur_file.is_file:
                checksum += get_local_checksum(cur_pos, cur_file.size, cur_file.index)
            cur_pos += cur_file.size
            cur_file = cur_file.next

        return checksum


def get_local_checksum(block_pos, block_size, block_id):
    position_sum = sum(range(block_pos, block_pos + block_size))
    return position_sum * block_id


def print_memory(cur_node, index_to_highlight=-1):
    while cur_node is not None:
        if cur_node.is_file:
            if cur_node.index == index_to_highlight:
                print_result(str(cur_node.index) * cur_node.size, end="")
            else:
                print(str(cur_node.index)*cur_node.size, end="")
        else:
            print("."*cur_node.size, end="")
        cur_node = cur_node.next

    print()


p2 = Part_2()
p2.test(2858)
p2.execute()
