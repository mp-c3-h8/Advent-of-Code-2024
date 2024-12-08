from collections import defaultdict
from dataclasses import dataclass
import itertools as it


@dataclass(unsafe_hash=True)
class p:
    x: int
    y: int


data = open("input.txt").read().splitlines()
grid = defaultdict(list[p])
nrows = len(data)
ncols = len(data[0])
antinodes = set()


def is_valid(p: p) -> bool:
    return p.x >= 0 and p.x < ncols and p.y >= 0 and p.y < nrows


def add_antinodes(p1: p, p2: p) -> None:
    candidates = [p(2*p1.x - p2.x, 2*p1.y - p2.y),
                  p(-p1.x + 2*p2.x, -p1.y + 2*p2.y)]
    # inbetweeners
    needs_div_check = [(2*p1.x + p2.x, 2*p1.y + p2.y),
                       (p1.x + 2*p2.x, p1.y + 2*p2.y)]

    for (qx,rx),(qy,ry) in ((divmod(x, 3), divmod(y, 3)) for x, y in needs_div_check):
        if rx == 0 and ry == 0:
            candidates.append(p(qx, qy))

    for c in candidates:
        if is_valid(c):
            antinodes.add(c)


for j, line in enumerate(data):
    for i, char in enumerate(line):
        if char != ".":
            grid[char].append(p(i, j))

for locs in grid.values():
    for p1, p2 in it.combinations(locs, 2):
        add_antinodes(p1, p2)

print(len(antinodes))
