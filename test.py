import networkx as nx
import matplotlib.pyplot as plt

Grafo = nx.Graph()
Grafo.add_node("A")      # add_node("n") agrega "n" como nodo del grafo
Grafo.add_node("E")
Grafo.add_node("I")
Grafo.add_edge("A","E")  # add_edge("e") agrega "e" como borde de un nodo
Grafo.add_edge("E","I")
Grafo.add_edge("I","U")

nx.draw(Grafo, with_labels = True)
plt.show(Grafo)