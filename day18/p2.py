from itertools import product
from networkx import shortest_path_length
from networkx import grid_2d_graph

data = open("input.txt").read().splitlines()
DIMY, DIMX = 71, 71
SOURCE = (0, 0)
TARGET = (DIMY-1, DIMX-1)

rocks = [(y, x) for line in data for x, y in [map(int, line.split(","))]]


def build_graph(number_rocks: int):
    G = grid_2d_graph(DIMY, DIMX)
    for rock in rocks[:number_rocks]:
        G.remove_node(rock)
    return G

print("Part 1:", shortest_path_length(build_graph(1024),SOURCE,TARGET))

l, r = 1024, len(rocks)-1
while r-l > 1:
    m = (l+r) // 2
    G = build_graph(m)
    try:
        shortest_path_length(G, SOURCE, TARGET)
        l = m
    except:
        r = m

print("NO WAY OUT AFTER BYTE =", r, "AT (y,x) =", rocks[r-1])