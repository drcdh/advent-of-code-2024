program = [2,4,1,1,7,5,1,5,4,3,0,3,5,5,3,0]
def compiled(A):
    B, C = 0, 0
    output = []
    while A > 0:             # 3,0
        B = (A%8)            # 2,4
        B = B^1              # 1,1
        C = int(A/(1 << B))  # 7,5
        B = B^5              # 1,5
        B = B^C              # 4,3
        A = int(A/(1 << 3))  # 0,3
        output.append(B%8)   # 5,5
    return output

def octals(f, p, a8s=""):
    start = 0 if a8s else 1
    for d8 in range(start, 8):
        a8s_ = a8s + str(d8)
        A = int(a8s_, 8)
        output = f(A)
        l = len(output)
        if output == p[-l:]:
            if l == len(p):
                return A
            if (A := octals(f, p, a8s_)) is not None:
                return A

print("Part 1:", ",".join(map(str, compiled(46323429))))
print("Part 2:", octals(compiled, program))

