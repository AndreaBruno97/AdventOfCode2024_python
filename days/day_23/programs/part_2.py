from common import *


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

        sub_lan_set = set()

        for cur_node, cur_neighbor_list in lan_map.items():
            for cur_neigh in cur_neighbor_list:
                for neigh_neighbor in lan_map[cur_neigh]:
                    if neigh_neighbor in cur_neighbor_list and "t" in cur_node[0] + cur_neigh[0] + neigh_neighbor[0]:
                        sub_lan_set.add(frozenset([cur_node, cur_neigh, neigh_neighbor]))

        fully_connected_sub_lan_set = set()

        for triangle in sub_lan_set:
            fully_connected_sub_lan = set(triangle)
            for new_triangle in sub_lan_set:
                is_fully_connected = True
                for new_node in new_triangle:
                    if new_node in fully_connected_sub_lan:
                        continue
                    for cur_node in fully_connected_sub_lan:
                        if cur_node not in lan_map[new_node]:
                            is_fully_connected = False
                            break
                if is_fully_connected:
                    fully_connected_sub_lan = fully_connected_sub_lan.union(new_triangle)

            fully_connected_sub_lan_set.add(frozenset(fully_connected_sub_lan))

        fully_connected_sub_lan_list = list(fully_connected_sub_lan_set)
        fully_connected_sub_lan_list.sort(key=lambda x: -len(x))

        biggest_fully_connected_subset = list(fully_connected_sub_lan_list[0])
        biggest_fully_connected_subset.sort()

        return ",".join(biggest_fully_connected_subset)


p2 = Part_2()
p2.test("co,de,ka,ta")
p2.execute()
