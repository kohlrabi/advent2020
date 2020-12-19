#!/usr/bin/env python3

class Passport:
    def __init__(self, byr, iyr, eyr, hgt, hcl, ecl, pid, cid=None):
        self.byr = byr
        self.iyr = iyr
        self.eyr = eyr
        self.hgt = hgt
        self.hcl = hcl
        self.ecl = ecl
        self.pid = pid
        self.cid = cid

    @classmethod
    def valid(cls, d):
        import re

        try:
            p = cls(**d)
            return True
        except:
            return False

    @classmethod
    def valid_full(cls, d):
        import re

        try:
            p = cls(**d)
            if not(1920 <= int(p.byr) <= 2002):
                return False
            if not(2010 <= int(p.iyr) <= 2020):
                return False
            if not (2020 <= int(p.eyr) <= 2030):
                return False

            m = re.match(r'^([0-9]+)([a-z]{2})$', p.hgt)
            if m:
                if m.group(2) == 'cm':
                    if not(150 <= int(m.group(1)) <= 193):
                        return False
                elif m.group(2) == 'in':
                    if not(59 <= int(m.group(1)) <= 76):
                        return False
                else:
                    return False
            else:
                return False

            m = re.match(r'^#[0-9a-f]{6}$', p.hcl)

            if not m:
                return False
            if p.ecl not in ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'):
                return False
            m = re.match(r'^[0-9]{9}$', p.pid)
            if not m:
                return False
            return True
        except:
            return False


def part1(lines):
    num_valid = 0

    keys = {}
    for line in lines:
        if not line:
            num_valid += Passport.valid(keys)
            keys = {}
        else:
            tok = line.split()
            for t in tok:
                k, v = t.split(':')
                keys.update({k: v})

    return num_valid


def part2(lines):
    num_valid = 0

    keys = {}
    for line in lines:
        if not line:
            num_valid += Passport.valid_full(keys)
            keys = {}
        else:
            tok = line.split()
            for t in tok:
                k, v = t.split(':')
                keys.update({k: v})

    return num_valid


with open("../input/day04.input") as f:
    lines = [x.strip() for x in f.readlines()]
    print("part1:", part1(lines))
    print("part2:", part2(lines))
