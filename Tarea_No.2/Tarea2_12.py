import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()  #Se crea un grafo vacio

G.add_nodes_from([1 , 2], bipartite=0)
G.add_nodes_from([3,4,5], bipartite=1)
G.add_edges_from([(1,3),(1,4),(2,4),(2,5)])

nx.draw(G,pos=nx.bipartite_layout(G,[1,2]),with_labels=True) #Se dibuja el grafo
plt.savefig("Tarea2_12.eps")
plt.show() #Se dibuja en pantalla

