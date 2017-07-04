#!/usr/bin/env python
import sys

class Register:
    def __init__(self, value=0):
        self.value = value

    def hlf(self):
        self.value //= 2

    def tpl(self):
        self.value *= 3

    def inc(self):
        self.value += 1

    def even(self):
        return self.value % 2 == 0

    def one(self):
        return self.value == 1

if __name__ == '__main__':
    registers = {
        'a': Register(value=1),
        'b': Register(),
    }

    with open(sys.argv[1]) as f:
        instructions = [line.strip() for line in f.readlines()]

    index = 0
    while True:
        if index < 0  or index >= len(instructions):
            break

        instruction = instructions[index]
        parts = instruction.split(' ')
        if parts[0] == 'hlf':
            registers[parts[1]].hlf()
        elif parts[0] == 'tpl':
            registers[parts[1]].tpl()
        elif parts[0] == 'inc':
            registers[parts[1]].inc()
        elif parts[0] == 'jmp':
            index += int(parts[1])
            continue
        elif parts[0] == 'jie':
            if registers[parts[1].strip(',')].even():
                index += int(parts[2])
                continue
        elif parts[0] == 'jio':
            if registers[parts[1].strip(',')].one():
                index += int(parts[2])
                continue

        index += 1

    print(registers['a'].value)
    print(registers['b'].value)
