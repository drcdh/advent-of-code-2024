
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

import functools

@functools.cache
def shortest_paths(G_, s, t):
    return tuple(nx.all_shortest_paths(G_, s, t))

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

@functools.cache
def get_shortest_robot_cmds(G_, commands, commanding_Gs=None):
    commands = "A" + commands
    new_command_candidates = []
    for b1, b2 in zip(commands[:-1], commands[1:]):
        move_cmd_candidates = []
        for path in nx.all_shortest_paths(G_, source=b1, target=b2):
            _cmds = ""
            for p1, p2 in zip(path[:-1], path[1:]):
                _cmds += G_[p1][p2]["cmd"]
            move_cmd_candidates.append(_cmds+"A")
        #print(move_cmd_candidates)
        new_command_candidates = list(append_many_to_many(new_command_candidates, move_cmd_candidates))
    #print(new_command_candidates)
    if commanding_Gs:
        return min(new_command_candidates, key=lambda cc: len(cc)+len(get_shortest_robot_cmds(commanding_Gs[0], cc, commanding_Gs[1:])))
    return new_command_candidates[0]

#print(get_shortest_robot_cmds(G_numeric, test[0], G_directional))

def complexity(code):
    sequence = get_shortest_robot_cmds(
        G_directional,
        get_shortest_robot_cmds(
            G_directional,
            get_shortest_robot_cmds(
                G_numeric,
                code,
                (G_directional, G_directional)
            ),
            (G_directional,)
        ),
    )
    print(f"{code=}   {sequence=}")
    l = len(sequence)
    n = int(code[:-1])
    print(f"{l=} {n=}")
    return l*n

#print("Part 1:", sum(complexity(c_) for c_ in input))

def convert_to_presses(G_, path):
    cmds = ""
    for p1, p2 in zip(path[:-1], path[1:]):
        cmds += G_[p1][p2]["cmd"]
    return cmds

numeric_paths = dict(nx.all_pairs_all_shortest_paths(G_numeric))
numeric_cmds = {
    b1: {
        b2: [
            convert_to_presses(G_numeric, path)
            for path in paths
        ] for b2, paths in b1_dict.items()
    } for b1, b1_dict in numeric_paths.items()
}

from pprint import pprint
#pprint(numeric_cmds)

directional_paths = dict(nx.all_pairs_all_shortest_paths(G_directional))
directional_cmds = {
    b1: {
        b2: [
            convert_to_presses(G_directional, path)
            for path in paths
        ] for b2, paths in b1_dict.items()
    } for b1, b1_dict in directional_paths.items()
}

@functools.cache
def best_robot_controlled_directional_commands(code, controlled=True):
    code = "A" + code
    candidates = []
    for b1, b2 in zip(code[:-1], code[1:]):
        candidates = append_many_to_many(candidates, directional_cmds[b1][b2])
        candidates = append_to_all(candidates, "A")
    #pprint(candidates)
    if not controlled:
        return min(candidates, key=len)
    return min(candidates, key=lambda c: len(best_robot_controlled_directional_commands(c, False)))

def get_possible_commands(code, Gc):
    code = "A" + code
    candidates = tuple()
    for b1, b2 in zip(code[:-1], code[1:]):
        candidates = append_many_to_many(candidates, Gc[b1][b2])
        candidates = append_to_all(candidates, "A")
    return candidates

def do_layer(possibles):
    blah = []
    for p in possibles:
        blah.extend(get_possible_commands(p, directional_cmds))
    l = len(min(blah, key=len))
    return [b_ for b_ in blah if len(b_) == l]

def get_shortest_human_command(code):
    possible_numerical_commands = get_possible_commands(code, numeric_cmds)
    blah = possible_numerical_commands
    for _ in range(2):
        blah = do_layer(blah)
    return min(blah, key=len)

def get_shortest_human_command_2(code, n_directional_robots=2):
    blah = tuple(get_possible_commands(code, numeric_cmds))
    for _ in range(n_directional_robots):
        blah = tuple(best_robot_controlled_directional_commands(_blah) for _blah in blah)
    #blah = best_robot_controlled_directional_commands(code, False)
    return min(blah, key=len)

if __name__ == "__main__":
    result = 0
    for code in input:
        h = get_shortest_human_command(code)
        l = len(h)
        n = int(code[:-1])
        result += l*n
        print(f"{l}  {h}")
    print("Part 1:", result)

