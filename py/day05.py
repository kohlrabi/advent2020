#!/usr/bin/env python3

def take_half(x, c):
    try:
        l = len(x) // 2
        if c[0]:
            return take_half(x[:l], c[1:])
        else:
            return take_half(x[l:], c[1:])
    except IndexError:
        return x[0]


def part1(lines):
    import math
    nrows = 128
    ncols = 8

    rows = range(0, nrows)
    columns = range(0, ncols)

    max_seat = 0
    for line in lines:
        conds = []
        conds_rows = []
        check_char = 'F'
        for i, c in enumerate(line):
            conds.append(c == check_char)
            if i == int(math.log2(nrows)) - 1:
                conds_rows = conds[:]
                conds.clear()
                check_char = 'L'

        row = take_half(rows, conds_rows)
        column = take_half(columns, conds)
        seat = row * 8 + column
        max_seat = max(max_seat, seat)

    return max_seat


def part2(lines):
    import math
    nrows = 128
    ncols = 8

    rows = range(0, nrows)
    columns = range(0, ncols)

    max_seat = 0
    min_seat = 128 * 8
    seats = []
    for line in lines:
        conds = []
        conds_rows = []
        check_char = 'F'
        for i, c in enumerate(line):
            conds.append(c == check_char)
            if i == int(math.log2(nrows)) - 1:
                conds_rows = conds[:]
                conds.clear()
                check_char = 'L'

        row = take_half(rows, conds_rows)
        column = take_half(columns, conds)
        seat = row * 8 + column
        max_seat = max(max_seat, seat)
        min_seat = min(min_seat, seat)
        seats.append(seat)

    seats = set(seats)
    my_seat = set(range(min_seat, max_seat+1))

    return list(my_seat ^ seats)[0]


import os, sys

pwd = os.path.dirname(sys.argv[0])
with open(os.path.join(pwd, "../input/day05.input")) as f:
    lines = [x.strip() for x in f.readlines()]
    print("part1:", part1(lines))
    print("part2:", part2(lines))
