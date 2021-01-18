import numpy as np
import seaborn as sb
import matplotlib.pyplot as plt
from MakeGrap import *
from Model.GraficaComparasion import DiffusionTrendComparison
from Threshold import * 
from Profile import *
from ProfileTreshold import *
import random
import pandas as pd

def make_hm_impar(values_x, values_y, a, model, name, G):
    arr_p = []
    if_seed = 0.05
    op = 't'
    for y in values_y:
        arrtmp = []
        for x in values_x:
            print(y, x, a)
            if model == 1: 
                m3, t3 = make_t_graph_simulation(if_seed, x, y, a, G)
            else:
                op = 'y' 
                m3, t3 = make_p_graph_simulation(if_seed, x, y, a, G)
            viz = DiffusionTrendComparison([m3],[t3], plt = None)
            lol = viz.plot(filename=name)    
            arrtmp.append(max(lol))
        arr_p.append(arrtmp)
    df = pd.DataFrame(np.array(arr_p), index = values_y, columns = values_x)
    sb.heatmap(df,  annot=False,  cmap="Greens")
    print(df)
    plt.xlabel(op)
    plt.ylabel('p')
    plt.savefig(name)
    plt.show()


def make_hm_par(values_x, values_a, p, model, name, G):
    arr_p = []
    if_seed = 0.05
    op = 't'
    for a in values_a:
        arrtmp = []
        for x in values_x:
            print(a, x, p)
            if model == 1: # threshold
                m3, t3 = make_t_graph_simulation(if_seed, x, p, a, G)
            else: 
                m3, t3 = make_p_graph_simulation(if_seed, x, p, a, G)
                op = 'y'
            viz = DiffusionTrendComparison([m3],[t3], plt = None)
            lol = viz.plot(filename=name)    
            arrtmp.append(max(lol))
        arr_p.append(arrtmp)
    df = pd.DataFrame(np.array(arr_p), index = values_a, columns = values_x)
    sb.heatmap(df,  annot=False,  cmap="Greens")
    print(df)
    plt.xlabel(op)
    plt.ylabel('a')
    plt.savefig(name)
    plt.show()

def make_hm_pt(values_t, values_y, p, a, name, G):
    arr_p = []
    if_seed = 0.05
    for y in values_y:
        arrtmp = []
        for t in values_t:
            print(p, t, a, p)
            m3, t3, it = make_pt_graph_simulation(if_seed, y, t, p, a, G)
            viz = DiffusionTrendComparison([m3],[t3], plt = None)
            lol = viz.plot(filename=name)    
            arrtmp.append(max(lol))
        arr_p.append(arrtmp)
    df = pd.DataFrame(np.array(arr_p), index = values_y, columns = values_t)
    sb.heatmap(df,  annot=False,  cmap="Greens")
    print(df)
    plt.xlabel('t')
    plt.ylabel('y')
    plt.savefig(name)
    plt.show()


if  __name__ == "__main__":
    G = make_graph_db('facebook.txt', 'Facebook')

    nameT1, nameT2, nameT3, nameT4  = 'hm01.png', 'hm02.png', 'hm03.png', 'hm04.png'
    nameP1, nameP2, nameP3, nameP4  = 'hm05.png', 'hm06.png', 'hm07.png', 'hm08.png'
    nameC1, nameC2, nameC3, nameC4  = 'hm09.png', 'hm10.png', 'hm11.png', 'hm12.png'
    
    values_t = [ i/10 for i in range (1, 9)]
    values_p = [ i/10 for i in range (3, -1, -1)]
    values_y = [ 0.8, 0.7, 0.6, 0.5, 0.4, 0.3, 0.2, 0.1, 0.05]
    values_a = [0.01, 0.005, 0.001, 0.0] 

    # Threshold
    make_hm_impar(values_t, values_p, 0, 1, nameT1, G)
    make_hm_par(values_t, values_a, 0, 1, nameT2, G)
    make_hm_impar(values_t, values_p, 0.01, 1, nameT3, G)
    make_hm_par(values_t, values_a, 0.1, 1, nameT4, G)

    # Profile
    
    make_hm_impar(values_y, values_p, 0, 2, nameP1, G)
    make_hm_par(values_y, values_a, 0, 2, nameP2, G)
    make_hm_impar(values_y, values_p, 0.01, 2, nameP3, G)
    make_hm_par(values_y, values_a, 0.1, 2, nameP4, G)

    # Profile-Threshold
    make_hm_pt(values_t, values_y, 0, 0, nameC1, G)
    make_hm_pt(values_t, values_y, 0, 0.005, nameC1, G)
    make_hm_pt(values_t, values_y, 0.2, 0, nameC1, G)
    make_hm_pt(values_t, values_y, 0.2, 0.005, nameC1, G)
    


    
