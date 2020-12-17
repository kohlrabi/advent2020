#!/usr/bin/env python3

def part1(lines):
    ints = [int(x) for x in lines]
    for i, first in enumerate(ints):
        for _, second in enumerate(ints[i+1:]):
            if first + second == 2020:
                return first * second


def part2(lines):
    ints = [int(x) for x in lines]
    for i, first in enumerate(ints):
        for j, second in enumerate(ints[i+1:]):
            for _, third in enumerate(ints[j+1:]):
                if first + second + third == 2020:
                    return first * second * third


with open("../input/day01.input") as f:
    lines = [x for x in f.readlines()]
    print("part1:", part1(lines))
    print("part2:", part2(lines))
