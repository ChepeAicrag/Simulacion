"""
El algoritmo Degree Discount algoritmo heuristico basado a en la centralidad de grado
"""
from priorityQueue import PriorityQueue as PQ # priority queue

def degree_discount(g, k, p = 0.01):
    S = []
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
        S.append(u)
        for v in g[u]:
            if v not in S:
                t[v] += g[u][v]['weight'] # increase number of selected neighbors
                priority = d[v] - 2*t[v] - (d[v] - t[v])*t[v]*p # discount of degree
                dd.add_task(v, -priority)
    return S