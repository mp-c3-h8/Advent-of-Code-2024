from math import copysign

import keyboard
import numpy as np
import matplotlib.pyplot as plt


type Coords = tuple[int, int]  # (y,x)
type Grid = list[list[str]]
grid2 = []
robot: Coords = (0, 0)

warehouse, moves = open("input.txt").read().split("\n\n")
moves = moves.replace("\n","")
warehouse = warehouse.splitlines()

for y, line in enumerate(warehouse):
    for x, n in enumerate(line):
        if n == "@":
            robot = (y, x)
    grid2.append(list(line))

grid = np.array(grid2)

DIMY, DIMX = len(warehouse), len(warehouse[0])
DIRS = {
    "^": (-1, 0),
    ">": (0, 1),
    "v": (1, 0),
    "<": (0, -1)
}


def find_free_spot(dir: Coords) -> Coords | None:
    y, x = robot
    while grid[y][x] != "#":
        if grid[y][x] == ".":
            return (y, x)
        y += dir[0]
        x += dir[1]


def move(move: str) -> None:
    global robot
    dy, dx = DIRS[move]
    if f := find_free_spot((dy, dx)):
        fy, fx = f
        ry, rx = robot
        abs_x = int(copysign(1, fx-rx))
        abs_y = int(copysign(1, fy-ry))
        if fx-rx:
            grid[ry, rx+abs_x:fx+abs_x:abs_x] = grid[ry, rx:fx:abs_x]
        elif fy-ry:
            grid[ry+abs_y:fy+abs_y:abs_y, rx] = grid[ry:fy:abs_y, rx]

        grid[robot] = "."
        robot = (ry+dy, rx+dx)


def print_move(move: str,) -> None:
    matrix = np.zeros((DIMY, DIMX), dtype=int)
    for y, row in enumerate(grid):
        for x, val in enumerate(row):
            if val == "#":
                matrix[y, x] = 0
            elif val == ".":
                matrix[y, x] = 10
            elif val == "O":
                matrix[y, x] = 8
            elif val == "@":
                matrix[y, x] = 4
    plt.figure(1, clear=True)
    plt.matshow(matrix, 1, cmap="hot")
    plt.title("Move " + move)
    plt.pause(0.01)
    plt.show()


plt.ion()
for m in moves:
    move(m)

    # print_move(m)
    # keyboard.wait("space")

res = 0
print(sum(y*100+x for (y, x), val in np.ndenumerate(grid) if val == "O"))
