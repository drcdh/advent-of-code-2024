
def is_safe(levels):
    direction = None
    for l1, l2 in zip(levels[:-1], levels[1:]):
        if l1 == l2:
            return False
        if abs(l1 - l2) > 3:
            return False
        if l1 < l2:
            # increasing
            if direction is None:
                direction = 1
            elif direction < 0:
                return False
        elif l1 > l2:
            # decreasing
            if direction is None:
                direction = -1
            elif direction > 0:
                return False
    return True

safe = 0
safe_with_dampener = 0
with open("input", "r") as f:
    for line in f.readlines():
        levels = list(map(int, line.split(" ")))
        if is_safe(levels):
            safe += 1
            safe_with_dampener += 1
        else:
            for i in range(len(levels)):
                if is_safe(levels[:i] + levels[i+1:]):
                    safe_with_dampener += 1
                    break

print(f"{safe=}")
print(f"{safe_with_dampener=}")

