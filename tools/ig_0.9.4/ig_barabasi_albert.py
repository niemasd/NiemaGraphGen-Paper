#!/usr/bin/env python3
from igraph import Graph
from sys import argv, stderr
try:
    n = int(argv[1])
    m = int(argv[2])
except:
    print("USAGE: %s <num_nodes> <num_edges_from_new>" % argv[0], file=stderr); exit(1)
g = Graph.Barabasi(n, m)
for node in range(g.vcount()):
    print("NODE\t%s\t." % node)
for edge in g.es:
    print("EDGE\t%s\t%s\t.\tu" % (edge.source, edge.target))
