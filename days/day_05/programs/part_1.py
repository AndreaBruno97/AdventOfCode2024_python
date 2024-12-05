from common import *
import math


class Part_1(BaseClass):

    def __init__(self):
        super().__init__()

    def execute_internal(self, filepath):
        file_str = open_file(filepath)
        rule_str, update_str = file_str.split("\n\n")

        rule_list = [rule.split("|") for rule in rule_str.split("\n")]
        update_list = [update.split(",") for update in update_str.split("\n")]

        total = 0

        for update in update_list:
            # Searching the i-th element for a broken rule
            # Not useful to test the first element
            is_correct = True

            for i in range(1, len(update)):
                for k in range(i):
                    # i is the current element in the update list
                    # k is one of the previous elements we are testing
                    #
                    # The correct rule would have the element in i AFTER the element in k
                    # But if we find the rule with i BEFORE k, the update list is incorrect

                    if [update[i], update[k]] in rule_list:
                        is_correct = False
                        break

                if not is_correct:
                    break

            if is_correct:
                # The current update is correct, extract the middle element
                middle_index = math.floor(len(update)/2)
                middle_element = int(update[middle_index])
                total += middle_element

        return total


p1 = Part_1()
p1.test(143)
p1.execute()
