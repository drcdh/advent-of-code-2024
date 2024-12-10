from pprint import pprint

filepath = "input"
#filepath = "test"
#filepath = "test2"

top = []
trailheads = []

with open(filepath, "r") as f:
    for y, line in enumerate(f.readlines()):
        top_row = []
        for x, l in enumerate(line.strip()):
            t = int(l)
            top_row.append(t)
            if t == 0:
                trailheads.append((x, y))
        top.append(top_row)

if filepath != "input":
    pprint(top)
    print(len(trailheads))
    pprint(trailheads)

def th_score(x, y):
    if x < 0 or y < 0:
        return set(), 0
    try:
        h = top[y][x]
    except IndexError:
        return set(), 0
    if h == 9:
        return {(x, y)}, 1
    tops = set()
    rating = 0
    try:
        if top[y-1][x] == h+1:
            t, r = th_score(x, y-1)
            tops |= t
            rating += r
    except IndexError:
        pass
    try:
        if top[y+1][x] == h+1:
            t, r = th_score(x, y+1)
            tops |= t
            rating += r
    except IndexError:
        pass
    try:
        if top[y][x-1] == h+1:
            t, r = th_score(x-1, y)
            tops |= t
            rating += r
    except IndexError:
        pass
    try:
        if top[y][x+1] == h+1:
            t, r = th_score(x+1, y)
            tops |= t
            rating += r
    except IndexError:
        pass
    return tops, rating

results = [th_score(*th) for th in trailheads]
scores = [len(result[0]) for result in results]
score = sum(scores)

if filepath != "input":
    pprint(results)
    pprint(scores)

print(score)

results_2 = [result[1] for result in results]
total_rating = sum(results_2)
print(total_rating)

