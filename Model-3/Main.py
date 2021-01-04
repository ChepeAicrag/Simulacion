from MakeGraph import *
import networkx as nx
import matplotlib.pyplot as plt
from igraph import Graph, plot
from Greedy import *
from DegreeDiscount import *
from Aleatorio import *
from TGSSCM import *
from SingleDiscount import *


if __name__ == "__main__":
    G = read_graph('email-univ.edges')
    #G = read_graph('Wiki-Vote.txt')
    nx.write_graphml(G, 'graph.graphml')  # Export NX graph to file
    number_seed = 10
    #degree_output = degree_discount(G, number_seed, p=0.01)
    
    greedy2_output = general_greedy(G, number_seed, p=0.01)
    random_output = random_heruistic(G, number_seed, p=0.01)
    singleDiscount = single_discount(G, number_seed, p=0.01)

    #print("Greedy output: " + str(greedy_output))
    print("Greedy2 output: " + str(greedy2_output))
    #print("TGSSCM output: " + str(tgsscm_output))
    # print("Greedy time: " + str(greedy_output[2]))
    #print("Degree discount: " + str(degree_output))
    print("Single Discount" + str(singleDiscount))
    print("Random: " + str(random_output))
    #print("Independiente Cascade " + str(iterations))