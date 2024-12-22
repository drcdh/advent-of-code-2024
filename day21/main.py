import functools
import sys
from pprint import pprint

from graphs import directional_cmds, numeric_cmds

filepath = sys.argv[1]
NUM_DIR_ROBOTS = int(sys.argv[2])

input = [l.strip() for l in open(filepath, "r").readlines()]

def append_many_to_many(l1, l2):
    if not l1:
        yield from l2
    else:
        for l1_ in l1:
            for l2_ in l2:
                yield l1_+l2_

def cmds_from_prev_robot(to_press: str, numeric=False):
    paths = numeric_cmds if numeric else directional_cmds
    path = "A" + to_press
    possibilities = None
    #print(f"{numeric=} {path=}")
    for b1, b2 in zip(path[:-1], path[1:]):
        possibilities = append_many_to_many(possibilities, paths[b1][b2])
    return tuple(possibilities)

@functools.cache
def length_of_command(cmds, layer, numeric=False):
    if layer == 0:
        return len(cmds)
    l = 0
    for _cmds in cmds.split("A")[:-1]:
        _cmds = _cmds+"A"
        next_cmds = min(cmds_from_prev_robot(_cmds, numeric=numeric), key=lambda _c: length_of_command(_c, layer-1))
        l += length_of_command(next_cmds, layer-1, numeric=False)
    return l

result = 0
for cmds in input:
    n = int(cmds[:-1])
    l = length_of_command(cmds, layer=NUM_DIR_ROBOTS+1, numeric=True)
    complexity = n*l
    result += complexity
print("One directional keypad that you are using.")
print(NUM_DIR_ROBOTS, "directional keypads that robots are using.")
print("One numeric keypad (on a door) that a robot is using.")
print(result)

