import networkx as nx
import matplotlib.pyplot as plt

G = nx.MultiGraph()  #Se crea un grafo vacio

G.add_node(1) #Se crea el nodo raíz

G.add_nodes_from([2,3,4,5,6,7,8,9])
G.add_edge(1,2,color='blue',weight=4)
G.add_edge(3,2,color='blue',weight=4)
G.add_edge(3,4,color='blue',weight=4)
G.add_edge(3,5,color='blue',weight=4)
G.add_edge(6,5,color='blue',weight=4)
G.add_edge(6,7,color='blue',weight=4)
G.add_edge(8,7,color='blue',weight=4)
G.add_edge(8,7,color='blue',weight=4)
G.add_edge(9,7,color='blue',weight=4)

G.add_edges_from([(2,1),(2,3),(4,3),(5,3),(5,6),(7,6),(7,8),(9,7)],color='red',weight=1)

edges= G.edges()

colors=[]
weight=[]

for (u,v,attrib_dict) in list(G.edges.data()):
    colors.append(attrib_dict['color'])
    weight.append(attrib_dict['weight'])

pos=nx.fruchterman_reingold_layout(G)


nx.draw(G,pos,edges=edges,edge_color=colors,width=weight,with_labels=True,font_size=8) #Se dibuja el grafo
plt.savefig("Tarea2_06.eps")
plt.show() #Se dibuja en pantalla