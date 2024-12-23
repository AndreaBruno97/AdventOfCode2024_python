from common import *
import itertools


class Part_2(BaseClass):

    def __init__(self):
        super().__init__()

    def execute_internal(self, filepath):
        edge_list = [x.split("-") for x in open_file_lines(filepath)]

        lan_map = dict()
        node_set = set()

        for left, right in edge_list:
            if left not in lan_map:
                lan_map[left] = []
            if right not in lan_map:
                lan_map[right] = []

            lan_map[left].append(right)
            lan_map[right].append(left)

            node_set.add(left)
            node_set.add(right)

        biggest_connected_subset = []

        for cur_node in node_set:
            cur_neigh_list = lan_map[cur_node]
            found = False
            for i in range(len(cur_neigh_list), 2, -1):
                for cur_combination in itertools.combinations(cur_neigh_list, i):
                    cur_combination = [*cur_combination, cur_node]
                    is_fully_connected = True
                    for first_node, second_node in itertools.combinations(cur_combination, 2):
                        if first_node not in lan_map[second_node]:
                            is_fully_connected = False
                            break

                    if is_fully_connected:
                        if len(biggest_connected_subset) < len(cur_combination):
                            biggest_connected_subset = cur_combination
                        found = True
                        break
                if found:
                    break

        biggest_connected_subset = list(biggest_connected_subset)
        biggest_connected_subset.sort()

        return ",".join(biggest_connected_subset)


p2 = Part_2()
p2.test("co,de,ka,ta")
p2.execute()
