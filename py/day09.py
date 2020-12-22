#!/usr/bin/env python3


import functools
import itertools

@functools.lru_cache(None)
def cached_sum(*args):
    return sum(*args)

def part1(lines):
    preamble = 25
    numbers = [int(x) for x in lines]
    for i, n in enumerate(numbers[preamble:]):
        for c in itertools.combinations(numbers[i:i+preamble], 2):
            if cached_sum(c) == n:
                break
        else:
            return n


def part2(lines):
    numbers = [int(x) for x in lines]
    target = part1(lines)
    for i in range(len(numbers)):
        for j in range(i+2, len(numbers)):
            s = cached_sum(tuple(numbers[i:j]))
            if s == target:
                return max(numbers[i:j]) + min(numbers[i:j])
            if s > target:
                break
            

import os, sys

pwd = os.path.dirname(sys.argv[0])
with open(os.path.join(pwd, "../input/day09.input")) as f:
    lines = [x.strip() for x in f.readlines()]
    print("part1:", part1(lines))
    print("part2:", part2(lines))
