#!/usr/bin/env python3
import hashlib

PUZZLE_INPUT = b'iwrupvqb'

if __name__ == '__main__':
    number = 0

    while True:
        h = hashlib.md5(PUZZLE_INPUT + str(number).encode())
        if h.hexdigest().startswith('000000'):
            break
        number += 1

    print(number)
