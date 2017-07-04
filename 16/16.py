#!/usr/bin/env python
import sys

class Sue:
    def __init__(self, number, children=None, cats=None, samoyeds=None,
                 pomeranians=None, akitas=None, vizslas=None, goldfish=None, trees=None,
                 cars=None, perfumes=None):
        self.number = number
        self.children = children
        self.cats = cats
        self.samoyeds = samoyeds
        self.pomeranians = pomeranians
        self.akitas = akitas
        self.vizslas = vizslas
        self.goldfish = goldfish
        self.trees = trees
        self.cars = cars
        self.perfumes = perfumes

    def possible(self, other_sue):
        return ((other_sue.children is None or self.children == other_sue.children) and
                (other_sue.cats is None or self.cats < other_sue.cats) and
                (other_sue.samoyeds is None or self.samoyeds == other_sue.samoyeds) and
                (other_sue.pomeranians is None or self.pomeranians > other_sue.pomeranians) and
                (other_sue.akitas is None or self.akitas == other_sue.akitas) and
                (other_sue.vizslas is None or self.vizslas == other_sue.vizslas) and
                (other_sue.goldfish is None or self.goldfish > other_sue.goldfish) and
                (other_sue.trees is None or self.trees < other_sue.trees) and
                (other_sue.cars is None or self.cars == other_sue.cars) and
                (other_sue.perfumes is None or self.perfumes == other_sue.perfumes))


def parse_descriptions(descriptions):
    sues = []
    for description in descriptions:
        parts = description.split(' ')
        number = parts[1].strip(':')

        kwargs  = {}
        for i in range(len(parts[2:]) // 2):
            key = parts[i*2 + 2].strip(':')
            kwargs[key] = int(parts[(i*2 + 2) + 1].strip(',\n'))

        sues.append(
            Sue(
                number=number,
                **kwargs
            )
        )

    return sues


if __name__ == '__main__':
    with open(sys.argv[1]) as f:
        descriptions = f.readlines()

    target_sue =  Sue(
        number=0,
        children=3,
        cats=7,
        samoyeds=2,
        pomeranians=3,
        akitas=0,
        vizslas=0,
        goldfish=5,
        trees=3,
        cars=2,
        perfumes=1,
    )
    sues = parse_descriptions(descriptions)

    for sue in sues:
        if target_sue.possible(sue):
            print('possible sue: ', sue.number)
