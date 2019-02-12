import networkx as nx
import matplotlib.pyplot as plt

G = nx.DiGraph()  #Se crea un grafo vacio

G.add_node("x")
G.add_nodes_from(["y","z","w","s","t"])
G.add_edges_from([("t","s"),("s","w"),("s","z"),("z","x"),("x","y"),("y","y")])

nx.draw(G,with_labels=True) #Se dibuja el grafo
plt.savefig("Tarea1_06.eps")
plt.show() #Se dibuja en pantalla
