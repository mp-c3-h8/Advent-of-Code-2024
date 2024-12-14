
from collections import defaultdict
from re import findall
from typing import Iterable
import matplotlib.pyplot as plt
import numpy as np

type Coords = tuple[int, int]
robots: list[tuple[int, int, int, int]] = []

DIMX, DIMY = 101, 103
DIR = [(1,0),(-1,0),(0,1),(0,-1),(1,1),(1,-1),(-1,1),(-1,-1)]

for line in open("input.txt").read().splitlines():
    sx, sy, vx, vy = map(int, findall(r"[-]?\d+", line))
    robots.append((sx, sy, vx, vy))


def positions_after_moving(steps: int) -> set[Coords]:
    positions = {((sy + steps*vy) % (DIMY), (sx + steps*vx) % (DIMX))
            for sx, sy, vx, vy in robots}

    return positions

def neighbors(p: Coords) -> Iterable[Coords]:
    return ((p[0]+dy,p[1]+dx) for dy,dx in DIR)

def max_connected(positions: set[Coords]) -> int:
    regions: defaultdict[int, set[Coords]] = defaultdict(set)
    done: set[Coords] = set()

    def grow(c: Coords, id: int) -> None:
        if c in done:
            return

        regions[id].add(c)
        done.add(c)

        for n in (n for n in neighbors(c) if n in positions and n not in done):
            grow(n, id)

    for i, position in enumerate(p for p in positions if p not in done):
        grow(position, i)

    return max(len(r) for r in regions.values())


def show_robots(points: set[Coords], moves: int, connected: int) -> None:
    matrix = np.zeros((DIMY, DIMX), dtype=int)
    for y, x in points:
        matrix[y][x] = 1
    plt.figure(moves)
    plt.matshow(matrix, moves)
    plt.title("Steps: " + str(moves) + " Max connected: " + str(connected))


for i in range(10_000):
    positions = positions_after_moving(i)
    m = max_connected(positions)
    if m > 20:
        show_robots(positions, i, m)

plt.show()
