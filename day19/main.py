import functools

import test as input
#import input

available = input.available.split(", ")
patterns = input.patterns.split("\n")

@functools.cache
def possible(p):
    count = 0
    for a in available:
        if p == a:
            count += 1
            continue
        if p.startswith(a):
            if (ways := possible(p[len(a):])) > 0:
                count += ways
    return count

print("Part 1:", sum(possible(p) > 0 for p in patterns))
print("Part 2:", sum(possible(p) for p in patterns))

