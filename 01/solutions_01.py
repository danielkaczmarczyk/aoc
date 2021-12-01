#!/usr/bin/python3

def parse_depths(depth_string):
    return int(depth_string.strip())


with open('./01/input') as file:
    depths = list(map(parse_depths, file.readlines()))


def solve_part_1():
    increases = 0
    for i in range(len(depths) - 1):
        if depths[i] < depths[i + 1]:
            increases += 1
    return increases


def get_window_sum(i, depths):
    return depths[i] + depths[i+1] + depths[i+2]


def solve_part_2():
    increases = 0
    for i in range(len(depths) - 3):
        if get_window_sum(i, depths) < get_window_sum(i + 1, depths):
            increases += 1
    return increases


print(solve_part_1(), solve_part_2())
