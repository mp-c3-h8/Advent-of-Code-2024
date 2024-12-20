from collections import defaultdict


type Coords = tuple[int, int]
grid: set[Coords] = set()
start: Coords = (0, 0)
target: Coords = (0, 0)

DIRS = (
    (-1, 0),  # ^
    (0, 1),  # >
    (1, 0),  # v
    (0, -1)  # <
)

for j, line in enumerate(open("input.txt").read().splitlines()):
    for i, val in enumerate(line):
        if val == ".":
            grid.add((j, i))
        elif val == "S":
            start = (j, i)
        elif val == "E":
            target = (j, i)
            grid.add((j, i))


def get_path() -> dict[Coords, int]:
    path: dict[Coords, int] = {start: 0}

    curry, currx = start
    length = 1
    while (curry, currx) != target:
        for dy, dx in DIRS:
            ny, nx = curry+dy, currx+dx
            if (ny, nx) in grid and (ny, nx) not in path:
                path[(ny, nx)] = length
                curry, currx = ny, nx
                length += 1
                break

    return path


def cheat_destinations(l: int):
    x = l
    for bound in range(l+1):
        for y in range(-bound, bound+1):
            yield (y, x), abs(y)+abs(x)
        x -= 1
    x = -l
    for bound in range(l):
        for y in range(-bound, bound+1):
            yield (y, x), abs(y)+abs(x)
        x += 1


path = get_path()

cheats: dict[int, set[tuple[Coords, Coords]]] = defaultdict(set)
for (curry, currx), curr_cost in path.items():
    for (cheaty, cheatx), cheatl in cheat_destinations(20):
        oy, ox = curry+cheaty, currx+cheatx
        if (oy, ox) not in grid:
            continue
        if (oy, ox) == target and curr_cost+cheatl < path[target]:
            best = path[target] + 1
        else:
            best = max((path[(oy+ny, ox+nx)] for (ny, nx) in DIRS if (oy+ny, ox+nx)
                       in path and curr_cost+cheatl+1 < path[(oy+ny, ox+nx)]), default=False)
        if best:
            saved = best - curr_cost - cheatl-1
            cheats[saved].add(((currx, curry), (oy, ox)))

res = 0
for saved, c in cheats.items():
    if saved >= 100:
        res += len(c)
        #print(len(c),"mal",saved,"picos")

print("Part 2:", res)

# for p in cheat_destinations(1):
#     print(p)
