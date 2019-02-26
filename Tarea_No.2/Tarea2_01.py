import networkx as nx
import matplotlib.pyplot as plt


G  = nx.DiGraph()


G.add_node("X")
G.add_nodes_from([1,2,3,4,5,6])

G.add_edges_from([("X",2),(2,4),(4,6),(6,5),(5,3),(3,1),(1,"X")])

nx.draw(G,pos=nx.circular_layout(G),with_labels= True)    # Dibuja el grafo G en forma circular
#plt.savefig("Tarea2_01.eps")
plt.show() #Se dibuja en pantalla