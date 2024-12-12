from common import *
from itertools import combinations


class Part_2(BaseClass):

    def __init__(self):
        super().__init__()

    def execute_internal(self, filepath):
        garden = open_file_str_matrix_guarded(filepath, "-")
        rows = len(garden)
        cols = len(garden[0])

        plot_set = set()
        for r in range(1, rows-1):
            for c in range(1, cols-1):
                plot_set.add((r, c))

        region_list = []
        while len(plot_set) > 0:
            cur_plot = plot_set.pop()
            region = find_region(cur_plot, garden, plot_set)
            region_list.append(region)

        total = 0
        for region in region_list:
            area = len(region)
            perimeter = 0

            rows_list = [[x for x in region if x[0] == r] for r in range(1, rows-1)]
            cols_list = [[x for x in region if x[1] == c] for c in range(1, cols-1)]

            for row in rows_list:
                row.sort()

                # Check up and down
                for delta in [-1, 1]:
                    last_c = -1
                    for cur_r, cur_c in row:
                        if garden[cur_r, cur_c] != garden[cur_r+delta, cur_c]:
                            if cur_c > last_c + 1:
                                perimeter += 1
                            last_c = cur_c

            for col in cols_list:
                col.sort()

                # Check left and right
                for delta in [-1, 1]:
                    last_r = -1
                    for cur_r, cur_c in col:
                        if garden[cur_r, cur_c] != garden[cur_r, cur_c+delta]:
                            if cur_r > last_r + 1:
                                perimeter += 1
                            last_r = cur_r

            total += area * perimeter

        return total


def find_region(cur_plot, garden, plot_set):
    region = {cur_plot}
    plot_set.discard(cur_plot)
    cur_r, cur_c = cur_plot
    cur_plot_val = garden[cur_r, cur_c]

    for delta_r, delta_c in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        new_r, new_c = cur_r+delta_r, cur_c+delta_c
        new_plot = (new_r, new_c)
        new_plot_val = garden[new_r, new_c]

        if new_plot_val == cur_plot_val and new_plot in plot_set:
            new_region = find_region(new_plot, garden, plot_set)
            region = region.union(new_region)

    return region


p2 = Part_2()
p2.test(80, [("example_2.txt", 436), ("example_3.txt", 1206), ("example_4.txt", 236), ("example_5.txt", 368)])
p2.execute()
