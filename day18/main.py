import sys

filepath = sys.argv[1]
SIZE = int(sys.argv[2])
BYTES = int(sys.argv[3]) if len(sys.argv) > 3 else None


start = (SIZE-1, SIZE-1)
end = (0, 0)

with open(filepath, "r") as f:
    corruption = [
        tuple(map(int, s.strip().split(","))) for s in f.readlines()
    ]

def get_closest(unvisited, dist):
    return min(unvisited, key=lambda n: dist.get(n, float('inf')))

def get_unvisited_neighbors(x, y, unvisited):
    for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
        blah = x+dx, y+dy
        if blah in unvisited and x >= 0 and x < SIZE and y >= 0 and y < SIZE:
            yield blah

def try_find_path(n):
    dist = {start: 0}
    unvisited = set()
    for y in range(SIZE):
        for x in range(SIZE):
            if (x, y) not in corruption[:n]:
                unvisited.add((x, y))

    while unvisited:
        current = get_closest(unvisited, dist)
        for considered in get_unvisited_neighbors(*current, unvisited):
            try:
                new_cost = dist[current] + 1
            except KeyError:
                # path blocked
                return None
            if considered not in dist or new_cost < dist[considered]:
                dist[considered] = new_cost
        unvisited.remove(current)
        if end in dist:
            break
    return dist[end]

if BYTES:
    print("Part 1:", try_find_path(BYTES))

def find_least_satisfying(f, minimum, maximum):
    if f(minimum):
        return minimum
    high_false = minimum
    if not f(maximum):
        return None
    low_true = maximum
    while high_false < low_true-1:
        trial = (low_true - high_false)//2 + high_false
        if f(trial):
            low_true = trial
        else:
            high_false = trial
    return low_true

fewest_to_block = find_least_satisfying(
    lambda n: try_find_path(n) is None,
    BYTES or 0,
    len(corruption)-1,
)
print("Part 2:", ",".join(map(str, corruption[fewest_to_block-1])))

