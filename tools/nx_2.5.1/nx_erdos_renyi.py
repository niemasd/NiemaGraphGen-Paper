#!/usr/bin/env python3
from networkx import fast_gnp_random_graph
from sys import argv, stderr
try:
    n = int(argv[1])
    p = float(argv[2])
except:
    print("USAGE: %s <num_nodes> <prob_edge_creation>" % argv[0], file=stderr); exit(1)
g = fast_gnp_random_graph(n, p, directed=False)
for node in g.nodes:
    print("NODE\t%s\t." % node)
for edge in g.edges:
    print("EDGE\t%s\t%s\t.\tu" % edge)
