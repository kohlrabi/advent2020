#!/usr/bin/env python3

def part1(lines):
    group = set()
    answers = 0
    for line in lines:
        if line:
            group |= set(line)
        else:
            answers += len(group)
            group = set()

    return answers


def part2(lines):
    group = set(chr(x) for x in range(ord('a'), ord('z') + 1))
    answers = 0
    for line in lines:
        if line:
            group &= set(line)
        else:
            answers += len(group)
            group = set(chr(x) for x in range(ord('a'), ord('z') + 1))

    return answers


import os, sys

pwd = os.path.dirname(sys.argv[0])
with open(os.path.join(pwd, "../input/day06.input")) as f:
    lines = [x.strip() for x in f.readlines()]
    print("part1:", part1(lines))
    print("part2:", part2(lines))
