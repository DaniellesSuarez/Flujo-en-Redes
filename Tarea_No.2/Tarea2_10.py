import networkx as nx
import matplotlib.pyplot as plt

G = nx.MultiDiGraph()  #Se crea un grafo vacio

G.add_node("A") #Se crea el nodo raíz
G.add_nodes_from(["C","B","R","G"])

G.add_edges_from([("A","C"),("C","A"),("C","B"),("B","C"),("B","R"),("R","B"),("R","G")])

nx.draw(G,pos=nx.random_layout(G),with_labels=True) #Se dibuja el grafo
plt.savefig("Tarea2_10.eps")
plt.show() #Se dibuja en pantalla