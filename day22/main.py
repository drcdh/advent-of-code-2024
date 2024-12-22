from collections import defaultdict
import sys

filepath = sys.argv[1]

with open(filepath, "r") as f:
    initial = [int(l.strip()) for l in f.readlines()]

def mix(val, secret):
    return val^secret

def prune(secret):
    return secret%16777216

def step_1(secret):
    return prune(mix(secret*64, secret))

def step_2(secret):
    return prune(mix(secret//32, secret))

def step_3(secret):
    return prune(mix(secret*2048, secret))

def step(secret):
    secret = step_1(secret)
    secret = step_2(secret)
    secret = step_3(secret)
    return secret

def price(secret):
    return secret%10

bananas_by_change = defaultdict(int)
best_payout = 0
best_seq = None

result = 0
for secret in initial:
    i = secret
    changes = []
    changes_seen = set()
    for _ in range(2000):
        prev_p = price(secret)
        secret = step(secret)
        new_price = price(secret)
        change = new_price-prev_p
        changes.append(change)
        if len(changes) >= 4:
            c4 = tuple(changes[-4:])
            if c4 not in changes_seen:
                bananas_by_change[c4] += new_price
                changes_seen.add(c4)
    if filepath != "input":
        print(f"{i}: {secret}")
    result += secret
print()

print("Part 1:", result)

best_payout = max(bananas_by_change.values())
print("Part 2:", best_payout)

