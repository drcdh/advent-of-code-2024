import numpy as np


filepath = "test"
filepath = "input"

_m = dict(X=1, M=2, A=3, S=4)

with open(filepath, "r") as f:
    input = np.stack([
        np.array([_m[_c] for _c in line if _c in _m], dtype=int) for line in f.readlines()])

if filepath == "test":
    print(input)

filters = [
    [[1,2,3,4]],
    [[4,3,2,1]],
    [[1],[2],[3],[4]],
    [[4],[3],[2],[1]],
    [[1,0,0,0],
     [0,2,0,0],
     [0,0,3,0],
     [0,0,0,4]],
    [[4,0,0,0],
     [0,3,0,0],
     [0,0,2,0],
     [0,0,0,1]],
    [[0,0,0,1],
     [0,0,2,0],
     [0,3,0,0],
     [4,0,0,0]],
    [[0,0,0,4],
     [0,0,3,0],
     [0,2,0,0],
     [1,0,0,0]]
]

count = 0

for i_f, filter in enumerate(filters):
    filter = np.array(filter)
    mask = (filter >= 1).astype(int)
    for i in range(input.shape[0] - mask.shape[0] + 1):
        for j in range(input.shape[1] - mask.shape[1] + 1):
            v = input[i:i+mask.shape[0],j:j+mask.shape[1]].copy()
            v *= mask
            if np.all(v == filter):
                count += 1
                if filepath == "test":
                    print(f"Filter {i_f} found at {i=} {j=}")

print(count)

