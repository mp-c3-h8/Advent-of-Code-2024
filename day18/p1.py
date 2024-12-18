from itertools import product
import networkx as nx
from networkx import shortest_path_length

data = open("input.txt").read().splitlines()
DIMY, DIMX = 71, 71
DG = nx.Graph()
SOURCE = 0
TARGET = DIMX-1 + (DIMY-1) * 1j

rocks = {x + y*1j for i, line in enumerate(data)
         for x, y in [map(int, line.split(","))] if i < 1024}

for z in (x + y*1j for x, y in product(range(DIMX), range(DIMY))):
    if z in rocks:
        continue
    for dz in [1j, -1, -1j, 1]:
        neighbor = z+dz
        if neighbor not in rocks:
            DG.add_edge(z, neighbor)

print(shortest_path_length(DG, SOURCE, TARGET))
