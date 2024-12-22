import functools
import sys

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
#input = test


from pprint import pprint
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
        return [s]
    return tuple(_l+s for _l in l)

def append_many_to_many(l1, l2):
    if not l1:
        yield from l2
    else:
        for l1_ in l1:
            for l2_ in l2:
                yield l1_+l2_

def convert_to_presses(G_, path):
    cmds = ""
    for p1, p2 in zip(path[:-1], path[1:]):
        cmds += G_[p1][p2]["cmd"]
    return cmds

numeric_paths = dict(nx.all_pairs_all_shortest_paths(G_numeric))
numeric_cmds = {
    b1: {
        b2: [
            convert_to_presses(G_numeric, path)+"A"
            for path in paths
        ] for b2, paths in b1_dict.items()
    } for b1, b1_dict in numeric_paths.items()
}

directional_paths = dict(nx.all_pairs_all_shortest_paths(G_directional))
directional_cmds = {
    b1: {
        b2: [
            convert_to_presses(G_directional, path)+"A"
            for path in paths
        ] for b2, paths in b1_dict.items()
    } for b1, b1_dict in directional_paths.items()
}

def cmds_from_prev_robot(to_press: str, numeric=False):
    paths = numeric_cmds if numeric else directional_cmds
    path = "A" + to_press
    possibilities = None
    #print(f"{numeric=} {path=}")
    for b1, b2 in zip(path[:-1], path[1:]):
        possibilities = append_many_to_many(possibilities, paths[b1][b2])
    return tuple(possibilities)

#print(cmds_from_prev_robot("2A", True))
print(cmds_from_prev_robot("v<"))
print(cmds_from_prev_robot("<v"))
print()
for _cmds in cmds_from_prev_robot("v<"):
    print(list(map(len, cmds_from_prev_robot(_cmds))))
for _cmds in cmds_from_prev_robot("<v"):
    print(list(map(len, cmds_from_prev_robot(_cmds))))

def blarg(cmds, layers=2, numeric=False):
    #return len(min(cmds_from_prev_robot(cmds, numeric), key=len))
    if isinstance(cmds, str):
        cmds = (cmds,)
    for _ in range(layers):
        prev = cmds
        cmds = ()
        for _cmds in prev:
            cmds = cmds + cmds_from_prev_robot(_cmds, numeric)
    return len(min(cmds, key=len))

print(blarg("v<"))
print(blarg("<v"))
print()

def remove_long_entries(l, key):
    shortest_len = key(min(l, key=key))
    return tuple(_l for _l in l if key(_l) == shortest_len)

print(remove_long_entries(directional_cmds["A"]["v"], blarg))
print()

def apply_to_values(d, f, *args, **kwargs):
    if isinstance(d, dict):
        return {k: apply_to_values(v, f, *args, **kwargs) for k, v in d.items()}
    fd = f(d, *args, **kwargs)
    #print(f"{d=}  {fd=}")
    return fd

def remove_suboptimal_cmds(cmds_dict, layers=2, numeric=False):
    return apply_to_values(cmds_dict, remove_long_entries, lambda cmd: blarg(cmd, layers=layers, numeric=numeric))

pprint(numeric_cmds)
print()
numeric_cmds = remove_suboptimal_cmds(numeric_cmds, 1)
numeric_cmds = remove_suboptimal_cmds(numeric_cmds, 2)
#numeric_cmds = remove_suboptimal_cmds(numeric_cmds, 3)
pprint(numeric_cmds)
print()

#pprint(directional_cmds)
#print()
directional_cmds = remove_suboptimal_cmds(directional_cmds, layers=1)
directional_cmds = remove_suboptimal_cmds(directional_cmds, layers=2)
directional_cmds = remove_suboptimal_cmds(directional_cmds, layers=3)
#pprint(directional_cmds)
#print()
directional_cmds = remove_suboptimal_cmds(directional_cmds, layers=4)
pprint(directional_cmds)

#print(blarg("^>A", 4))
#print(blarg(">^A", 4))
#print()

#sys.setrecursionlimit(20000)

NUM_DIR_ROBOTS = int(sys.argv[1])

if NUM_DIR_ROBOTS < 7:
    result_1 = 0
    for cmds in input:
        n = int(cmds[:-1])
        print(cmds)
        numeric = True
        for _ in range(NUM_DIR_ROBOTS):
            cmds = min(cmds_from_prev_robot(cmds, numeric=numeric), key=len)
            #print(cmds)
            numeric = False
        complexity = n*len(cmds)
        result_1 += complexity
        print(len(cmds), complexity)
    print("Part 1 (method A):", result_1)

@functools.cache
def length_of_command(cmds, layer, numeric=False):
    if layer == 0:
        return len(cmds)
    l = 0
    for _cmds in cmds.split("A")[:-1]:
        _cmds = _cmds+"A"
        #next_cmds = min(cmds_from_prev_robot(_cmds, numeric=numeric), key=len)
        next_cmds = min(cmds_from_prev_robot(_cmds, numeric=numeric), key=lambda _c: length_of_command(_c, layer-1))
        l += length_of_command(next_cmds, layer-1, numeric=False)
    return l

result_1 = 0
for cmds in input:
    n = int(cmds[:-1])
    l = length_of_command(cmds, layer=NUM_DIR_ROBOTS, numeric=True)
    complexity = n*l
    result_1 += complexity
    print(len(cmds), complexity)
print("Part 1 (method B):", result_1)

