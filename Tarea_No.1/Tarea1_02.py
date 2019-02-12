import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()  #Se crea un grafo vacio

G.add_node(1)
G.add_nodes_from([2,3,4,5,6])
G.add_edges_from([(1,2),(1,3),(1,4),(1,5),(1,6)])
G.add_edges_from ([(2,3)])
G.add_edges_from ([(3,4)])
G.add_edges_from ([(4,5)])
G.add_edges_from ([(5,6)])
G.add_edges_from ([(6,2)])

nx.draw(G,with_labels=True) #Se dibuja el grafo
plt.savefig("Tarea1_02.eps")
plt.show() #Se dibuja en pantalla


