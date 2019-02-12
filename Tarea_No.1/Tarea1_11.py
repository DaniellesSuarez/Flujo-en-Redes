import networkx as nx
import matplotlib.pyplot as plt

G = nx.MultiDiGraph()  #Se crea un grafo vacio

G.add_node(1) #Se crea el nodo raíz
G.add_nodes_from([2,3,4,5])

G.add_edges_from([(1,2),(2,1),(2,3),(3,4),(4,5),(5,2)])

nx.draw(G,with_labels=True) #Se dibuja el grafo
plt.savefig("Tarea1_11.eps")
plt.show() #Se dibuja en pantalla