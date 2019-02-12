import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()  #Se crea un grafo vacio

G.add_node("Direccion") #Se crea el nodo raíz
G.add_nodes_from(["Produccion","Contabilidad","Recursos Humanos","Grupo de Trabajo"])

G.add_edges_from([("Direccion","Produccion"),("Direccion","Contabilidad"),("Direccion","Recursos Humanos")])
G.add_edges_from([("Produccion","Grupo de Trabajo")])

nx.draw(G,with_labels=True) #Se dibuja el grafo
plt.savefig("Tarea1_01.eps")
plt.show() #Se dibuja en pantalla