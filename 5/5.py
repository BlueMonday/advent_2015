#!/usr/bin/env python3
import re
import sys

VOWELS = frozenset(['a', 'e', 'i', 'o', 'u'])
NICE_STRING_MIN_VOWELS = 3

INVALID_SEQUENCES = frozenset(['ab', 'cd', 'pq', 'xy'])


def nice_string_part_1(string):
    """Determines if ``string`` is a nice string according to the first spec.

    Nice strings contain at least ``NICE_STRING_MIN_VOWELS`` vowels, one
    character that appears twice in a row, and do not contain any of the
    invalid sequences.
    """
    vowel_count = 0
    duplicate_sequential_character = False

    for i in range(len(string)):
        if string[i] in VOWELS:
            vowel_count += 1

        if i < len(string) - 1:
            if string[i] == string[i+1]:
                duplicate_sequential_character = True

            if string[i:i+2] in INVALID_SEQUENCES:
                return False

    return (duplicate_sequential_character and
            vowel_count >= NICE_STRING_MIN_VOWELS)


def nice_string_part_2(string):
    """Determines if ``string`` is a nice string according to the second spec.

    Nice strings contain two letters that appears at least twice in the string
    without overlapping and at least one letter which repeats with exactly one
    letter between them.
    """
    return (re.search(r'(\w\w).*\1', string) and
            re.search(r'(\w)(?!\1)\w\1', string))


if __name__ == '__main__':
    with open(sys.argv[1]) as f:
        strings = [line.strip() for line in f.readlines()]

    nice_strings_part_1 = 0
    nice_strings_part_2 = 0
    for string in strings:
        print(string)
        if nice_string_part_1(string):
            nice_strings_part_1 += 1

        if nice_string_part_2(string):
            nice_strings_part_2 += 1

    print(nice_strings_part_1)
    print(nice_strings_part_2)
