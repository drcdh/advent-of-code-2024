
filepath = "input"
#filepath = "test"

diskmap = open(filepath, "r").read().strip()

diskmap = [
    (i//2 if i%2==0 else None, int(b)) for i, b in enumerate(diskmap)
]

moved = set()

done = False
while not done:
    move_made = False
    for j in range(len(diskmap))[::-1]:
        r = diskmap[j]
        if r[0] is None or r[0] in moved:
            continue
        for i in range(j):
            l = diskmap[i]
            if l[0] is not None:
                continue
            if l[1] >= r[1]:
                # rh file will fit
                diskmap[i] = (None, l[1] - r[1])
                diskmap[j] = (None, r[1])
                #diskmap.insert(i, (None, 0))
                diskmap.insert(i, r)
                moved.add(r[0])
                move_made = True
                break
        if move_made:
            break
    else:
        done = True

checksum = 0
i = 0
for d in diskmap:
    for _ in range(d[1]):
        if filepath == "test":
            print((d[0] if d[0] is not None else "."), end="")
        checksum += i*(d[0] or 0)
        i += 1
print()

print(f"Part 2: {checksum}")

