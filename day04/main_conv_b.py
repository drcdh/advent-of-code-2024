import numpy as np


filepath = "input"

_m = dict(X=1, M=2, A=3, S=4)

with open(filepath, "r") as f:
    input = np.stack([
        np.array([_m[_c] for _c in line if _c in _m], dtype=int) for line in f.readlines()])

filters = [
    np.array([[2,0,4],
              [0,3,0],
              [2,0,4]])
]
filters.append(filters[0][:,::-1])
filters.append(filters[0].T)
filters.append(filters[0][:,::-1].T)

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

print(count)

