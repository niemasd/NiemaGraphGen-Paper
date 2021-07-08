#!/usr/bin/env python3
from networkx import barabasi_albert_graph
from sys import argv, stderr
try:
    n = int(argv[1])
    m = int(argv[2])
except:
    print("USAGE: %s <num_nodes> <num_edges_from_new>" % argv[0], file=stderr); exit(1)
g = barabasi_albert_graph(n, m)
for node in g.nodes:
    print("NODE\t%s\t." % node)
for edge in g.edges:
    print("EDGE\t%s\t%s\t.\tu" % edge)
