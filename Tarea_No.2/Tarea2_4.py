import networkx as nx
from fa2 import ForceAtlas2
import matplotlib.pyplot as plt

G = nx.Graph()

G.add_node(1)
G.add_nodes_from([2, 3, 4, 5, 6, 7, 8, 9, 10])

G.add_edges_from([(1, 10), (2, 10), (10, 3), (10, 4), (4, 5), (4, 6), (4, 7), (7, 4), (7, 8), (7, 9)])

#Este fragmento de codigo fue tomado de https://github.com/bhargavchippada/forceatlas2/blob/master/examples/forceatlas2-layout.ipynb

forceatlas2 = ForceAtlas2(

    outboundAttractionDistribution=True,
    linLogMode=False,
    adjustSizes=False,
    edgeWeightInfluence=1.0,

    jitterTolerance=1.0,
    barnesHutOptimize=True,
    barnesHutTheta=1.2,
    multiThreaded=False,

    scalingRatio=2.0,
    strongGravityMode=False,
    gravity=1.0,

    verbose=True)

positions = forceatlas2.forceatlas2_networkx_layout(G, pos=None, iterations=2000)
nx.draw_networkx_nodes(G, positions, node_size=30, with_labels=False, node_color="green", alpha=0.7)
nx.draw_networkx_edges(G, positions, edge_color="blue", alpha=0.06)
plt.axis('off')
plt.savefig("Tarea2_10.eps")
plt.show()


