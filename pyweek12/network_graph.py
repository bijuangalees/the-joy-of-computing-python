# -*- coding: utf-8 -*-
"""
Created on Sat Apr 11 10:04:39 2020

@author: bijuangalees
"""

import networkx as nx
#G=nx.barbell_graph(5,3)
#G=nx.complete_graph(4)
#G=nx.cycle_graph(5)
#G=nx.ladder_graph(5)
#G=nx.path_graph(6)
#G=nx.star_graph(1000)
#G=nx.wheel_graph(9)
G=nx.gnp_random_graph(5,0.5)

nx.draw(G)
