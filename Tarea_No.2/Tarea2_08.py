import networkx as nx
import matplotlib.pyplot as plt

G = nx.MultiDiGraph()  #Se crea un grafo vacio

G.add_node(1) #Se crea el nodo raíz
G.add_nodes_from([2,3,4,5])
G.add_edge(2,1,color='red',weight=1)
G.add_edges_from([(1,2),(2,3),(3,4),(4,5),(5,2)],color='blue',weight=3)

edges= G.edges()

colors=[]
weight=[]

for (u,v,attrib_dict) in list(G.edges.data()):
    colors.append(attrib_dict['color'])
    weight.append(attrib_dict['weight'])

nx.draw(G,pos=nx.spectral_layout(G), edges=edges,edge_color=colors,width=weight,with_labels=True,font_size=8) #Se dibuja el grafo
plt.savefig("Tarea2_07.eps")
plt.show() #Se dibuja en pantalla