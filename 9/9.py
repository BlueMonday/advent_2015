#!/usr/bin/env python3
import copy
import collections
import sys


def parse_distances(distance_strings):
    distances = collections.defaultdict(dict)

    for distance_string in distance_strings:
        start, _, end, _, distance_str = distance_string.split(' ')

        distance = int(distance_str)
        distances[start][end] = distance
        distances[end][start] = distance

    return distances


def find_shortest_distance(path, not_visited, distances):
    """Finds the shortest travel distance required to visit every city."""
    if len(not_visited) == 1:
        return distances[path[-1]][list(not_visited)[0]]

    shortest_distance = sys.maxsize
    for city in not_visited:
        current_path = copy.copy(path)
        current_path.append(city)

        updated_not_visited = copy.copy(not_visited)
        updated_not_visited.remove(city)

        distance = 0
        if path:
            distance = distances[path[-1]][city]

        distance += find_shortest_distance(
            current_path,
            updated_not_visited,
            distances
        )

        if distance < shortest_distance:
            shortest_distance = distance

    return shortest_distance


def find_longest_distance(path, not_visited, distances):
    """Finds the longest travel distance required to visit every city."""
    if len(not_visited) == 1:
        return distances[path[-1]][list(not_visited)[0]]

    longest_distance = -sys.maxsize
    for city in not_visited:
        current_path = copy.copy(path)
        current_path.append(city)

        updated_not_visited = copy.copy(not_visited)
        updated_not_visited.remove(city)

        distance = 0
        if path:
            distance = distances[path[-1]][city]

        distance += find_longest_distance(
            current_path,
            updated_not_visited,
            distances
        )

        if distance > longest_distance:
            longest_distance = distance

    return longest_distance


if __name__ == '__main__':
    with open(sys.argv[1]) as f:
        distance_strings = [line.strip() for line in f.readlines()]

    distances = parse_distances(distance_strings)

    print(find_shortest_distance([], set(distances.keys()), distances))
    print(find_longest_distance([], set(distances.keys()), distances))
