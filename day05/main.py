import pprint
from collections import defaultdict

filepath = "input"
#filepath = "test"

rules = defaultdict(list)
updates = []

with open(filepath, "r") as f:
    read_updates = False
    for l in f.readlines():
        l = l.strip()
        if not l:
            read_updates = True
            continue
        if not read_updates:
            p1, p2 = l.split("|")
            rules[int(p1)].append(int(p2))
        else:
            updates.append(list(map(int, l.split(","))))

if filepath == "test":
    pprint.pprint(rules)
    pprint.pprint(updates)

def order(update):
    update = set(update)
    ordered = []
    while update:
        for p in update:
            if set(rules[p]) >= update^{p}:
                ordered.append(p)
                break
        else:
            raise Exception(update)
        update.remove(ordered[-1])
    return ordered

def check(update):
    for i, p1 in enumerate(update[:-1]):
        for p2 in update[i+1:]:
            if p2 not in rules[p1]:
                return 0, order(update)[(len(update)-1)//2]
    return update[(len(update)-1)//2], 0

results = [check(_u) for _u in updates]

result_A = sum(r[0] for r in results)
result_B = sum(r[1] for r in results)
print(f"Part A: {result_A}")
print(f"Part B: {result_B}")

