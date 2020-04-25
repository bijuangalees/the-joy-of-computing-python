# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 18:35:49 2020

@author: bijuangalees
"""

import networkx as nx
import matplotlib.pyplot as plt

G=nx.gnp_random_graph(10,0.2)
nx.draw(G)
plt.show()