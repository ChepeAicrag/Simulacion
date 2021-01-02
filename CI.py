import numpy as np
"""
Independiente Cascade
El método CI propuesto por Favliano y Hernan
"""

def independient_cascade(g, S, p=0.5, mc=1000):
    # Loop over the Monte-Carlo Simulations
    propagacion = []
    for i in range(mc):
        # Simulate propagation process
        new_active, A = S[:], S[:]
        while new_active:
            # For each newly active node, find its neighbors that become activated
            new_ones = []
            for node in new_active:
                # Determine neighbors that become infected
                np.random.seed(i)
                success = np.random.uniform(
                    0, 1, len(g.neighbors(node, mode="out"))) < p
                new_ones += list(np.extract(success,
                                            g.neighbors(node, mode="out")))
            new_active = list(set(new_ones) - set(A))
            # Add newly activated nodes to the set of activated nodes
            A += new_active
        propagacion.append(len(A))
    return np.mean(propagacion)
