import itertools
import sys

import numpy as np

filepath = sys.argv[1]

def read_keylock(lines):
    h = [0]*5
    is_key = lines[0].strip() == "."*5
    for line in lines[1:6]:
        for i, l in enumerate(line.strip()):
            if l == "#":
                h[i] += 1
    return np.array(h), is_key

with open(filepath, "r") as f:
    things = [read_keylock(lines) for lines in itertools.batched(f.readlines(), 8)]

count = 0
for i in range(len(things)-1):
    for j in range(i+1, len(things)):
        if things[i][1] == things[j][1]:
            continue
        if np.all(things[i][0]+things[j][0] <= 5):
            count += 1

print("Result:", count)

