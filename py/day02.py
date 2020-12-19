#!/usr/bin/env python3

def part1(lines):
    import re

    r = re.compile(r'(\d+)-(\d+) ([a-z]): ([a-z]+)')

    total = 0
    for line in lines:
        m = r.match(line)
        least, most, char, password = m.groups()
        least, most = int(least), int(most)

        if least <= password.count(char) <= most:
            total += 1

    return total


def part2(lines):
    import re

    r = re.compile(r'(\d+)-(\d+) ([a-z]): ([a-z]+)')

    total = 0
    for line in lines:
        m = r.match(line)
        least, most, char, password = m.groups()
        least, most = int(least), int(most)

        if (password[least-1], password[most-1],).count(char) == 1:
            total += 1

    return total


with open("../input/day02.input") as f:
    lines = [x.strip() for x in f.readlines()]
    print("part1:", part1(lines))
    print("part2:", part2(lines))
