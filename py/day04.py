#!/usr/bin/env python3

def valid(d):
    required = set(['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'])
    optional = set(['cid'])
    s = set(d.keys())
    return s & required == required and s & optional in (optional, set())


def part1(lines):
    num_valid = 0

    keys = {}
    for line in lines:
        if not line:
            num_valid += valid(keys)
            keys = {}
        else:
            tok = line.split()
            for t in tok:
                k, v = t.split(':')
                keys.update({k: v})

    return num_valid


def part2(lines):
    pass


with open("../input/day04.input") as f:
    lines = [x.strip() for x in f.readlines()]
    print("part1:", part1(lines))
    print("part2:", part2(lines))
