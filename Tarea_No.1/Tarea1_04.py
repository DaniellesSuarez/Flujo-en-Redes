import networkx as nx
import matplotlib.pyplot as plt

G = nx.DiGraph()  #Se crea un grafo vacio

G.add_node(1)
G.add_nodes_from([3,2,4,5])
G.add_edges_from([(1,2),(1,3),(1,5),(1,5)])
G.add_edges_from ([(2,4)])
G.add_edges_from ([(3,2),(3,5),(4,5)])
G.add_edges_from ([(4,5)])

nx.draw(G,with_labels=True) #Se dibuja el grafo
plt.savefig("Tarea1_04.eps")
plt.show() #Se dibuja en pantalla


