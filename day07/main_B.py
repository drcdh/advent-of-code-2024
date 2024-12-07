
filepath = "input"
#filepath = "test"

input = []

with open(filepath, "r") as f:
    for line in f.readlines():
        test_val, line = line.split(": ")
        test_val = int(test_val)
        nums = list(map(int, line.split(" ")))
        input.append((test_val, nums))

def check(test_val, numbers, val=None, ops=None):
    if not numbers:
        if val == test_val:
            if filepath == "test":
                print(test_val, ops)
            return test_val
        else:
            return 0
    if val is None:
        return check(test_val, numbers[1:], numbers[0], [])
    return max(
        check(test_val, numbers[1:], val + numbers[0], ops+["+"]),
        check(test_val, numbers[1:], val * numbers[0], ops+["*"]),
        check(test_val, numbers[1:], int(str(val) + str(numbers[0])), ops+["||"]),
    )

result = sum(
    check(*_input) for _input in input
)

print(result)

