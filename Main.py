from MakeGraph import *
import networkx as nx
import matplotlib.pyplot as plt
from igraph import Graph, plot
from Greedy import *
from DegreeDiscount import * 
from Aleatorio import *
from TGSSCM import *

if __name__ == "__main__":
    # Create simple network with 0 and 1 as the influential nodes
    G = read_graph()
    source = [1,1,1,3,3,4 ,5,5,6]
    target = [2,3,4,5,6,6,7,8,9]
    g = Graph(directed=True)
    size = range(10)
    g.add_vertices(size)
    g.add_edges(zip(source,target))
    A = [edge.tuple for edge in g.es]
    g2 = nx.DiGraph(A)
    
    # Plot graph
    g.vs["label"], g.es["color"], g.vs["color"] = size, "#B3CDE3", "#FBB4AE"
    plot(g,"social_network.png",bbox = (200,200),margin = 20,layout = g.layout("kk"))    

    greedy_output = greedy(g,2,p = 0.5,mc = 1000)
    tgsscm_output   = tgsscm(g,2,p = 0.2,mc = 1000)
    degree_output = degree_discount(G, 2, p = 0.01)
    greedy2_output = general_greedy(G, 2, p=0.01)
    random_output = random_heruistic(G,2, p=0.01)

    print("Greedy output: " + str(greedy_output))
    print("Greedy2 output: " + str(greedy2_output))
    print("TGSSCM output: " + str(tgsscm_output))
    # print("Greedy time: " + str(greedy_output[2]))
    print("Degree discount: " + str(degree_output))
    print("Random: " + str(random_output))