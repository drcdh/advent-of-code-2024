import re


prog = re.compile(r"(?P<op>(mul)|(do(n\'t)?))\(((?P<x1>\d{1,3}),(?P<x2>\d{1,3}))?\)")

with open("input", "r") as f:
    stuff = f.read()
    result_A, result_B = 0, 0
    enabled = True
    for match in prog.finditer(stuff):
        if match.group("op") == "mul":
            p = int(match.group("x1")) * int(match.group("x2"))
            result_A += p
            if enabled:
                result_B += p
        elif match.group("op") == "do":
            enabled = True
        elif match.group("op") == "don't":
            enabled = False

print(f"Part A: {result_A}")
print(f"Part B: {result_B}")

