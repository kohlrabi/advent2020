#!/usr/bin/env python3

class HandheldCode:

    def __init__(self, code, acc=0):
        self.code = code
        self.maxpos = len(self.code)
        self.acc = acc
        self.pos = 0

    def op_at(self, i):
        return self.code[i][0]

    def change_op(self, i, op):
        self.code[i] = (op, self.code[i][1])

    def reset(self):
        self.acc = 0
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
            if self.pos == self.maxpos:
                break
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

    def copy(self):
        return HandheldCode(self.code.copy())

class StopDouble:
    def __init__(self):
        self.visited = set()
        self.broken = False

    def add_visit(self, handheld):
        p = handheld.pos
        if p in self.visited:
            self.broken = True
            return True
        self.visited.add(p)

    def __call__(self, handheld):
        return self.add_visit(handheld)

    def reset(self):
        self.visited = set()
        self.broken = False


def part1(lines):
    handheld = HandheldCode.parse_code(lines)
    handheld.run(StopDouble())
    return handheld.acc

def part2(lines):
    handheld = HandheldCode.parse_code(lines)
    orig = handheld.copy()
    sd = StopDouble()
    for i in range(len(handheld.code)):
        if handheld.op_at(i) == 'nop':
            handheld.change_op(i, 'jmp')
        elif handheld.op_at(i) == 'jmp':
            handheld.change_op(i, 'nop')
        sd.reset()  
        handheld.run(sd)
        if sd.broken == False:
            return(handheld.acc)
        handheld = orig.copy()

import os, sys

pwd = os.path.dirname(sys.argv[0])
with open(os.path.join(pwd, "../input/day08.input")) as f:
    lines = [x.strip() for x in f.readlines()]
    print("part1:", part1(lines))
    print("part2:", part2(lines))
