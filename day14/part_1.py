import re
import sys

filepath = sys.argv[1]
WIDTH = int(sys.argv[2])
HEIGHT = int(sys.argv[3])
secs = int(sys.argv[4])

q_cnts = {1: 0, 2: 0, 3: 0, 4: 0, None: 0}
qh, qw = HEIGHT//2, WIDTH//2

def pos_t(p, v, dt):
    return (
        (p[0] + v[0]*dt) % WIDTH,
        (p[1] + v[1]*dt) % HEIGHT,
    )

def quad(p):
    if p[0] < qw and p[1] < qh:
        return 1
    if p[0] >= qw+1 and p[1] < qh:
        return 2
    if p[0] < qw and p[1] >= qh+1:
        return 3
    if p[0] >= qw+1 and p[1] >= qh+1:
        return 4

with open(filepath, "r") as f:
    for line in f.readlines():
        line = line.strip()
        m = re.match(r"p=(-?\d+),(-?\d+) v=(-?\d+),(-?\d+)", line)
        p = tuple(map(int, (m[1], m[2])))
        v = tuple(map(int, (m[3], m[4])))
        q_cnts[quad(pos_t(p, v, secs))] += 1

result = q_cnts[1]*q_cnts[2]*q_cnts[3]*q_cnts[4]
print(f"Part 1: {result}")

