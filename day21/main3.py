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

def append_to_all(l, s):
    if not l:
        return (s,)
    return tuple(_l+s for _l in l)

def append_many_to_many(l1, l2):
    if not l1:
        yield from l2
    else:
        for l1_ in l1:
            for l2_ in l2:
                yield l1_+l2_

import functools

def convert_num_cmds(path):
    cmds = ""
    for p1, p2 in zip(path[:-1], path[1:]):
        cmds += G_numeric[p1][p2]["cmd"]
    return cmds

#@functools.cache
def convert_dir_cmds(path):
    cmds = ""
    for p1, p2 in zip(path[:-1], path[1:]):
        cmds += G_directional[p1][p2]["cmd"]
    return cmds

def best_cmds_num(input, l):
    input = "A" + input
    candidates = None
    for b1, b2 in zip(input[:-1], input[1:]):
        subpaths = nx.all_shortest_paths(G_numeric, b1, b2)
        subcmds = tuple(map(convert_num_cmds, subpaths))
        #pprint(subcmds)
        candidates = append_many_to_many(candidates, subcmds)
        candidates = append_to_all(candidates, "A")
    #pprint(candidates)
    return min(
        candidates,
        key=lambda cc: len(cc)+len(best_cmds_dir(cc, l-1)),
    )

def best_cmds_dir(input, l):
    candidates = None
    inputs = input.split("A")[:-1]
    #pprint(input)
    #pprint(inputs)
    for i, _input in enumerate(inputs):
        #if i < len(inputs)-1:
        #    _input += "A"
        subcands = _best_cmds_dir(_input + "A", l)
        candidates = append_many_to_many(candidates, subcands)
    best = min(candidates, key=len)
    return best

def _best_cmds_dir(to_press, l):
    #print(f"{l=}  {to_press=}")
    candidates = None
    # start at A
    path = "A" + to_press
    for b1, b2 in zip(path[:-1], path[1:]):
        subpaths = nx.all_shortest_paths(G_directional, b1, b2)
        subcmds = tuple(map(convert_dir_cmds, subpaths))
        # move from b1 to b2
        candidates = append_many_to_many(candidates, subcmds)
        # press b2
        candidates = append_to_all(candidates, "A")
    if l == 0:
        smallest_len = min(map(len, candidates))
        return tuple(
            cc for cc in candidates if len(cc) == smallest_len
        )
    else:
        #metacandidates = tuple(best_cmds_dir(cc, l-1) for cc in candidates)
        multilens = [
            len(cc)+len(best_cmds_dir(cc, l-1))
                    for cc in candidates
        ]
        best_len = min(multilens)
        return tuple(
            cc for ml, cc in zip(multilens, candidates) if ml == best_len
        )

ROBOTS = 2

#print(input[0], convert_num_cmds(input[0]))

if __name__ == "__main__":
    blah = best_cmds_dir("<A>A<AAv<AA>>^AvAA^A<vAAA^>A", 1)
    print(blah, [len(b) for b in blah])
    #print(_best_cmds_dir("v<A", 1))
    print()
    for code in input[-1:]:
        blah = best_cmds_num(code, 2)
        #print(blah)
        blarg = best_cmds_dir(blah, 1)
        print(blarg)
        blarg = best_cmds_dir(blarg, 0)
        print(len(blarg), blarg)


