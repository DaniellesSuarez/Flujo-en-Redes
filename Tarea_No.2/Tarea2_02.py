import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()  #Se crea un grafo vacio

G.add_node(1) #Se crea el nodo raíz
G.add_nodes_from([2,3,4])

G.add_edges_from([(1,2),(2,3),(3,4),(2,2),(4,1),(2,4)])

color_map=[]
for node in G:
    if (node==2):
        color_map.append('blue')
    else:
        color_map.append('green')

nx.draw(G,pos=nx.kamada_kawai_layout(G),node_color=color_map,with_labels=True) #Se dibuja el grafo
plt.savefig("Tarea2_02.eps")
plt.show() #Se dibuja en pantalla