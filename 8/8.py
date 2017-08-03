#!/usr/bin/env python
import sys


def part_one(strings):
    number_of_characters_of_code = 0
    number_of_characters_in_memory = 0

    for string in strings:
        number_of_characters_of_code += len(string)

        escaping = False
        hex_characters_left = 0
        for c in string:
            if c == '"':
                if escaping:
                    escaping = False
                else:
                    continue
            elif c == '\\':
                if escaping:
                    escaping = False
                else:
                    escaping = True
                    continue
            elif c == 'x' and escaping:
                hex_characters_left = 2
                continue
            elif hex_characters_left > 0:
                hex_characters_left -= 1

                if hex_characters_left > 0:
                    continue
                else:
                    escaping = False
            elif escaping:
                escaping = False

            number_of_characters_in_memory += 1

    return number_of_characters_of_code - number_of_characters_in_memory


def part_two(strings):
    number_of_characters_encoded = 0
    number_of_characters = 0

    for string in strings:
        number_of_characters += len(string)

        number_of_characters_encoded += 2
        for c in string:
            if c == '"' or c == '\\':
                number_of_characters_encoded += 2
            else:
                number_of_characters_encoded += 1


    return number_of_characters_encoded - number_of_characters


if __name__ == '__main__':
    with open(sys.argv[1]) as f:
        strings = [line.strip() for line in f.readlines()]

    print(part_one(strings))
    print(part_two(strings))
