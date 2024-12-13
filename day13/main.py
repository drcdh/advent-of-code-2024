import re
import sys

import numpy as np


filepath = sys.argv[1]
extra = 10000000000000 if len(sys.argv) > 2 else 0

def parse_A(l):
    m = re.match(r"Button A: X\+(\d+), Y\+(\d+)", l)
    return int(m[1]), int(m[2])

def parse_B(l):
    m = re.match(r"Button B: X\+(\d+), Y\+(\d+)", l)
    return int(m[1]), int(m[2])

def parse_prize(l):
    m = re.match(r"Prize: X=(\d+), Y=(\d+)", l)
    return int(m[1]), int(m[2])


def play_game(a, b, p):
    a = np.array([a, b]).T
    b = np.array(p)
    b += extra
    n = np.linalg.solve(a, b)
    if np.any(n < 0):
        t = 0
    else:
        n = np.round(n).astype(int)
        if np.all(np.dot(a, n) == b):
            t = 3*n[0] + n[1]
        else:
            t = 0
    return t
    

with open(filepath, "r") as f:
    a, b, p = None, None, None
    total = 0
    for n, l in enumerate(f.readlines()):
        if n%4 == 0:
            a = parse_A(l)
        elif n%4 == 1:
            b = parse_B(l)
        elif n%4 == 2:
            p = parse_prize(l)
        else:
            t = play_game(a, b, p)
            total += t
    t = play_game(a, b, p)
    total += t

print(total)
