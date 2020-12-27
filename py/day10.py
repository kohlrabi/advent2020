#!/usr/bin/env python3


import sys
import os


def diff(x):
    return (n - p for n, p in zip(x[1:], x[:-1]))


def part1(lines):
    from collections import Counter
    adapters = sorted(int(x) for x in lines)
    adapters = [0] + adapters + [adapters[-1] + 3]
    diffs = diff(adapters)
    c = Counter(diffs)
    return c[1] * c[3]


def part2(lines):
    pass


pwd = os.path.dirname(sys.argv[0])
with open(os.path.join(pwd, "../input/day10.input")) as f:
    lines = [x.strip() for x in f.readlines()]
    print("part1:", part1(lines))
    print("part2:", part2(lines))
