import time


filepath = "input"; SIZE = 130
#filepath = "test"; SIZE = 10

N = ( 0, -1)
S = ( 0,  1)
E = ( 1,  0)
W = (-1,  0)

turns = {
    N: E,
    E: S,
    S: W,
    W: N,
}

obstacles = set()
starting_pos = None
starting_direction = None

with open(filepath, "r") as f:
    for y, line in enumerate(f.readlines()):
        for x, l in enumerate(line.strip()):
            if l == "#":
                obstacles.add((x, y))
            elif l == "^":
                starting_pos = (x, y)
                starting_direction = N
            else:
                pass

if filepath == "test":
    print(starting_pos, starting_direction)
    print(obstacles)

def turn(d):
    return turns[d]

def step(p, d):
    return p[0] + d[0], p[1] + d[1]

def move(p, d, obs, extra=None):
    while step(p, d) in obs:
        d = turn(d)
    p = step(p, d)
    return p, d

def outside(p):
    if p[0] < 0 or p[1] < 0:
        return True
    if p[0] >= SIZE or p[1] >= SIZE:
        return True
    return False



def run(extra=None):
    obs = obstacles|{extra} if extra is not None else obstacles
    p = starting_pos
    d = starting_direction
    visited = {starting_pos}
    visited_dir = {(starting_pos, starting_direction)}
    while True:
        p, d = move(p, d, obs)
        if (p, d) in visited_dir:
            return visited, True
        if outside(p):
            return visited, False
        visited.add(p)
        visited_dir.add((p, d))

t0 = time.time()
result_A = run()
tA = time.time() - t0
print(f"Part A: {len(result_A[0])}  (took {tA:.6f} seconds)")

loop_count = 0
t0 = time.time()
for extra in result_A[0]:
    if extra == starting_pos:
        continue
    loop_count += run(extra)[1]
tB = time.time() - t0

print(f"Part B: {loop_count}  (took {tB:.6f} seconds)")

