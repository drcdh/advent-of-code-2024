import functools
import sys


@functools.cache
def count_stones(s, b):
    if b == 0:
        return 1
    if s == 0:
        return count_stones(1, b-1)
    else:
        s_str = str(s)
        l = len(s_str)
        if l%2 == 0:
            l_s = int(s_str[:l//2])
            r_s = int(s_str[l//2:])
            return count_stones(l_s, b-1) + count_stones(r_s, b-1)
        else:
            return count_stones(s*2024, b-1)

filepath = sys.argv[1]
blinks = int(sys.argv[2])

with open(filepath, "r") as f:
    result = sum(count_stones(s, blinks) for s in map(int, f.read().strip().split(" ")))
print(f"Number of stones after {blinks} blinks: {result}")

