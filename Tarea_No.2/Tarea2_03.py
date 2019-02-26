import networkx as nx
import matplotlib.pyplot as plt

G = nx.MultiGraph()  #Se crea un grafo vacio

G.add_node("A") #Se crea el nodo raíz
G.add_nodes_from(["B","C","D","E"])

G.add_edge("B","C", color='red',weight=6)
G.add_edges_from([("A","B"),("B","C"),("C","D"),("D","E")],color='blue',weight=2)

edges = G.edges()

colors = []
weight = []

for (u,v,attrib_dict) in list(G.edges.data()):
    colors.append(attrib_dict['color'])
    weight.append(attrib_dict['weight'])

pos=nx.random_layout(G)

nx.draw(G,pos,edges=edges,edge_color=colors,width=weight,with_labels=True,font_size=8) #Se dibuja el grafo
plt.savefig("Tarea2_02.eps")
plt.show() #Se dibuja en pantalla