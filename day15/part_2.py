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
                    walls.add((2*x, y))
                elif c == "O":
                    boxes.append([2*x, y])
                elif c == "@":
                    bot = [2*x, y]
        else:
            moves += line

def blocked(p):
    for dw in (0, -1):
        if (p[0]+dw, p[1]) in walls:
            return True
    return False

def can_move(p, dx, dy, to_move=None, player=False):
    to_move = to_move or set()
    for bx in ((0, 1) if not player and dx == 0 else (0,)):
        maybe_wall = (p[0] + bx + (dx if player or dx < 0 else 2*dx), p[1] + dy)
        if blocked(maybe_wall):
            return False, to_move
        if (i_box := get_box_index((p[0] + bx + (dx if player or dx < 0 else 2*dx), p[1] + dy))) is not None:
            to_move.add(i_box)
            not_blocked, _to_move = can_move(boxes[i_box], dx, dy, to_move)
            to_move |= _to_move
            if not not_blocked:
                return False, to_move
    return True, to_move

def get_box_index(place):
    for dx in (0, -1):
        try:
            return boxes.index([place[0]+dx, place[1]])
        except:
            pass
    return None

def try_move(dx, dy):
    global bot
    not_blocked, i_moved = can_move(bot, dx, dy, player=True)
    if not_blocked:
        bot = [bot[0] + dx, bot[1] + dy]
        for ib in i_moved:
            boxes[ib] = [boxes[ib][0] + dx, boxes[ib][1] + dy]

def gps(box):
    return 100*box[1] + box[0]

def draw():
    print("  ", end="")
    for i in range(2*w):
        if i < 10:
            print(i, end="")
    print()
    draw_robot = False
    for y in range(h):
        print(f"{y:2}", end="")
        for x in range(0, 2*w):
            if (x, y) in walls or (x-1, y) in walls:
                print("#", end="")
            elif [x, y] == bot:
                print("@", end="")
            elif draw_robot:
                print("]", end="")
                draw_robot = False
            elif [x, y] in boxes:
                print("[", end="")
                draw_robot = True
            else:
                print(".", end="")
        print()
    print()

draw()

n_moves = len(moves)
for im, move in enumerate(moves, 1):
    if move == "^":
        try_move(0, -1)
    elif move == ">":
        try_move(1, 0)
    elif move == "<":
        try_move(-1, 0)
    elif move == "v":
        try_move(0, 1)

draw()

result = sum(gps(box) for box in boxes)
print(f"Part 2: {result}")

