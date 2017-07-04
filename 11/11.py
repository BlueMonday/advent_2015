#!/usr/bin/env python
import string


CHARS_NOT_ALLOWED = ['i', 'o', 'l']


def increment(password):
    index = len(password) - 1
    password_list = list(password)

    while True:
        prev_char = password_list[index]
        next_char_index = (string.ascii_lowercase.index(password_list[index]) + 1) % len(string.ascii_lowercase)
        password_list[index] = string.ascii_lowercase[next_char_index]

        if prev_char != 'z':
            return ''.join(password_list)

        index -= 1

        if index < 0:
            raise Exception('Unable to increment password: {}'.format(password))


def valid(password):
    incrementing_straight = False
    previous_3_characters = ['\0', '\0', '\0']
    pairs = set()

    for char in password:
        if char in CHARS_NOT_ALLOWED:
            return False

        if char == previous_3_characters[len(previous_3_characters)-1]:
            if char not in pairs:
                pairs.add(char)

        for i in range(2):
            previous_3_characters[i] = previous_3_characters[i+1]

        previous_3_characters[len(previous_3_characters) - 1] = char

        for i in range(2):
            if previous_3_characters[i] == 'z' or previous_3_characters[i] == '\0':
                break

            next_char_in_straight = string.ascii_lowercase[string.ascii_lowercase.index(previous_3_characters[i]) + 1]
            if previous_3_characters[i+1] != next_char_in_straight:
                break
        else:
            incrementing_straight = True


    return incrementing_straight and len(pairs) >= 2


def part_1(previous_password):
    password = increment(previous_password)
    while not valid(password):
        print(password)
        password = increment(password)

    return password


if __name__ == '__main__':
    # print(part_1('hxbxwxba'))
    print(part_1('hxbxxyzz'))
