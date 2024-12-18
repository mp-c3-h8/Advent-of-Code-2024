from itertools import product
from networkx import Graph, has_path, shortest_path_length

data = open("input.txt").read().splitlines()
DIMY, DIMX = 71, 71
SOURCE = (0, 0)
TARGET = (DIMY-1, DIMX-1)

rocks = [(y, x) for line in data for x, y in [map(int, line.split(","))]]


def build_graph(number_rocks: int):
    G = Graph()
    rr = set(rocks[:number_rocks])
    for y, x in product(range(DIMY), range(DIMX)):
        if (y, x) in rr:
            continue
        for ny, nx in [(y, x+1), (y, x-1), (y+1, x), (y-1, x)]:
            if (ny, nx) not in rr:
                G.add_edge((y, x), (ny, nx))
    return G


print("Part 1:", shortest_path_length(build_graph(1024), SOURCE, TARGET))

l, r = 1024, len(rocks)
while l < r-1:
    m = (l+r) // 2
    G = build_graph(m)
    l,r = (m,r) if has_path(G, SOURCE, TARGET) else (l,m)
    
print("NO WAY OUT AFTER BYTE =", r, "AT (y,x) =", rocks[r-1])
