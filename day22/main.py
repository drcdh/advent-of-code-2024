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


prices = []
changes = []
changes_to_prices = []

result = 0
for secret in initial:
    i = secret
    p, c = [], []
    c2p = {}
    for _ in range(2000):
        prev_p = secret%10
        secret = step(secret)
        price = secret%10
        p.append(price)
        change = p[-1]-prev_p
        c.append(change)
        if len(c) >= 4:
            c4 = tuple(c[-4:])
            if c4 not in c2p:
                c2p[c4] = price
    if filepath != "input":
        print(f"{i}: {secret}")
    result += secret
    prices.append(p)
    changes.append(c)
    changes_to_prices.append(c2p)
print()

print("Part 1:", result)

all_sequences = set()
for _c2p in changes_to_prices:
    all_sequences |= _c2p.keys()

best_payout = 0
best_seq = None
for seq in all_sequences:
    payout = sum(
        _c2p.get(seq, 0) for _c2p in changes_to_prices
    )
    if payout > best_payout:
        best_payout = payout
        best_seq = seq

print("Part 2:", best_payout)

