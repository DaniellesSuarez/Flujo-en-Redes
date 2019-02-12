import networkx as nx
import matplotlib.pyplot as plt

G = nx.MultiDiGraph()  #Se crea un grafo vacio

G.add_node(1) #Se crea el nodo raíz
G.add_nodes_from([2,3,4,5,6,7,8,9])

G.add_edges_from([(1,2),(2,1),(2,3),(3,2),(3,4),(4,3),(3,5),(5,3),(5,6),(6,5),(6,7),(7,6),(7,8),(8,7),(7,9),(9,7)])

nx.draw(G,with_labels=True) #Se dibuja el grafo
plt.savefig("Tarea1_09.eps")
plt.show() #Se dibuja en pantalla