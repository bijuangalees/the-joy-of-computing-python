# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 18:41:55 2020

@author: bijuangalees
"""

import networkx as nx
import matplotlib.pyplot as plt

#G=nx.Graph()
G=nx.barabasi_albert_graph(100,2)
nx.draw(G)
plt.show()
nx.write_gexf(G,"analysis3.gexf")