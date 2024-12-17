from common import *
import math
import re


class Part_2(BaseClass):

    def __init__(self):
        super().__init__()

    def execute_internal(self, filepath):
        register_str, program_str = open_file(filepath).split("\n\n")

        pattern = r"Register A: (\d+)\nRegister B: (\d+)\nRegister C: (\d+)"
        reg_a, reg_b_start, reg_c_start = [[int(y) for y in x] for x in re.findall(pattern, register_str)][0]
        program = [int(x) for x in program_str.replace("Program: ", "").split(",")]
        program_len = len(program)

        is_success = False
        reg_a_start = 0

        while not is_success:
            if reg_a_start % 1_000_000 == 0:
                print(str(int(reg_a_start/1_000_000)) + "M")
            pointer = 0
            output_pointer = 0
            reg_a = reg_a_start
            reg_b = reg_b_start
            reg_c = reg_c_start
            is_cur_program_equal = True

            while pointer < program_len and is_cur_program_equal:
                opcode = program[pointer]
                operand = program[pointer + 1]
                combo_op = operand if 0 <= operand <= 3 else reg_a if operand == 4 else reg_b if operand == 5 else reg_c if operand == 6 else 0

                if opcode == 0:  # adv - Division in register A
                    reg_a = math.floor(reg_a / math.pow(2, combo_op))
                elif opcode == 1:  # bxl - Bitwise XOR, register B
                    reg_b = reg_b ^ operand
                elif opcode == 2:  # bst - Combo modulo 8
                    reg_b = combo_op % 8
                elif opcode == 3:  # jnz - Conditional jump
                    if reg_a != 0:
                        pointer = operand
                        continue
                elif opcode == 4:  # bxc - Bitwise XOR, register B and C
                    reg_b = reg_b ^ reg_c
                elif opcode == 5:  # out - Output
                    cur_output = combo_op % 8
                    if output_pointer >= program_len or cur_output != program[output_pointer]:  # Exit the current cycle
                        is_cur_program_equal = False
                    else:
                        output_pointer += 1
                elif opcode == 6:  # bdv - Division in register B
                    reg_b = math.floor(reg_a / math.pow(2, combo_op))
                elif opcode == 7:  # cdv - Division in register C
                    reg_c = math.floor(reg_a / math.pow(2, combo_op))

                pointer += 2

            is_cur_program_equal = is_cur_program_equal and output_pointer == program_len

            if not is_cur_program_equal:
                reg_a_start += 1
            else:
                is_success = True

        return reg_a_start


p2 = Part_2()
p2.test(None, [("example_2.txt", 117440)])
p2.execute()
