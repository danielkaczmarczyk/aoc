#!/usr/bin/python3

floor = 0
char_index = 0


def move_elevator(char):
    global floor
    if char == "(":
        floor += 1
    elif char == ")":
        floor -= 1


with open("./2015/01/input", encoding="utf-8") as file:
    while char := file.read(1):
        move_elevator(char)
        char_index += 1
        if floor == -1:
            print('first basement index:')
            print(char_index)
            break

print(floor)
