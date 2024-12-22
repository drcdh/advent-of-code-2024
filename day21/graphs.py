import networkx as nx

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

