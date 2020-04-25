# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 18:33:33 2020

@author: bijuangalees
"""

import networkx as nx
import matplotlib.pyplot as plt

G=nx.complete_graph(10)
nx.draw(G)
plt.show()