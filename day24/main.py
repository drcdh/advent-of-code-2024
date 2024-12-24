import itertools
import sys

import input
#import test as input

inputs = {}
signals = {}
rewires = {}

def evaluate(w):
    w = rewires.get(w, w)
    if w in inputs:
        return inputs[w]
    l, op, r = signals[w]
    if op == "AND":
        return evaluate(l) & evaluate(r)
    elif op == "OR":
        return evaluate(l) | evaluate(r)
    elif op == "XOR":
        return evaluate(l) ^ evaluate(r)

def parse_operation(op):
    l, op, r = op.split()
    return l, op, r


for init in input.initial.split("\n"):
    k, v = init.split(": ")
    inputs[k] = int(v)

for wire in input.wires.split("\n"):
    op, target = wire.split(" -> ")
    signals[target] = parse_operation(op)

def get_binary(c, w=signals):
    bin_str = ""
    for s in sorted(w.keys()):
        if s.startswith(c):
            v = evaluate(s)
            bin_str = str(v) + bin_str
    return int(bin_str, 2)

print("Part 1:", get_binary("z"))


for w1, w2 in input.swaps:
    rewires[w1], rewires[w2] = w2, w1

x = get_binary("x", inputs)
y = get_binary("y", inputs)
z = get_binary("z")
assert z == input.expected_z(x, y)

swaps = ()
for s in input.swaps:
    swaps = swaps + s
swaps = sorted(swaps)
print("Part 2:", ",".join(swaps))

