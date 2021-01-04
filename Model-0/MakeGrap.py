import networkx as nx

def make_graph(ds):
    if ds == 1: 
        dg = nx.barabasi_albert_graph(63392, 13) 
    elif ds == 2:
        dg = nx.erdos_renyi_graph(n = 63392, p = 0.0004) 
    else:
        dg = nx.watts_strogatz_graph(63392, 13, 0.01)     
    return dg