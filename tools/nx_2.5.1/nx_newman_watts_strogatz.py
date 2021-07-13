#!/usr/bin/env python3
from networkx import newman_watts_strogatz_graph
from sys import argv, stderr
try:
    n = int(argv[1])
    k = int(argv[2])
    p = float(argv[3])
except:
    print("USAGE: %s <num_nodes> <lattice_degree> <prob_rewire>" % argv[0], file=stderr); exit(1)
g = newman_watts_strogatz_graph(n, k, p)
for node in g.nodes:
    print("NODE\t%s\t." % node)
for edge in g.edges:
    print("EDGE\t%s\t%s\t.\tu" % edge)
