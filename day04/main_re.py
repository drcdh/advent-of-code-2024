# DOES NOT WORK :-c

import regex as re

filepath, W = "test", 10
filepath, W = "input", 140

with open(filepath, "r") as f:
    input = f.read()

count = 0
count += len(re.findall(r"XMAS", input))
count += len(re.findall(r"SAMX", input))
#    "XMAS",  # horizontal, left to right
#    "SAMX",  # horizontal, right to left
input = input.replace("\n", "")
patterns = [
    f"X.{{{W-1}}}M.{{{W-1}}}A.{{{W-1}}}S",  # vertical, top to bottom
    f"S.{{{W-1}}}A.{{{W-1}}}M.{{{W-1}}}X",  # vertical, bottom to top
    f"X.{{{W}}}M.{{{W}}}A.{{{W}}}S",  # diagonal, topleft to bottomright
    f"S.{{{W}}}A.{{{W}}}M.{{{W}}}X",  # diagonal, bottomright to topleft
    f"X.{{{W-2}}}M.{{{W-2}}}A.{{{W-2}}}S",  # diagonal, topright to bottomleft
    f"S.{{{W-2}}}A.{{{W-2}}}M.{{{W-2}}}X",  # diagonal, bottomleft to topright
]

count += sum([
    len(re.findall(pattern, input, overlapped=True)) for pattern in patterns
])

print(count)

