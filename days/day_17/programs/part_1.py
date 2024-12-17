from common import *
import math
import re


TEST_OUTPUT = "4,6,3,5,6,3,5,2,1,0"


class Part_1(BaseClass):

    def __init__(self):
        super().__init__()

    def execute_internal(self, filepath):
        register_str, program_str = open_file(filepath).split("\n\n")

        pattern = r"Register A: (\d+)\nRegister B: (\d+)\nRegister C: (\d+)"
        reg_a, reg_b, reg_c = [[int(y) for y in x] for x in re.findall(pattern, register_str)][0]
        program = [int(x) for x in program_str.replace("Program: ", "").split(",")]
        output = []
        pointer = 0

        while pointer < len(program):
            opcode = program[pointer]
            operand = program[pointer + 1]
            combo_op = operand if 0 <= operand <= 3 \
                else reg_a if operand == 4 \
                else reg_b if operand == 5 \
                else reg_c if operand == 6 \
                else 0

            if opcode == 0:
                # adv - Division in register A
                reg_a = math.floor(reg_a/math.pow(2, combo_op))
            elif opcode == 1:
                # bxl - Bitwise XOR, register B
                reg_b = reg_b ^ operand
            elif opcode == 2:
                # bst - Combo modulo 8
                reg_b = combo_op % 8
            elif opcode == 3:
                # jnz - Conditional jump
                if reg_a != 0:
                    pointer = operand
                    continue
            elif opcode == 4:
                # bxc - Bitwise XOR, register B and C
                reg_b = reg_b ^ reg_c
            elif opcode == 5:
                # out - Output
                output.append(str(combo_op % 8))
            elif opcode == 6:
                # bdv - Division in register B
                reg_b = math.floor(reg_a/math.pow(2, combo_op))
            elif opcode == 7:
                # cdv - Division in register C
                reg_c = math.floor(reg_a/math.pow(2, combo_op))

            pointer += 2

        output_str = ",".join(output)
        is_correct = output_str == TEST_OUTPUT
        if "input.txt" in filepath:
            print_result(output_str)
        elif is_correct:
            print_success(output_str)
        else:
            print_error(output_str)
        return 0 if is_correct else -1


p1 = Part_1()
p1.test(0)
p1.execute()
