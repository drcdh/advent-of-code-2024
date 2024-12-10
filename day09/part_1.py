
filepath = "input"
#filepath = "test"
#filepath = "test2"

diskmap = open(filepath, "r").read().strip()


checksum = 0

l, r = 0, len(diskmap)-1
l_d, r_d = 0, (len(diskmap)-1)//2
r_size = int(diskmap[r])
r_b = r_size-1
while l <= r:
    if l%2 == 0:
        # file
        l_size = int(diskmap[l])
        for l_b in range(l_size):
            if "test" in filepath:
                print(f"L: {l_d} * {l//2}  --  {l=} {r=}")
            checksum += l_d * (l//2)
            l_d += 1
            if l == r and l_b == r_b: break
    else:
        # free space
        l_size = int(diskmap[l])
        for l_b in range(l_size):
            if "test" in filepath:
                print(f"R: {l_d} * {r//2}  --  {l=} {r=}  {l_b=} {r_b=}")
            checksum += l_d * (r//2)
            r_b -= 1
            if r_b < 0:
                r -= 2
                r_size = int(diskmap[r])
                r_b = r_size-1
            l_d += 1
    l += 1

print(checksum)

