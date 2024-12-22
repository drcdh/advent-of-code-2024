from pprint import pprint

input = [
    "319A",
    "985A",
    "340A",
    "489A",
    "964A",
]
test = [
    "029A",
    "980A",
    "179A",
    "456A",
    "379A",
]
input = test


import networkx as nx

# Final robot
G_numeric = nx.DiGraph()
for edge, cmd in [
    (("7", "8"), ">"),
    (("7", "4"), "v"),
    (("8", "9"), ">"),
    (("8", "5"), "v"),
    (("9", "6"), "v"),
    (("4", "5"), ">"),
    (("4", "1"), "v"),
    (("5", "6"), ">"),
    (("5", "2"), "v"),
    (("6", "3"), "v"),
    (("1", "2"), ">"),
    (("2", "3"), ">"),
    (("2", "0"), "v"),
    (("3", "A"), "v"),
    (("0", "A"), ">"),

    (("8", "7"), "<"),
    (("4", "7"), "^"),
    (("9", "8"), "<"),
    (("5", "8"), "^"),
    (("6", "9"), "^"),
    (("5", "4"), "<"),
    (("1", "4"), "^"),
    (("6", "5"), "<"),
    (("2", "5"), "^"),
    (("3", "6"), "^"),
    (("2", "1"), "<"),
    (("3", "2"), "<"),
    (("0", "2"), "^"),
    (("A", "3"), "^"),
    (("A", "0"), "<"),
]:
    G_numeric.add_edge(*edge, cmd=cmd)

G_directional = nx.DiGraph()
for edge, cmd in [
    (("^", "A"), ">"),
    (("A", "^"), "<"),
    (("<", "v"), ">"),
    (("v", "<"), "<"),
    (("^", "v"), "v"),
    (("v", "^"), "^"),
    (("v", ">"), ">"),
    ((">", "v"), "<"),
    (("A", ">"), "v"),
    ((">", "A"), "^"),
]:
    G_directional.add_edge(*edge, cmd=cmd)


def convert_to_presses(G_, path):
    cmds = ""
    for p1, p2 in zip(path[:-1], path[1:]):
        cmds += G_[p1][p2]["cmd"]
    return cmds

import functools

ROBOTS = 2

def total_cmds(presses, l=ROBOTS):
    #presses = "A" + presses
    return sum(min_cmds(b1, b2, l) for b1, b2 in zip(presses[:-1], presses[1:]))

@functools.cache
def min_cmds(b1, b2, l):
    if l == ROBOTS:
        # numeric
        if l == 0:
            p = nx.shortest_path(G_numeric, b1, b2)
            print(p)
            return len(p)
        return total_cmds(min(
            [convert_to_presses(G_numeric, _p) for _p in nx.all_shortest_paths(G_numeric, b1, b2)],
            key=lambda presses: total_cmds(presses, l-1)
        ), l-1)
    if l == 0:
        return nx.shortest_path_length(G_directional, b1, b2)
    blah = [convert_to_presses(G_directional, _p) for _p in nx.all_shortest_paths(G_directional, b1, b2)]
    pprint(blah)
    return total_cmds(min(
        blah,
        key=lambda presses: total_cmds(presses, l-1)
    ), l-1)

#print(input[0], total_cmds(input[0], 0))
#print(min_cmds("<", "v", 1))
#print(total_cmds("<v", 1))
#print(total_cmds(input[0]))
print("A"+input[0], total_cmds(input[0]))
