from common import *
from itertools import combinations


class Part_1(BaseClass):

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
            perimeter = 4 * area

            for first, second in combinations(region, 2):
                first_r, first_c = first
                second_r, second_c = second
                delta_r, delta_c = abs(first_r-second_r), abs(first_c-second_c)

                if (delta_r == 0 and delta_c == 1) or (delta_r == 1 and delta_c == 0):
                    perimeter -= 2

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


p1 = Part_1()
p1.test(140, [("example_2.txt", 772), ("example_3.txt", 1930)])
p1.execute()
