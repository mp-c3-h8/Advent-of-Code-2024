
from collections import Counter
from math import prod
from re import findall

DIMX, DIMY = 101, 103
MX, MY = (DIMX-1)//2, (DIMY-1)//2
STEPS = 100

quadrants = Counter()

for line in open("input.txt").read().splitlines():
    sx, sy, vx, vy = map(int, findall(r"[-]?\d+", line))
    x = (sx + STEPS*vx) % (DIMX)
    y = (sy + STEPS*vy) % (DIMY)

    if x != MX and y != MY:
        quadrants[(x < MX)+2*(y < MY)] += 1


print(prod(quadrants.values()))
