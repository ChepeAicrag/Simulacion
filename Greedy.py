from random import uniform, seed
import numpy as np
import time
from igraph import *
import CI as ci
from priorityQueue import PriorityQueue as PQ

"""
Input:  graph object, number of seed nodes
Output: optimal seed set, resulting spread, time for each iteration
"""
def greedy(g, k, p = 0.1, mc = 1000):
    S, spread, timelapse, start_time = [], [], [], time.time()    
    # Find k nodes with largest marginal gain
    for _ in range(k):
        # Loop over nodes that are not yet in seed set to find biggest marginal gain
        best_spread = 0
        for j in set(range(g.vcount()))-set(S):
            # get the spread
            s = ci.independient_cascade(g, S + [j], p, mc)
            # Update the winning node and spread so far
            if s > best_spread:
                best_spread, node = s, j
        # Add the selected node to the seed set
        S.append(node)
        # Add estimated spread and elapsed time
        spread.append(best_spread)
        timelapse.append(time.time() - start_time)
    return(S,spread,timelapse)



def general_greedy(g, k, p=.01):
    ''' Finds initial seed set S using general greedy heuristic
    Input: g -- networkx graph object
    k -- number of initial nodes needed
    p -- propagation probability
    Output: S -- initial set of k nodes to propagate
    '''
    import time
    start = time.time()
    R = 20 # number of times to run Random Cascade
    S = [] # set of selected nodes
    # add node to S if achieves maximum propagation for current chosen + this node
    for i in range(k):
        s = PQ() # priority queue
        for v in g.nodes():
            if v not in S:
                s.add_task(v, 0) # initialize spread value
                for _ in range(R): # run R times Random Cascade
                    [priority, count, task] = s.entry_finder[v]
                    s.add_task(v, priority - float(len(ic(g, S + [v], p)))/R) # add normalized spread value
        _, priority = s.pop_item()
        S.append(task)
        print (i, k, time.time() - start)
    return S

def ic (g, S, p = .01):
    ''' Runs independent cascade model.
    Input: g -- networkx graph object
    S -- initial set of vertices
    p -- propagation probability
    Output: T -- resulted influenced set of vertices (including S)
    '''
    from copy import deepcopy
    from random import random
    T = deepcopy(S) # copy already selected nodes
    i = 0
    while i < len(T):
        for v in g[T[i]]: # for neighbors of a selected node
            if v not in T: # if it wasn't selected yet
                w = g[T[i]][v]['weight'] # count the number of edges between two nodes
                if random() <= 1 - (1-p)**w: # if at least one of edges propagate influence
                    print (T[i], 'influences', v)
                    T.append(v)
        i += 1
    return T