import networkx as nx
from networkx import shortest_path
from networkx import path_weight

data = open("input.txt").read().splitlines()
DIMY, DIMX = len(data), len(data[0])
DG = nx.DiGraph()
SOURCE = (DIMY-2, 1, 1)
target = None

DIRS = {
    0: (-1, 0),  # ^
    1: (0, 1),  # >
    2: (1, 0),  # v
    3: (0, -1)  # <
}


def is_valid(y: int, x: int) -> bool:
    return x >= 0 and x < DIMX and y >= 0 and y < DIMY


def add_edges_towards_neighbor(node: tuple[int, int], neighbor: tuple[int, int], d: int) -> None:
    n = neighbor+(d,)
    DG.add_edge(node+(d,), n, weight=1)
    DG.add_edge(node+((d+1) % 4,), n, weight=1001)
    DG.add_edge(node+((d-1) % 4,), n, weight=1001)


def add_edges_towards_target(target: tuple[int, int]) -> None:
    ty, tx = target
    if data[ty][tx-1] == ".":  # west
        DG.add_edge((ty, tx-1, 0), target, weight=1001)
        DG.add_edge((ty, tx-1, 1), target, weight=1)
    if data[ty+1][tx] == ".":  # south
        DG.add_edge((ty+1, tx, 0), target, weight=1)
        DG.add_edge((ty+1, tx, 1), target, weight=1001)


for j, line in enumerate(data):
    for i, val in enumerate(line):
        if val == "E":
            target = (j, i)
            add_edges_towards_target(target)
            continue
        for d, (dy, dx) in DIRS.items():
            ny, nx = j+dy, i+dx
            if is_valid(ny, nx) and data[ny][nx] in ".S":
                add_edges_towards_neighbor((j, i), (ny, nx), d)

path = list(shortest_path(DG, SOURCE, target, weight="weight"))
res = path_weight(DG, path, weight="weight")
print(res)
