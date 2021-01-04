from priorityQueue import PriorityQueue as PQ # priority queue

def single_discount(G, k, p=.1):
    S = [] # set of activated nodes
    d = PQ() # degrees
    for u in G:
        degree = sum([G[u][v]['weight'] for v in G[u]])
        d.add_task(u, -degree)
    for _ in range(k):
        u, priority = d.pop_item()
        S.append(u)
        for v in G[u]:
            if v not in S:
                [priority, count, task] = d.entry_finder[v]
                d.add_task(v, priority + G[u][v]['weight']) # discount degree by the weight of the edge
    return S