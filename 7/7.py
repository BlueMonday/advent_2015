#!/usr/bin/env python
import functools
import sys


wires = {}


def parse_source(source):
    if source.isdigit():
        return int(source)

    return source


@functools.lru_cache()
def get_source_value(source):
    if isinstance(source, int):
        return source

    return wires[source].compute()


class Not:
    def __init__(self, source):
        self.source = source

    def compute(self):
        source_value = get_source_value(self.source)
        return ~source_value & (2 ** 16 - 1)


class Arrow:
    def __init__(self, source):
        self.source = source

    def compute(self):
        return get_source_value(self.source)


class And:
    def __init__(self, source_a, source_b):
        self.source_a = source_a
        self.source_b = source_b

    def compute(self):
        source_value_a = get_source_value(self.source_a)
        source_value_b = get_source_value(self.source_b)

        return source_value_a & source_value_b


class Or:
    def __init__(self, source_a, source_b):
        self.source_a = source_a
        self.source_b = source_b

    def compute(self):
        source_value_a = get_source_value(self.source_a)
        source_value_b = get_source_value(self.source_b)

        return source_value_a | source_value_b


class LShift:
    def __init__(self, source, number_of_places):
        self.source = source
        self.number_of_places = number_of_places

    def compute(self):
        source_value = get_source_value(self.source)
        return (source_value << self.number_of_places) & (2 ** 16 - 1)


class RShift:
    def __init__(self, source, number_of_places):
        self.source = source
        self.number_of_places = number_of_places

    def compute(self):
        source_value = get_source_value(self.source)
        return (source_value >> self.number_of_places) & (2 ** 16 - 1)


if __name__ == '__main__':
    with open(sys.argv[1]) as f:
        instructions = [line.strip() for line in f.readlines()]

    for instruction in instructions:
        parts = instruction.split(' ')

        if parts[0] == 'NOT':
            source = parse_source(parts[1])
            destination = parts[3]

            wires[destination] = Not(source)
        elif parts[1] == '->':
            source = parse_source(parts[0])
            destination = parts[2]

            wires[destination] = Arrow(source)
        elif parts[1] == 'AND':
            source_a = parse_source(parts[0])
            source_b = parse_source(parts[2])
            destination = parts[4]

            wires[destination] = And(source_a, source_b)
        elif parts[1] == 'OR':
            source_a = parse_source(parts[0])
            source_b = parse_source(parts[2])
            destination = parts[4]

            wires[destination] = Or(source_a, source_b)
        elif parts[1] == 'LSHIFT':
            source = parse_source(parts[0])
            number_of_places = int(parts[2])
            destination = parts[4]

            wires[destination] = LShift(source, number_of_places)
        elif parts[1] == 'RSHIFT':
            source = parse_source(parts[0])
            number_of_places = int(parts[2])
            destination = parts[4]

            wires[destination] = RShift(source, number_of_places)

    wire_a_signal = wires['a'].compute()
    print('part one', wire_a_signal)

    get_source_value.cache_clear()
    wires['b'] = Arrow(wire_a_signal)
    print('part two', wires['a'].compute())
