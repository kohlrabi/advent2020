#!/usr/bin/env python3

def part1(lines, x_step=3, y_step=1):
    height = len(lines)
    width = len(lines[0])

    x, y = 0, 0

    trees = 0
    while y < height - y_step:
        x = (x + x_step) % width
        y = y + y_step
        if lines[y][x] == '#':
            trees += 1

    return trees


def part2(lines):
    import functools

    def mult(x, y): return x * y
    pairs = ((1, 1), (3, 1), (5, 1), (7, 1), (1, 2))
    trees = (part1(lines, *args) for args in pairs)

    return functools.reduce(mult, trees)


import os, sys

pwd = os.path.dirname(sys.argv[0])
with open(os.path.join(pwd, "../input/day03.input")) as f:
    lines = [x.strip() for x in f.readlines()]
    print("part1:", part1(lines))
    print("part2:", part2(lines))
