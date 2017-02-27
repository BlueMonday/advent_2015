#!/usr/bin/env python3
import sys


def box_surface_area(l, w, h):
    smallest_side = min(l*w, w*h, h*l)
    return 2*l*w + 2*w*h + 2*h*l + smallest_side


def wrap_ribbon_length(l, w, h):
    return min(2*l + 2*w, 2*w + 2*h, 2*h + 2*l)


def bow_ribbon_length(l, w, h):
    return l*w*h


if __name__ == '__main__':
    with open(sys.argv[1]) as f:
        boxes = [line.strip() for line in f.readlines()]

    total_paper_sq_feet = 0
    total_ribbon_length = 0
    for box in boxes:
        length, width, height = map(int, box.split('x'))

        total_paper_sq_feet += box_surface_area(length, width, height)

        total_ribbon_length += (wrap_ribbon_length(length, width, height) +
                                bow_ribbon_length(length, width, height))

    print(total_paper_sq_feet)
    print(total_ribbon_length)
