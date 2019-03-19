import networkx as nx
import matplotlib.pyplot as plt
import time
import numpy as np
import pandas as pd
from scipy import stats

###############################################################
hist, bin_edges = np.histogram(list_5, density=True)
first_edge, last_edge = np.min(list_5), np.max(list_5)

n_equal_bins = 10
bin_edges = np.linspace(start=first_edge, stop=last_edge, num=n_equal_bins + 1, endpoint=True)

plt.hist(list_5, bins=bin_edges, rwidth=0.75)
plt.xlabel('Tiempo Computacional')
plt.ylabel('Frecuencia')
plt.grid(axis='y', alpha=0.75)
plt.savefig("Tarea3_05.eps")
plt.show(1)

normality_test = stats.shapiro(list_5)
print(normality_test)

######################################################################

colors = ['b', 'c', 'y', 'm', 'r']

lo = plt.scatter(list_1, nodos_1, marker='x', color=colors[0])
ll = plt.scatter(list_2, nodos_2, marker='*', color=colors[4])
l  = plt.scatter(list_3, nodos_3, marker='D', color=colors[1])
a  = plt.scatter(list_4, nodos_4, marker='^', color=colors[2])
h  = plt.scatter(list_5, nodos_5, marker='o', color=colors[3])

plt.legend((lo, ll, l, a, h,),
           ('All-Pairs shortest paths', 'Betweenness Centrality', 'Topological Sort', 'Max Clique', 'DFS Tree'),
           scatterpoints=1,
           loc='upper left',
           ncol=1,
           fontsize=9)

plt.xlabel('Tiempo (segundos)')
plt.ylabel('Cantidad de nodos')
plt.savefig("Tarea3_06.eps")
plt.show(1)
