#!/usr/bin/env python
import sys


NUMBER_OF_STEPS = 100


def print_grid(grid):
    for row in grid:
        print(''.join(row))

    print()


def count_lighs(grid):
    number_of_lights = 0
    for row in grid:
        for c in row:
            if c == '#':
                number_of_lights += 1

    return number_of_lights


if __name__ == '__main__':
    with open(sys.argv[1]) as f:
        grid = [[c for c in line.strip()] for line in f.readlines()]

    # Turn on the corners.
    grid[0][0] = '#'
    grid[0][len(grid[0])-1] = '#'
    grid[len(grid)-1][0] = '#'
    grid[len(grid)-1][len(grid[0])-1] = '#'

    for _ in range(NUMBER_OF_STEPS):
        new_grid = []

        for y, row in enumerate(grid):
            new_grid.append([])

            for x, c in enumerate(row):
                number_of_neighbors_turned_on = 0

                if y > 0:
                    if grid[y-1][x] == '#':
                        number_of_neighbors_turned_on += 1

                    if x > 0 and grid[y-1][x-1] == '#':
                        number_of_neighbors_turned_on += 1

                    if x < len(row) - 1 and grid[y-1][x+1] == '#':
                        number_of_neighbors_turned_on += 1

                if y < len(grid) - 1 :
                    if grid[y+1][x] == '#':
                        number_of_neighbors_turned_on += 1

                    if x > 0 and grid[y+1][x-1] == '#':
                        number_of_neighbors_turned_on += 1

                    if x < len(row) - 1 and grid[y+1][x+1] == '#':
                        number_of_neighbors_turned_on += 1

                if x > 0 and grid[y][x-1] == '#':
                    number_of_neighbors_turned_on += 1

                if x < len(row) - 1 and grid[y][x+1] == '#':
                    number_of_neighbors_turned_on += 1

                if (y == 0 and x == 0) or (y == 0 and x == len(row) - 1) or (y == len(grid) - 1  and x == 0) or (y == len(grid) - 1 and x == len(row) - 1):
                    new_grid[y].append('#')
                elif grid[y][x] == '#' and (number_of_neighbors_turned_on != 2 and number_of_neighbors_turned_on != 3):
                    new_grid[y].append('.')
                elif grid[y][x] == '.' and number_of_neighbors_turned_on == 3:
                    new_grid[y].append('#')
                else:
                    new_grid[y].append(grid[y][x])

        grid = new_grid
        print_grid(grid)

    print(count_lighs(grid))
