import itertools

from common import *


class Part_1(BaseClass):

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

        sub_lan_set = set()

        for cur_node, cur_neighbor_list in lan_map.items():
            for cur_neigh in cur_neighbor_list:
                for neigh_neighbor in lan_map[cur_neigh]:
                    if neigh_neighbor in cur_neighbor_list and "t" in cur_node[0] + cur_neigh[0] + neigh_neighbor[0]:
                        sub_lan_set.add(frozenset([cur_node, cur_neigh, neigh_neighbor]))

        return len(sub_lan_set)


p1 = Part_1()
p1.test(7)
p1.execute()
