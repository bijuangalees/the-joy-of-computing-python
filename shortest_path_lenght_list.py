# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 19:38:15 2020

@author: bijuangalees
"""

import networkx as nx
import numpy


G=nx.read_edgelist("facebook_combined.txt")
N=list(G.nodes())

#shortest path length list
spll=[]
for u in N:
    for v in N:
        if u!=v:
            l=nx.shortest_path_length(G,u,v)
            print("shortest path between",u,"and",v,"is of length",l)
            spll.append(l)
            
min_spl=min(spll)
max_spl=max(spll)
avg_spl=numpy.average(spll)


print("Minimum shortest path length:",min_spl)
print("Maximum shortest path length:",max_spl)
print("average shortest path length:",avg_spl)
