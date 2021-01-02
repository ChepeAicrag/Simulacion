"""
Este algoritmo selecciona aleatoriamente los nodos seed
"""
import random
from statistics import mode

def random_heruistic(g, k, p=.01, mc = 1000):
    s_tmp = {}
    c_dir = {}
    for i in range(mc):
        a = random.sample(g.nodes(), k)
        p_s = list(s_tmp.values())
        if a not in p_s:
            s_tmp[i] = a
        else:
            index = p_s.index(a)
            c_dir[index] = c_dir.get(index, 0) + 1
    i_key = None
    big_value = None                
    for key, value in c_dir.items() :
        if i_key is None or value > big_value : 
            i_key = key
            big_value = value
    return p_s[i_key]  