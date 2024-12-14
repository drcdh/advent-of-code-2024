import re
import sys

filepath = sys.argv[1]
secs = int(sys.argv[2])
HEIGHT = int(sys.argv[3])
WIDTH = int(sys.argv[4])

p, v = [], []
with open(filepath, "r") as f:
    for line in f.readlines():
        line = line.strip()
        m = re.match(r"p=(-?\d+),(-?\d+) v=(-?\d+),(-?\d+)", line)
        p.append([int(m[1]), int(m[2])])
        v.append([int(m[3]), int(m[4])])

if filepath != "input":
    print(p)
    print(v)

def move(p, v):
    p = [p[0]+v[0], p[1]+v[1]]
    if p[0] >= WIDTH:
        p[0] = p[0] - WIDTH
    elif p[0] < 0:
        p[0] = WIDTH + p[0]
    if p[1] >= HEIGHT:
        p[1] = p[1] - HEIGHT
    elif p[1] < 0:
        p[1] = HEIGHT + p[1]
    return p

while secs > 0:
    for i in range(len(p)):
        p[i] = move(p[i], v[i])
    secs -= 1

def count(p, xr, yr):
    c = 0
    for _p in p:
        if _p[0] >= xr[0] and _p[0] < xr[1] and _p[1] >= yr[0] and _p[1] < yr[1]:
            c += 1
    return c

qh, qw = HEIGHT//2, WIDTH//2
q1 = count(p, (0, qw), (0, qh))
q2 = count(p, (qw+1, WIDTH), (0, qh))
q3 = count(p, (0, qw), (qh+1, HEIGHT))
q4 = count(p, (qw+1, WIDTH), (qh+1, HEIGHT))

print(q1*q2*q3*q4)

