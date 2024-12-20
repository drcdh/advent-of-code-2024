# Race Condition

import sys
from collections import defaultdict
from time import time

filepath = sys.argv[1]
size = int(sys.argv[2])
max_cheat_dist = int(sys.argv[3])
min_savings = int(sys.argv[4])

start, end = None, None
tracks = []
with open(filepath, "r") as f:
    for y, line in enumerate(f.readlines()):
        line = line.strip()
        for x, l in enumerate(line):
            if l in "SE.":
                tracks.append((x, y))
            if l == "S":
                start = (x, y)
            elif l == "E":
                end = (x, y)


def get_closest(unvisited, dist):
    return min(unvisited, key=lambda n: dist.get(n, float('inf')))

def get_unvisited_neighbors(x, y, unvisited):
    for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
        blah = x+dx, y+dy
        if blah in unvisited:
            yield blah

def get_cost(start, end, additional=None):
    dist = {start: 0}
    unvisited = set(tracks)
    if additional is not None:
        unvisited |= additional

    while unvisited:
        current = get_closest(unvisited, dist)
        for considered in get_unvisited_neighbors(*current, unvisited):
            new_cost = dist[current] + 1
            if considered not in dist or new_cost < dist[considered]:
                dist[considered] = new_cost
        unvisited.remove(current)
        if end in dist:
            break
    return dist

start_1 = time()
no_cheats_costs = get_cost(start, end)
t1 = time() - start_1
no_cheats_cost = no_cheats_costs[end]
print(f"Cost w/o cheating: {no_cheats_cost}  ({t1:.3f} seconds)")

def iter_separated_tracks(max_dist=2):
    for i in range(len(tracks)-1):
        ti = tracks[i]
        for j in range(i+1, len(tracks)):
            tj = tracks[j]
            d = abs(ti[0] - tj[0]) + abs(ti[1] - tj[1])
            if 1 < d <= max_dist:
                yield d, ti, tj

savings = defaultdict(int)
for d, t1, t2 in iter_separated_tracks(max_cheat_dist):
    cost_saved = abs(no_cheats_costs[t1] - no_cheats_costs[t2]) - d
    if cost_saved > 0:
        savings[cost_saved] += 1

print(f"Ways to save >={min_savings}:", sum(v for k, v in savings.items() if k >= min_savings))

