#!/usr/bin/env python
import json
import sys


def sum_of_all_numbers(o):
    if isinstance(o, dict):
        sum_of_dict = 0
        for _, v in o.items():
            if v == 'red':
                return 0
            sum_of_dict += sum_of_all_numbers(v)

        return sum_of_dict
    elif isinstance(o, list):
        sum_of_list = 0
        for item in o:
            sum_of_list += sum_of_all_numbers(item)

        return sum_of_list
    elif isinstance(o, str):
        return 0
    elif isinstance(o, int):
        return o

    raise Exception("Unsupported type")


if __name__ == '__main__':
    with open(sys.argv[1]) as f:
        o = json.load(f)

    print(sum_of_all_numbers(o))
