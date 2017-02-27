#!/usr/bin/env python

PART_1_ROUNDS = 40
PART_2_ROUNDS = 50

INPUT = '1321131112'


def look_and_say(initial_sequence, rounds):
    sequence = initial_sequence

    for _ in range(rounds):
        new_sequence = ''
        digit_count = 0
        current_digit = sequence[0]

        for c in sequence:
            if c != current_digit:
                new_sequence += '{}{}'.format(digit_count, current_digit)

                current_digit = c
                digit_count = 1
            else:
                digit_count += 1

        sequence = new_sequence + '{}{}'.format(digit_count, current_digit)

    return sequence


if __name__ == '__main__':
    print(len(look_and_say(INPUT, PART_1_ROUNDS)))
    print(len(look_and_say(INPUT, PART_2_ROUNDS)))
