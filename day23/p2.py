
import networkx as nx

data = open("input.txt").read().splitlines()
G = nx.Graph(line.split("-") for line in data)


max_clique = max((clique for clique in nx.find_cliques(G)), key=len)  # seems to be unique

print(",".join(sorted(max_clique)))
