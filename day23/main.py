import sys
from collections import defaultdict

filepath = sys.argv[1]

comps = defaultdict(list)

with open(filepath, "r") as f:
    for line in f.readlines():
        c1, c2 = line.strip().split("-")
        comps[c1].append(c2)
        comps[c2].append(c1)

def find_next_largest_subnets(subnets):
    larger_subnets = set()
    for subnet in subnets:
        common = None
        cl = subnet.split(",")
        for c in cl:
            common = common or set(comps[c])
            common &= set(comps[c])
        for new_c in common:
            subnet = ",".join(sorted(cl + [new_c]))
            larger_subnets.add(subnet)
    return larger_subnets

subnets = set(comps.keys())
for _ in range(2):
    subnets = find_next_largest_subnets(subnets)
result_1 = len([sn_ for sn_ in subnets if sn_.startswith("t") or ",t" in sn_])
print("Part 1:", result_1)

while len(subnets) > 1:
    subnets = find_next_largest_subnets(subnets)
print("Part 2:", subnets.pop())

