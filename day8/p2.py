from collections import defaultdict
import itertools as it


data = open("input.txt").read().splitlines()
grid = defaultdict(list[complex])
nrows = len(data)
ncols = len(data[0])
antinodes = set()


def is_valid(p: complex) -> bool:
    r, i = p.real, p.imag
    return r >= 0 and r < ncols and i >= 0 and i < nrows


for j, line in enumerate(data):
    for i, char in enumerate(line):
        if char != ".":
            grid[char].append(i + j*1j)

for locs in grid.values():
    for p1, p2 in it.combinations(locs, 2):
        dp = p2-p1
        while is_valid(p1):
            antinodes.add(p1)
            p1 += dp

        while is_valid(p2):
            antinodes.add(p2)
            p2 -= dp


print(len(antinodes))
