import networkx as nx
from networkx import all_shortest_paths
from networkx import shortest_path
from networkx import path_weight

data = open("input.txt").read().splitlines()
DIMY, DIMX = len(data), len(data[0])
DG = nx.DiGraph()
SOURCE = (DIMY-2, 1, 1)  # (y,x,d) with d = 1 = facing east
TARGET = (1, DIMX-2) # (y,x): we dont care what direction we are facing after reaching E

DIRS = {
    0: (-1, 0),  # ^
    1: (0, 1),  # >
    2: (1, 0),  # v
    3: (0, -1)  # <
}


def add_edges_towards_neighbor(coords: tuple[int, int], neighbor: tuple[int, int], d: int) -> None:
    # we add nodes (y,x,d) on the fly, where y: row, x: column, d \in DIRS.keys() aka direction
    # for every (y,x) we create 4 nodes (y,x,d) with d \in {0,1,2,3}
    n = neighbor+(d,) # creating 3-tupel via 2-tupel + 1-tupel
    DG.add_edge(coords+(d,), n, weight=1)
    DG.add_edge(coords+((d+1) % 4,), n, weight=1001)
    DG.add_edge(coords+((d-1) % 4,), n, weight=1001)


def add_edges_towards_target() -> None:
    ty, tx = TARGET
    if data[ty][tx-1] == ".":  # coming from west
        DG.add_edge((ty, tx-1, 0), TARGET, weight=1001)
        DG.add_edge((ty, tx-1, 1), TARGET, weight=1)
    if data[ty+1][tx] == ".":  # coming from south
        DG.add_edge((ty+1, tx, 0), TARGET, weight=1)
        DG.add_edge((ty+1, tx, 1), TARGET, weight=1001)


add_edges_towards_target()
for y, line in enumerate(data):
    for x, val in enumerate(line):
        if val in ".S":
            for d, (dy, dx) in DIRS.items():
                ny, nx = y+dy, x+dx  # coordinates of neighbor
                if data[ny][nx] == ".": # no need to check for S - we never visit S again
                    add_edges_towards_neighbor((y, x), (ny, nx), d)


s_path = shortest_path(DG, SOURCE, TARGET, weight="weight")
all_paths = all_shortest_paths(DG, SOURCE, TARGET, weight="weight")
part2 = set()
for path in all_paths:
    set.update(part2, ((y, x) for y, x, *d in path))

print("Part 1:", path_weight(DG, [*s_path], weight="weight"))
print("Part 2:", len(part2))
