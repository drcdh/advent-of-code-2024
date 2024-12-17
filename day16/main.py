from pprint import pprint
import sys

sys.setrecursionlimit(20000)

filename = sys.argv[1]

NORTH = 0
EAST = 1
SOUTH = 2
WEST = 3

unvisited = set()
start, end = None, None
with open(filename, "r") as f:
    for y, line in enumerate(f.readlines()):
        for x, c in enumerate(line.strip()):
            if c == "S":
                start = ((x, y), EAST)
            elif c == "E":
                end = (x, y)
            if c in "SE.":
                for d in range(4):
                    unvisited.add(((x, y), d))

def turn_cost(d0, d1):
    if d0 == NORTH and d1 == SOUTH:
        return 2000
    if d0 == EAST and d1 == WEST:
        return 2000
    return 1000*(d0 != d1)

costs = {start: 0}
shortest_path_directions = {start: EAST}
def get_closest_unvisited():
    return min(unvisited, key=lambda n: costs.get(n, float('inf')))

def get_unvisited_neighbors(p, d):
    dx, dy = 0, 0
    if d == NORTH:
        dy = -1
    elif d == SOUTH:
        dy = 1
    elif d == EAST:
        dx = 1
    else:
        dx = -1
    return [pdc for pdc in [
        (((p[0] + dx, p[1] + dy), d), 1),
        ((p, (d+1)%4), 1000),
        ((p, (d-1)%4), 1000),
    ] if pdc[0] in unvisited]

def done():
    for d in range(4):
        if (end, d) in unvisited:
            return False
    return True

while unvisited and not done():
    current = get_closest_unvisited()
    for considered, move_cost in get_unvisited_neighbors(*current):
        new_cost = costs[current] + move_cost
        if considered not in costs or new_cost < costs[considered]:
            costs[considered] = new_cost
    unvisited.remove(current)

print("Part 1: ", min(costs.get((end, d)) for d in range(4)))

# WARNING: this "solution" to part 2 fails in some cases, but it got me my star... :-/
tiles = set()
def best_path_tiles_to(p=end, d=NORTH):
    if p in tiles:
        return
    tiles.add(p)
    cost = costs[(p, d)]
    for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
        pp = (p[0] + dx, p[1] + dy)
        if (pp, d) in costs and costs[(pp, d)] < cost:
            best_path_tiles_to(pp, d)
    for dd in range(4):
        if d == dd:
            continue
        if (p, dd) in costs and costs[(p, dd)] < cost:
            best_path_tiles_to(p, dd)

best_path_tiles_to()
print("Part 2: ", len(tiles))

