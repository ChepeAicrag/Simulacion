# Para la creaxión de los grafos #
import sqlite3
from random import uniform, seed
import numpy as np
import networkx as nx
from igraph import Graph, plot
import CI as ci
conn = sqlite3.connect('Simulacion.db')
cur = conn.cursor()
    # cur.execute('SELECT * FROM Alumno')
    # for alumno in cur:
    #     print(alumno)

def make_graph():
    source = [0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,2,3,4,5]
    target = [2,3,4,5,6,7,8,9,2,3,4,5,6,7,8,9,6,7,8,9]
    g = Graph(directed=True)
    rango = range(20)
    g.add_vertices(rango)
    g.add_edges(zip(source,target))
    g.vs["label"], g.es["color"], g.vs["color"] = rango, "#B3CDE3", "#FBB4AE"
    plot(g,"social_network.png",bbox = (500,500),margin = 20,layout = g.layout("kk"))


def read_graph():
    '''
    Read a graph from a file that may have multiple edges between the same nodes.
    '''
    G = nx.Graph()
    with open('./test.txt') as f:
        n, m = f.readline().split()
        for line in f:
            u, v = map(int, line.split())
            try:
                G[u][v]['weight'] += 1
            except Exception:
                G.add_edge(u,v, weight=1)
    print('Built graph G')
    return G
