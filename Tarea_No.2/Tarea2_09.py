import networkx as nx
import matplotlib.pyplot as plt

G = nx.DiGraph()  #Se crea un grafo vacio

G.add_nodes_from(['s','x'],bipartite=0)
G.add_nodes_from(['w','z','y','t'],bipartite=1)
G.add_edges_from([('s','w'),('s','z'),('s','t'),('x','y'),('z','x')])


nx.draw(G,pos=nx.bipartite_layout(G,['s','x']),with_labels=True) #Se dibuja el grafo
plt.savefig("Tarea2_06.eps")
plt.show() #Se dibuja en pantalla

