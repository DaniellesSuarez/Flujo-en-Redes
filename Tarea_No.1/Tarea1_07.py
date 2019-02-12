import networkx as nx
import matplotlib.pyplot as plt

G = nx.MultiGraph()  #Se crea un grafo vacio

G.add_node("A") #Se crea el nodo raíz
G.add_nodes_from(["B","C","D","E"])

G.add_edges_from([("A","B"),("B","C"),("B","C"),("C","D"),("D","E")])

nx.draw(G,with_labels=True) #Se dibuja el grafo
plt.savefig("Tarea1_07.eps")
plt.show() #Se dibuja en pantalla