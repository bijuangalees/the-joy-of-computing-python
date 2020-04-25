# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 18:31:56 2020

@author: bijuangalees
"""

import networkx as nx
import matplotlib.pyplot as plt

G=nx.Graph()
l=[1,2,3]
G.add_nodes_from(l)
G.add_edge(1,2)
G.add_edge(2,3)
G.add_edge(1,3)
print(G.nodes)
print(G.edges)
nx.draw(G)
plt.show()