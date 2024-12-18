from networkx import shortest_path_length
from networkx import grid_2d_graph

data = open("input.txt").read().splitlines()
DIMY, DIMX = 71, 71
SOURCE = (0, 0)
TARGET = (DIMY-1, DIMX-1)
G = grid_2d_graph(DIMY, DIMX)


for i, rock in enumerate((y, x) for line in data for x, y in [map(int, line.split(","))]):
    G.remove_node(rock)
    try:
        sp = shortest_path_length(G, SOURCE, TARGET)
        if i == 1023:
            print("Part 1:", sp)
    except:
        print("NO WAY OUT AFTER BYTE =", i+1, "AT (y,x) =", rock)
        break
