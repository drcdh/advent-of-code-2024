from collections import defaultdict
from pprint import pprint
import sys

filepath = sys.argv[1]

regions = defaultdict(list)

def adjacent_to_any(x, y, region):
    for rx, ry in region:
        if (x, y) in [(rx, ry-1), (rx, ry+1), (rx-1, ry), (rx+1, ry)]:
            return True
    return False

with open(filepath, "r") as f:
    for y, line in enumerate(f.readlines()):
        for x, p in enumerate(line.strip()):
            for region in regions[p]:
                if adjacent_to_any(x, y, region):
                    region.add((x, y))
                    break
            else:
                regions[p].append({(x, y)})

for p_regions in regions.values():
    while True:
        move_made = False
        for i in range(len(p_regions)-1):
            for j in range(i+1, len(p_regions)):
                join = None
                for ip in p_regions[i]:
                    if adjacent_to_any(*ip, p_regions[j]):
                        join = (i, j)
                        break
                if join is not None:
                    p_regions[i] |= p_regions[j]
                    del p_regions[j]
                    move_made = True
                    break
            if move_made:
                break
        if not move_made:
            break

if filepath != "input":
    pprint(dict(regions))

def _perimeter(x, y, region):
    return 4-sum([
        (x-1, y) in region,
        (x+1, y) in region,
        (x, y-1) in region,
        (x, y+1) in region,
        ])

def perimeter(region):
    return sum(_perimeter(*p, region) for p in region)

def cost(region):
    return perimeter(region)*len(region)

def _corners(x, y, region):
    return sum([
        (x-1, y) not in region and (x, y-1) not in region,
        (x-1, y) not in region and (x, y+1) not in region,
        (x+1, y) not in region and (x, y-1) not in region,
        (x+1, y) not in region and (x, y+1) not in region,
        (x-1, y) in region and (x, y-1) in region and (x-1, y-1) not in region,
        (x-1, y) in region and (x, y+1) in region and (x-1, y+1) not in region,
        (x+1, y) in region and (x, y-1) in region and (x+1, y-1) not in region,
        (x+1, y) in region and (x, y+1) in region and (x+1, y+1) not in region,
    ])

def sides(region):
    return sum(_corners(*p, region) for p in region)

def discount_cost(region):
    return sides(region)*len(region)

result_1, result_2 = 0, 0
for p, p_regions in regions.items():
    for region in p_regions:
        c = cost(region)
        d = discount_cost(region)
        result_1 += c
        result_2 += d
        if filepath != "input":
            print(f"Cost of {p}: {c}")
            print(f"Discount cost of {p}: {d}")

print(f"Part 1: {result_1}")
print(f"Part 2: {result_2}")

