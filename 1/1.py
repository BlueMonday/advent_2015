#!/usr/bin/env python3
import sys

TARGET_FLOOR = -1


def current_floor(directions):
    floor = 0

    for c in directions:
        if c == '(':
            floor += 1
        elif c == ')':
            floor -= 1

    return floor


def find_directions_index(directions, target_floor):
    """Returns the directions index which led to ``target_floor`."""
    floor = 0

    for i, c in enumerate(directions):
        if c == '(':
            floor += 1
        elif c == ')':
            floor -= 1

        if floor == target_floor:
            return i + 1

    return -1


if __name__ == '__main__':
    with open(sys.argv[1]) as f:
        directions_list = [line.strip() for line in f.readlines()]

    for directions in directions_list:
        print('directions: ', directions)
        print('part 1: ', current_floor(directions))
        print('part 2: ', find_directions_index(directions, TARGET_FLOOR))
