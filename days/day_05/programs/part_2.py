from common import *
import math
import numpy as np


class Part_2(BaseClass):

    def __init__(self):
        super().__init__()

    def execute_internal(self, filepath):
        file_str = open_file(filepath)
        rule_str, update_str = file_str.split("\n\n")

        rule_list = [rule.split("|") for rule in rule_str.split("\n")]
        update_list = [update.split(",") for update in update_str.split("\n")]

        total = 0

        for update in update_list:
            if not is_sorted(update, rule_list):
                # Re-ordering the update
                new_update = []
                option_list = [*update]
                while len(new_update) < len(update):
                    for option in option_list:
                        check_list = [[option, x] for x in option_list if option is not x]

                        if np.all([x in rule_list for x in check_list]):
                            new_update.append(option)
                            option_list = [x for x in option_list if option is not x]
                            break

                update = new_update

                # The current update is now correct, extract the middle element
                middle_index = math.floor(len(update) / 2)
                middle_element = int(update[middle_index])
                total += middle_element

        return total


def is_sorted(update, rule_list):
    # Searching the i-th element for a broken rule
    # Not useful to test the first element
    for i in range(1, len(update)):
        for k in range(i):
            # i is the current element in the update list
            # k is one of the previous elements we are testing
            #
            # The correct rule would have the element in i AFTER the element in k
            # But if we find the rule with i BEFORE k, the update list is incorrect

            if [update[i], update[k]] in rule_list:
                return False

    return True


'''
def get_sorted_update(cur_update, option_list, rule_list):
    if len(option_list) == 0:
        return cur_update

    for option in option_list:
        is_valid = True
        for old_update in cur_update:
            if [option, old_update] in rule_list:
                is_valid = False
                break

        if is_valid:
            new_update = [*cur_update, option]
            new_option_list = [x for x in option_list if x is not option]
            result = get_sorted_update(new_update, new_option_list, rule_list)

            if len(result) > 0:
                return result

    return []
'''

p2 = Part_2()
p2.test(123)
p2.execute()
