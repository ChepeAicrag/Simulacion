import networkx as nx
import sqlite3
from Database import * 

def make_graph(ds):
    if ds == 1: 
        dg = nx.barabasi_albert_graph(63392, 13) 
    elif ds == 2:
        dg = nx.erdos_renyi_graph(n = 63392, p = 0.0004) 
    else:
        dg = nx.watts_strogatz_graph(63392, 13, 0.01)     
    return dg

def make_graph_db(nameFile, table):
    if not load_data_in_db(nameFile, table):
        print("No se ha podido cargar los datos")
        return None
    conn = sqlite3.connect('spider.sqlite')
    cur = conn.cursor()
    cur.execute('''SELECT from_node_id, to_node_id FROM ''' + table)
    G = nx.DiGraph()
    #G.add_weighted_edges_from(cur.fetchall())
    G.add_edges_from(cur.fetchall())
    return G