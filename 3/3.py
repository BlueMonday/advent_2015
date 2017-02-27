#!/usr/bin/env python3
import sys
import copy


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return 'Point({}, {})'.format(self.x, self.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return hash((self.x, self.y))


def part_one(directions):
    visited = set()

    position = Point(0, 0)
    visited.add(position)

    for direction in directions:
        if direction == '<':
            position.x -= 1
        elif direction == '>':
            position.x += 1
        elif direction == '^':
            position.y += 1
        elif direction == 'v':
            position.y -= 1

        visited.add(copy.copy(position))

    return len(visited)


def part_two(directions):
    visited = set()

    santa_position = Point(0, 0)
    robo_santa_position = Point(0, 0)
    visited.add(santa_position)

    for i, direction in enumerate(directions):
        santa_to_move = santa_position
        if i % 2 == 0:
            santa_to_move = robo_santa_position

        if direction == '<':
            santa_to_move.x -= 1
        elif direction == '>':
            santa_to_move.x += 1
        elif direction == '^':
            santa_to_move.y += 1
        elif direction == 'v':
            santa_to_move.y -= 1

        visited.add(copy.copy(santa_to_move))

    return len(visited)


if __name__ == '__main__':
    with open(sys.argv[1]) as f:
        directions_list = [line.strip() for line in f.readlines()]

    for directions in directions_list:
        print("part one: ", part_one(directions))
        print("part two: ", part_two(directions))
