
import networkx as nx

data = open("input.txt").read().splitlines()
G = nx.Graph(line.split("-") for line in data)


res = 0
for clique in nx.enumerate_all_cliques(G):
    if len(clique) < 3:
        continue
    if len(clique) > 3:
        break
    if any(comp.startswith("t") for comp in clique):
        res += 1

print(res)
