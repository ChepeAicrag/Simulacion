"""
El algoritmo Degree Discount algoritmo heuristico basado a en la centralidad de grado
"""
from priorityQueue import PriorityQueue as PQ # priority queue
from CI import * 
import math
import networkx as nx

def degree_discount(g, k, p = 0.01):
    S_out = []
    dd = PQ() # degree discount
    t = dict() # number of adjacent vertices that are in S
    d = dict() # degree of each vertex
    # initialize degree discount
    for u in g.nodes():
        d[u] = sum([g[u][v]['weight'] for v in g[u]]) # each edge adds degree 1
        # d[u] = len(g[u]) # each neighbor adds degree 1
        dd.add_task(u, -d[u]) # add degree of each node
        t[u] = 0
    # add vertices to S greedily
    for _ in range(k):
        u, priority = dd.pop_item() # extract node with maximal degree discount
        S_out.append(u)
        for v in g[u]:
            if v not in S_out:
                t[v] += g[u][v]['weight'] # increase number of selected neighbors
                priority = d[v] - 2*t[v] - (d[v] - t[v])*t[v]*p # discount of degree
                dd.add_task(v, -priority)
    return S_out


def binary_search_boundary(G, k, Tsize, targeted_size, step, p, iterations):
    # initialization for binary search
    R = iterations
    stepk = -int(math.ceil(float(step)/2))
    k += stepk
    if k not in Tsize:
        S = degree_discount(G, k, p)
        avg = 0
        for _ in range(R):
            T = degree_discount(G, S, p)
            avg += float(len(T))/R
        Tsize[k] = avg
    # check values of Tsize in between last 2 calculated steps
    while stepk != 1:
        print (k, stepk, Tsize[k])
        if Tsize[k] >= targeted_size:
            stepk = -int(math.ceil(float(abs(stepk))/2))
        else:
            stepk = int(math.ceil(float(abs(stepk))/2))
        k += stepk
        if k not in Tsize:
            S = degree_discount(G, k, p)
            avg = 0
            for _ in range(R):
                T = degree_discount(G, S, p)
                avg += float(len(T))/R
            Tsize[k] = avg
    return (S, Tsize)

''' Finds initial set of nodes to propagate in Independent Cascade model (with priority queue)
Input: G -- networkx graph object
targeted_size -- desired size of targeted set
step -- step after each to calculate spread
p -- propagation probability
R -- number of iterations to average influence spread
Output:
S -- seed set that achieves targeted_size
Tsize -- averaged targeted size for different sizes of seed set
'''
def spread_degree_discount(G, targeted_size, step=1, p=.01, iterations=200):
    Tsize = dict()
    k = 0
    Tsize[k] = 0
    R = iterations
    while Tsize[k] <= targeted_size:
        k += step
        S = degree_discount(G, k, p)
        avg = 0
        for _ in range(R):
            T = independient_cascade_2(G, S, p)
            avg += float(len(T))/R
        Tsize[k] = avg
        print (k, Tsize[k])
    # binary search for optimal solution
    return binary_search_boundary(G, k, Tsize, targeted_size, step, p, iterations)