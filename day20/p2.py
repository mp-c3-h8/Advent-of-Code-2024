

from typing import Iterator


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


def cheat_destinations(dist: int) -> Iterator[tuple[Coords,int]]:
    for y in range(-dist, dist+1):
        left = dist - abs(y)
        for x in range(-left, left+1):
            yield (y, x), abs(y)+abs(x)


path = get_path()

res = {2: 0, 20:0}
for (curry, currx), curr_cost in path.items():
    for n in (2,20):
        for (dy, dx), dl in cheat_destinations(n):
            ny, nx = curry+dy, currx+dx
            if (ny, nx) not in grid:
                continue
            if (ny, nx) in path and path[(ny, nx)] - curr_cost - dl >= 100:
                res[n] += 1
 
print("Part 1:", res[2])
print("Part 2:", res[20])

