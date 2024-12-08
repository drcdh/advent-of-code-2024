from collections import defaultdict


filepath = "input"; SIZE = 50
#filepath = "test"; SIZE = 12

antennae = defaultdict(list)

with open(filepath, "r") as f:
    for y, line in enumerate(f.readlines()):
        for x, l in enumerate(line):
            if l != ".":
                antennae[l].append((x, y))

antinodes = set()
antinodes2 = set()

for freq, a in antennae.items():
    for i, (x1, y1) in enumerate(a[:-1]):
        for x2, y2 in a[i+1:]:
            dx, dy = x2-x1, y2-y1
            d = 0
            count = 0
            while True:
                new_anti = False
                ax, ay = x1-d*dx, y1-d*dy
                if not (ax < 0 or ay < 0 or ax >= SIZE or ay >= SIZE):
                    count += 1
                    new_anti = True
                    antinodes2.add((ax, ay))
                    if d == 1:
                        antinodes.add((ax, ay))
                ax, ay = x2+d*dx, y2+d*dy
                if not (ax < 0 or ay < 0 or ax >= SIZE or ay >= SIZE):
                    count += 1
                    new_anti = True
                    antinodes2.add((ax, ay))
                    if d == 1:
                        antinodes.add((ax, ay))
                d += 1
                if not new_anti:
                    break

print(f"Part 1: {len(antinodes)}")
print(f"Part 2: {len(antinodes2)}")

