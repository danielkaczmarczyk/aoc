#!/usr/bin/python3

def parse_directions(command):
    direction, magnitude = command.split()
    return direction, int(magnitude)


with open('./02/input') as file:
    directions = list(map(parse_directions, file.readlines()))


def solve_part_1():
    depth, horizontal_position = 0
    for direction in directions:
        if direction[0] == 'forward':
            horizontal_position += direction[1]
        elif direction[0] == 'up':
            depth -= direction[1]
        elif direction[0] == 'down':
            depth += direction[1]
    return depth * horizontal_position


def solve_part_2():
    aim, depth, horizontal_position = 0
    for direction in directions:
        if direction[0] == 'forward':
            horizontal_position += direction[1]
            depth += aim * direction[1]
        elif direction[0] == 'up':
            aim -= direction[1]
        elif direction[0] == 'down':
            aim += direction[1]
    return depth * horizontal_position


print(solve_part_1(), solve_part_2())
