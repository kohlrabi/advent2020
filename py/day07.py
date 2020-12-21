#!/usr/bin/env python3

class Bag:
    def __init__(self, name):
        self.name = name
        self.children = {}
        self.parents = []

    def add_child(self, bag, number):
        self.children[bag] = number
        bag.add_parent(self)

    def add_parent(self, bag):
        self.parents.append(bag)

    def visit_all_parents(self, fun):
        for p in self.parents:
            fun(p)
            p.visit_all_parents(fun)

    def __repr__(self):
        return f'Bag: {self.name}'

def collect_bags(lines):
    import re

    r_bag = re.compile(r'([a-z]+ [a-z]+) bags contain')
    r_children = re.compile(r'([0-9]+) ([a-z]+ [a-z]+) bag')

    bags = {}
    for line in lines:
        m = r_bag.match(line)
        name = m.group(1)
        if name not in bags:
            bags[name] = Bag(name)
        bag = bags[name]
        children = r_children.finditer(line)
        for child in children:
            number, name = child.groups(1)
            if not name in bags:
                bags[name] = Bag(name)
            bag_c = bags[name]
            bag.add_child(bag_c, int(number))
    return bags


def part1(lines):
    target = 'shiny gold'
    bags = collect_bags(lines)
    print(bags[target].children)

    class CountParents:
        def __init__(self):
            self.parents = set()

        def __call__(self, parent):
            self.parents.add(parent.name)

        def unique_parents(self):
            return len(self.parents)

    counter = CountParents()
    bags[target].visit_all_parents(counter)
    return counter.unique_parents()


def part2(lines):
    return


import os, sys

pwd = os.path.dirname(sys.argv[0])
with open(os.path.join(pwd, "../input/day07.input")) as f:
    lines = [x.strip() for x in f.readlines()]
    print("part1:", part1(lines))
    print("part2:", part2(lines))
