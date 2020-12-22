#!/usr/bin/env python3

class HandheldCode:


    def __init__(self, code, acc=0):
        self.code = code
        self.acc = acc
        self.pos = 0

    def op_acc(self, val):
        self.acc += val
        self.pos += 1
    
    def op_jmp(self, val):
        self.pos += val

    def op_nop(self, val):
        self.pos += 1

    def run(self, fun=None):
        while True:
            instr, val = self.code[self.pos]
            HandheldCode.ops[instr](self, val)
            if fun:
                ret = fun(self)
                if ret:
                    break

    @classmethod
    def parse_code(cls, lines):
        import re

        r = re.compile(r'([a-z]{3}) ([+-][0-9]+)')

        code = []
        for line in lines:
            m = r.match(line)
            if m:
                code.append((m.group(1), int(m.group(2))))

        return cls(code)

    ops = {
        'acc': op_acc,
        'jmp': op_jmp,
        'nop': op_nop,
    }


def part1(lines):
    
    class StopDouble:
        def __init__(self):
            self.visited = set()

        def add_visit(self, handheld):
            p = handheld.pos
            if p in self.visited:
                return True
            self.visited.add(p)

        def __call__(self, handheld):
            return self.add_visit(handheld)

    handheld = HandheldCode.parse_code(lines)
    handheld.run(StopDouble())
    return handheld.acc

def part2(lines):
    return None


import os, sys

pwd = os.path.dirname(sys.argv[0])
with open(os.path.join(pwd, "../input/day08.input")) as f:
    lines = [x.strip() for x in f.readlines()]
    print("part1:", part1(lines))
    print("part2:", part2(lines))
