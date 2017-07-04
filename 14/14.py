#!/usr/bin/env python
import collections
import sys


NUMBER_OF_SECONDS = 2503


class Reindeer:
    def __init__(self, name, speed, duration, rest):
        self.name = name
        self.speed = speed
        self.duration = duration
        self.rest = rest

        self.distance_traveled = 0
        self.resting = False
        self.time = 0
        self.points = 0

    def tick(self):
        if self.resting:
            self.time += 1
            if self.time == self.rest:
                self.resting = False
                self.time = 0
        else:
            self.distance_traveled += reindeer.speed
            self.time += 1
            if self.time == self.duration:
                self.resting = True
                self.time = 0


def parse_descriptions(descriptions):
    reindeers = []
    for description in descriptions:
        parts = description.split(' ')
        reindeers.append(
            Reindeer(
                name=parts[0],
                speed=int(parts[3]),
                duration=int(parts[6]),
                rest=int(parts[13]),
            )
        )

    return reindeers


if __name__ == '__main__':
    with open(sys.argv[1]) as f:
        descriptions = f.readlines()

    reindeers = parse_descriptions(descriptions)

    seconds = 0
    while seconds != NUMBER_OF_SECONDS:
        for reindeer in reindeers:
            reindeer.tick()

        seconds += 1

        lead_reindeers = []
        for reindeer in reindeers:
            if len(lead_reindeers) == 0:
                lead_reindeers.append(reindeer)
            elif reindeer.distance_traveled == lead_reindeers[0].distance_traveled:
                lead_reindeers.append(reindeer)
            elif reindeer.distance_traveled > lead_reindeers[0].distance_traveled:
                lead_reindeers = [reindeer]

        for lead_reindeer in lead_reindeers:
            lead_reindeer.points += 1

    max_distance = 0
    max_points = 0
    for reindeer in reindeers:
        if reindeer.distance_traveled > max_distance:
            max_distance = reindeer.distance_traveled

        if reindeer.points > max_points:
            max_points = reindeer.points


    print(max_distance)
    print(max_points)
