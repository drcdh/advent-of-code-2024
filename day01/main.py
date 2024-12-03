from collections import defaultdict

l1, l2 = [], []
c2 = defaultdict(int)
with open("input", "r") as f:
    for l in f.readlines():
        l = l.strip()
        n1, n2 = l.split("   ")
        l1.append(n1)
        l2.append(n2)
        c2[int(n2)] += 1
l1 = list(map(int, l1))
l2 = list(map(int, l2))
l1.sort()
l2.sort()

diff = map(lambda z: abs(z[0]-z[1]), zip(l1, l2))

diff_sum = sum(diff)

print("Part 1 answer: ", diff_sum)

sim_sum = 0
for n1 in l1:
    sim_sum += n1*c2[n1]
print("Part 2 answer: ", sim_sum)

