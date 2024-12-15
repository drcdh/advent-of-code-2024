import sys

filepath = sys.argv[1]

walls = set()
boxes = []
bot = None

w = None
h = 0
read_map = True
moves = ""
with open(filepath, "r") as f:
    for y, line in enumerate(f.readlines()):
        line = line.strip()
        if not line:
            read_map = False
            continue
        if w is None:
            w = len(line)
        if read_map:
            h += 1
            for x, c in enumerate(line):
                if c == "#":
                    walls.add((x, y))
                elif c == "O":
                    boxes.append([x, y])
                elif c == "@":
                    bot = [x, y]
        else:
            moves += line

def try_move_box(place, dx, dy):
    if tuple(place) in walls:
        return False
    try:
        i_box = boxes.index(place)
        place = [place[0] + dx, place[1] + dy]
        if try_move_box(place, dx, dy):
            boxes[i_box][0] += dx
            boxes[i_box][1] += dy
            return True
        return False
    except ValueError:
        return True

def try_move(dx, dy):
    global bot
    place = [bot[0] + dx, bot[1] + dy]
    if try_move_box(place, dx, dy):
        bot = place

def gps(box):
    return 100*box[1] + box[0]

for move in moves:
    if move == "^":
        try_move(0, -1)
    elif move == ">":
        try_move(1, 0)
    elif move == "<":
        try_move(-1, 0)
    elif move == "v":
        try_move(0, 1)

def draw():
    for y in range(h):
        for x in range(w):
            if (x, y) in walls:
                print("#", end="")
            elif [x, y] in boxes:
                print("O", end="")
            elif [x, y] == bot:
                print("@", end="")
            else:
                print(".", end="")
        print()

draw()

result = sum(gps(box) for box in boxes)
print(f"Part 1: {result}")

