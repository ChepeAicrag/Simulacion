import numpy as np
from copy import deepcopy
from random import random

"""
Independiente Cascade
El método CI propuesto por Favliano y Hernan
"""
"""
Aplicado a un Grafo de igraph
"""
def independient_cascade(g, S, p=0.5, mc=1000):
    # Loop over the Monte-Carlo Simulations
    propagacion = []
    for i in range(mc):
        # Simulate propagation process
        new_active, A = S[:], S[:]
        while new_active:
            # For each newly active node, find its neighbors that become activated
            new_ones = []
            for node in new_active:
                # Determine neighbors that become infected
                np.random.seed(i)
                success = np.random.uniform(
                    0, 1, len(g.neighbors(node, mode="out"))) < p
                new_ones += list(np.extract(success,
                                            g.neighbors(node, mode="out")))
            new_active = list(set(new_ones) - set(A))
            # Add newly activated nodes to the set of activated nodes
            A += new_active
        propagacion.append(len(A))
    return np.mean(propagacion)

''' Runs independent cascade model.
Input: G -- networkx graph object
S -- initial set of vertices
p -- propagation probability
Output: T -- resulted influenced set of vertices (including S)
'''
def independient_cascade_2 (G, S, p = .01):
    T = deepcopy(S) # copy already selected nodes
    i = 0
    while i < len(T):
        for v in G[T[i]]: # for neighbors of a selected node
            if v not in T: # if it wasn't selected yet
                w = G[T[i]][v]['weight'] # count the number of edges between two nodes
                if random() <= 1 - ( 1 - p ) ** w: # if at least one of edges propagate influence
                    T.append(v)
        i += 1
    return T