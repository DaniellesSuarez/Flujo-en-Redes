import networkx as nx
import matplotlib.pyplot as plt

G =nx.MultiDiGraph()

G.add_node(1)
G.add_nodes_from([2,3,4,5])
H=nx.Graph()
G.add_edges_from([(1,2),(2,1),(1,3),(4,5),(4,1)])

nx.draw(G,pos=nx.spring_layout(G),with_labels=True) #Se dibuja el grafo
plt.savefig("Tarea2_11.eps")
plt.show() #Se dibuja en pantalla