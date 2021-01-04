import networkx as nx 
import dynetx as dn
import ndlib.models.ModelConfig as mc
import ndlib.models.dynamic as dm
from past.builtins import xrange
from ndlib.viz.mpl.TrendComparison import DiffusionTrendComparison
from ProfileTreshold import *
from Profile import *
from Threshold import * 
from MakeGrap import *

def execution(if_seed, profile, threshold, p, a, g, name):
    m1, t1, it1 = make_pt_graph_simulation(if_seed, profile, threshold, p, a, g)
    m2, t2 = make_p_graph_simulation(if_seed, profile, p, a, g)
    m3, t3 = make_t_graph_simulation(if_seed, threshold, p, a, g)
    viz = DiffusionTrendComparison([m1, m2, m3],[t1, t2, t3])
    viz.plot(filename=name)

# Graficas para Diffusion trends for the Barabasi Alberth graph
def test01():
    execution(0.05, 0.1, 0.1, 0, 0, 1, "Fig 1 a).png")
    execution(0.05, 0.4, 0.1, 0, 0, 1, "Fig 1 b).png")
    execution(0.05, 0.8, 0.1, 0, 0, 1, "Fig 1 c).png")
    execution(0.05, 0.4, 0.2, 0, 0, 1, "Fig 1 d).png")


# Graficas para Diffusion trends for the Erdós-Renyi graph
def test11(g):
    execution(0.05, 0.1, 0.1, 0, 0, g, "Fig 2 a).png")
    execution(0.05, 0.4, 0.1, 0, 0, g, "Fig 2 b).png")
    execution(0.05, 0.8, 0.1, 0, 0, g, "Fig 2 c).png")
    execution(0.05, 0.4, 0.2, 0, 0, g, "Fig 2 d).png")    

# Graficas para Diffusion trends for the Erdós-Renyi graph
def test21(g):
    execution(0.05, 0.1, 0.1, 0, 0, g, "Fig 3 a).png")
    execution(0.05, 0.4, 0.1, 0, 0, g, "Fig 3 b).png")
    execution(0.05, 0.8, 0.1, 0, 0, g, "Fig 3 c).png")
    execution(0.05, 0.4, 0.2, 0, 0, g, "Fig 3 d).png")    
    execution(0.05, 0.4, 0.3, 0, 0, g, "Fig 3 e).png")
    execution(0.05, 0.4, 0.4, 0, 0, g, "Fig 3 f).png")    

def test31(g):
    # execution(0.05, 0.1, 0.1, 0, 0, g, "Fig 4 a).png")
    # print("Figura 4 - a) Generated")
    # execution(0.05, 0.4, 0.1, 0, 0, g, "Fig 4 b).png")
    # print("Figura 4 - b) Generated")
    # execution(0.05, 0.8, 0.1, 0, 0, g, "Fig 4 c).png")
    # print("Figura 4 - c) Generated")
    # execution(0.05, 0.4, 0.2, 0, 0, g, "Fig 4 d).png")    
    # print("Figura 4 - d) Generated")
    # execution(0.05, 0.4, 0.3, 0, 0, g, "Fig 4 e).png")
    # print("Figura 4 - e) Generated")
    execution(0.05, 0.8, 0.2, 0, 0, g, "Fig 4 f).png")
    print("Figura 4 - f) Generated")
# Main


if __name__ == "__main__":
    # test01()
    # print("Figura 1 - a) Generated")
    # test02()
    # print("Figura 1 - b) Generated")
    # test03()
    # print("Figura 1 - c) Generated")
    # test04()
    # print("Figura 1 - d) Generated")

    # g = make_graph(2)
    # print("Erdós-Renyi Graph created")
    # test11(g) 
    # print("Figura 2 - a) Generated")
    # test12(g)
    # print("Figura 2 - b) Generated")
    # test13(g)
    # print("Figura 2 - c) Generated")
    # test14(g)
    # print("Figura 2 - d) Generated")
    
    # g = make_graph(3)
    # print("Wats-Strogatz Graph created")
    # test21(g) 
    # print("Figura 3 - a) Generated")
    # test22(g)
    # print("Figura 3 - b) Generated")
    # test23(g)
    # print("Figura 3 - c) Generated")
    # test24(g)
    # print("Figura 3 - d) Generated")
    # test25(g)
    # print("Figura 3 - e) Generated")
    # test26(g)
    # print("Figura 3 - f) Generated")

    # g = make_graph_db('facebook-wall.txt.anon', 'Facebook')
    g = make_graph_db('facebook.txt', 'Face')
    test31(g)
    print("Program terminated")
    