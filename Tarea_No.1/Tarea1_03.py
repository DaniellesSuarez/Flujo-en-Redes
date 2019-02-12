import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()  #Se crea un grafo vacio

G.add_node(1) #Se crea el nodo raíz
G.add_nodes_from([2,3,4])

G.add_edges_from([(1,2),(2,3),(3,4),(2,2),(4,1),(2,4)])

nx.draw(G,with_labels=True) #Se dibuja el grafo
plt.savefig("Tarea1_03.eps")
plt.show() #Se dibuja en pantalla