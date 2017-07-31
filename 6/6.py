#!/usr/bin/env python
import sys


def parse_x_y(coordinate):
    return map(int, coordinate.split(','))


def count_lights(lights):
    count = 0
    for row in lights:
        for light in row:
            if light:
                count += 1

    return count

def count_brightness(lights):
    brightness = 0
    for row in lights:
        for light in row:
            brightness += light

    return brightness


def part_1(instructions):
    lights = [[False for i in range(1000)] for j in range(1000)]

    for instruction in instructions:
        parts = instruction.split(' ')

        if parts[0] == 'turn':
            state = parts[1]
            start_x, start_y = parse_x_y(parts[2])
            end_x, end_y = parse_x_y(parts[4])

            if state == 'on':
                for y in range(start_y, end_y + 1):
                    for x in range(start_x, end_x + 1):
                        lights[y][x] = True
            elif state == 'off':
                for y in range(start_y, end_y + 1):
                    for x in range(start_x, end_x + 1):
                        lights[y][x] = False
        elif parts[0] == 'toggle':
            start_x, start_y = parse_x_y(parts[1])
            end_x, end_y = parse_x_y(parts[3])

            for y in range(start_y, end_y + 1):
                for x in range(start_x, end_x + 1):
                    lights[y][x] = not lights[y][x]

    print(count_lights(lights))


def part_2(instructions):
    lights = [[0 for i in range(1000)] for j in range(1000)]

    for instruction in instructions:
        parts = instruction.split(' ')

        if parts[0] == 'turn':
            state = parts[1]
            start_x, start_y = parse_x_y(parts[2])
            end_x, end_y = parse_x_y(parts[4])

            if state == 'on':
                for y in range(start_y, end_y + 1):
                    for x in range(start_x, end_x + 1):
                        lights[y][x] += 1
            elif state == 'off':
                for y in range(start_y, end_y + 1):
                    for x in range(start_x, end_x + 1):
                        lights[y][x] = max(0, lights[y][x] - 1)
        elif parts[0] == 'toggle':
            start_x, start_y = parse_x_y(parts[1])
            end_x, end_y = parse_x_y(parts[3])

            for y in range(start_y, end_y + 1):
                for x in range(start_x, end_x + 1):
                    lights[y][x] += 2

    print(count_brightness(lights))

if __name__ == '__main__':
    with open(sys.argv[1]) as f:
        instructions = [line.strip() for line in f.readlines()]

    # part_1(instructions)
    part_2(instructions)
