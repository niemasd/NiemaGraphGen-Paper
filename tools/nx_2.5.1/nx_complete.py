#!/usr/bin/env python3
from networkx import complete_graph
from sys import argv, stderr
try:
    n = int(argv[1])
except:
    print("USAGE: %s <num_nodes>" % argv[0], file=stderr); exit(1)
g = complete_graph(n)
for node in g.nodes:
    print("NODE\t%s\t." % node)
for edge in g.edges:
    print("EDGE\t%s\t%s\t.\tu" % edge)
