# -*- coding: utf-8 -*-
"""
Created on Sat Apr 11 15:48:16 2020

@author: bijuangalees
"""

import networkx as nx
U=nx.Graph()#undirected graph
G=nx.DiGraph()
G.nodes()
#NodeView()
G.add_nodes_from([i for i in range(5)])
G.nodes()
list(G.nodes())
G.edges
