import networkx as nx
from networkx.algorithms.flow import dinitz
import matplotlib.pyplot as plt
import numpy as np
import random
import time
import heapq
import pandas as pd
import seaborn as sns

from scipy import stats

df1=pd.DataFrame()
df2=pd.DataFrame()
df3=pd.DataFrame()
df4=pd.DataFrame()
df5=pd.DataFrame()
df6=pd.DataFrame()

G = nx.complete_graph(10)
#G = nx.lollipop_graph(10, 1)
#G = nx.full_rary_tree(3, 50)
#G = nx.circular_ladder_graph(15)

weights = np.random.normal(4, 2.3, nx.number_of_edges(G))
m = 0
for t, s, p in G.edges(data=True):
    p['weight'] = weights[m]
    m += 1

st_list = []

for i in range(5):
    for j in range(1, 2):
        list_random_G = random.sample(range(len(G)), 2)
        for k in range(1, 2):
            value_dinitz = dinitz(G, list_random_G[0], list_random_G[1], capacity="weight")
            print("Fuente", list_random_G[0])
            print("Sumidero", list_random_G[1])
            nodos_fuente=[]
            nodos_fuente.append(list_random_G[0])
            print(nodos_fuente)
            nodos_sumidero = []
            nodos_sumidero.append(list_random_G[1])
            print(nodos_sumidero)

            color_map = []
            node_T = []
            for node in G:
                if node == list_random_G[0]:
                    color_map.append('royalblue')
                    node_T.append(500)
                else:
                    if node == list_random_G[1]:
                        color_map.append('darkblue')
                        node_T.append(500)
                    else:
                        color_map.append('springgreen')
                        node_T.append(150)

    max_flujo, max_dic = nx.maximum_flow(G, list_random_G[0], list_random_G[1], capacity='weight')
    print("Diccionario", max_dic)
    print("Flujo Maximo", max_flujo)
    edge_colors = ['black' if max_dic[i][j] == 0 and max_dic[j][i] == 0 else 'red' for i, j in G.edges]

    pos = nx.random_layout(G)

    #nx.draw(G, node_color=color_map, edge_color=edge_colors, node_size=node_T,width=weights, with_labels=True) #Se dibuja el grafo
    #plt.savefig("Tarea5_01.eps")
    #plt.show() #Se dibuja en pantalla

    fv_targets = {}
    for t in range(len(G)):
        if list_random_G[0] != t:

            #degree distribution
            st1 = time.time()
            flow_value = nx.maximum_flow_value(G, list_random_G[0], t, capacity='weight')
            fv_targets[t]=flow_value
            for c in range(30):
                for dd in range(300):
                    degree_distribution = nx.degree_centrality(G)
                e1 = time.time()
                execution_t1 = e1 - st1

                row = pd.DataFrame({'Structural_Characteristic': ['Degree Distribution'],
                                    'Instance': k,
                                    'Target Node': t,
                                    'Time': execution_t1,
                                    'Objective Value': flow_value})
                df1 = df1.append(row)

            #clustering coefficient
            st2 = time.time()
            for c in range(30):
                for clu in range(300):
                    clustering_coefficient = nx.clustering(G)
                e2 = time.time()
                execution_t2 = e2 - st2

                row = pd.DataFrame({'Structural_Characteristic': ['Clustering Coefficient'],
                                    'Instance': k,
                                    'Target Node': t,
                                    'Time': execution_t2,
                                    'Objective Value': flow_value})
                df2 = df2.append(row)

            #closeness centrality
            st3 = time.time()
            for c in range(30):
                for clo in range(300):
                    closeness_centrality = nx.closeness_centrality(G)
                e3 = time.time()
                execution_t3 = e3 - st3

                row = pd.DataFrame({'Structural_Characteristic': ['Clustering Coefficient'],
                                    'Instance': k,
                                    'Target Node': t,
                                    'Time': execution_t3,
                                    'Objective Value': flow_value})
                df3=df3.append(row)

            #load centrality
            st4 = time.time()
            for c in range(30):
                for lc in range(300):
                    load_centrality = nx.load_centrality(G)
                e4 = time.time()
                execution_t4 = e4 - st4
                row = pd.DataFrame({'Structural_Characteristic': ['Clustering Coefficient'],
                                    'Instance': k,
                                    'Target Node': t,
                                    'Time': execution_t4,
                                    'Objective Value': flow_value})
                df4 = df4.append(row)

            #eccentricity
            st5 = time.time()
            for c in range(30):
                for e in range(300):
                    eccentricity = nx.eccentricity(G)
                e5 = time.time()
                execution_t5 = e5 - st5
                row = pd.DataFrame({'Structural_Characteristic': ['Clustering Coefficient'],
                                    'Instance': k,
                                    'Target Node': t,
                                    'Time': execution_t5,
                                    'Objective Value': flow_value})
                df5=df5.append(row)

            #pagerank
            st6 = time.time()
            for c in range(30):
                for pr in range(300):
                    page_rank = nx.pagerank(G, alpha=0.95)
                e6 = time.time()
                execution_t6 = e6 - st6

                row = pd.DataFrame({'Structural_Characteristic': ['Clustering Coefficient'],
                                    'Instance': k,
                                   'Target Node': t,
                                   'Time': execution_t6,
                                   'Objective Value': flow_value})
                df6 = df6.append(row)

    bt=heapq.nlargest(3, fv_targets, key=fv_targets.get)
    print('The best targets are:',bt)

    # Analysis of good sources:
    fv_sources = {}
    for s in range(len(G)):
        if s != list_random_G[1]:
            fv = nx.maximum_flow_value(G, s, list_random_G[1], capacity='weight')
            fv_sources[s] = fv

    bs = heapq.nlargest(3, fv_sources, key=fv_sources.get)
    print('The best sources are:', bs)

print(df2)

v1 = sns.violinplot('Target Node', 'Time', data=df1)
plt.show()

v2 = sns.violinplot('Target Node', 'Time', data=df2)
plt.show()

v3 = sns.violinplot('Target Node', 'Time', data=df3)
plt.show()









'''
    fv_targets = {}
    for t in range(len(G)):
        if list_random_G[0] != t:
            print(list_random_G[0], t)
            flow_value = nx.maximum_flow_value(G, list_random_G[0], t, capacity='weight')
            fv_targets[t] = flow_value

    print(fv_targets)
    #best_target = max(fv_targets.items(), key=operator.itemgetter(1))[0]
    best_target = heapq.nlargest(3, fv_targets, key=fv_targets.get)
    print(best_target)

    # Analysis of good source:
    fv_sources = {}
    for s in range(len(G)):
        if s != list_random_G[0]:
            print(s, list_random_G[0])
            fv = nx.maximum_flow_value(G, s, list_random_G[0], capacity='weight')
            fv_sources[s] = fv

    print(fv_sources)
    #best_source = max(fv_sources.items(), key=operator.itemgetter(1))[0]
    best_source = heapq.nlargest(3, fv_sources, key=fv_sources.get)
    print(best_source)


    st1 = time.time()
    for dd in range(300):
        degree_distribution = nx.degree(G)
    e1 = time.time()
    execution_t1 = e1 - st1
    # degree_time.append(execution_t1)


    row = pd.DataFrame({'Structural_Characteristic': ['Degree Distribution'],
                        'Time': execution_t1,
                        'Objective Value': fv})
    all_data = all_data.append(row)

    #h_degree = sns.distplot(row)
    plt.xlabel("Computation Time")
    plt.ylabel("Frequency")
    plt.show()
    plt.savefig("histogram_degree_time.eps")


    time2 = time.time()
    for clu in range(300):
        clustering_coefficient = nx.clustering(G)
    e2 = time.time()
    execution_t2 = e2 - time2
    clustering_time.append(execution_t2)


    st3 = time.time()
    for clo in range(300):
        closeness_centrality = nx.closeness_centrality(G)
    e3 = time.time()
    execution_t3 = e3 - st3
    closeness_time.append(execution_t3)


    st4 = time.time()
    for lc in range(400):
        load_centrality = nx.load_centrality(G)
    e4 = time.time()
    execution_t4 = e4 - st4
    load_time.append(execution_t4)


    st5 = time.time()
    for e in range(400):
        eccentricity = nx.eccentricity(G)
    e5 = time.time()
    execution_t5 = e5 - st5
    eccentricity_time.append(execution_t5)


    st6 = time.time()
    for pr in range(300):
        page_rank = nx.pagerank(G, alpha=0.95)
    e6 = time.time()
    execution_t6 = e6 - st6
    pagerank_time.append(execution_t6)


_clu = sns.distplot(clustering_time)
plt.xlabel("Computation Time")
plt.ylabel("Frequency")
plt.show()
plt.savefig("histogram_clustering_time.eps")

h_close = sns.distplot(closeness_time)
plt.xlabel("Computation Time")
plt.ylabel("Frequency")
plt.show()
plt.savefig("histogram_closeness_time.eps")

h_load = sns.distplot(load_time)
plt.xlabel("Computation Time")
plt.ylabel("Frequency")
plt.show()
plt.savefig("histogram_load_time.eps")

h_ecc = sns.distplot(eccentricity_time)
plt.xlabel("Computation Time")
plt.ylabel("Frequency")
plt.show()
plt.savefig("histogram_eccentricity.eps")

h_ecc = sns.distplot(pagerank_time)
plt.xlabel("Computation Time")
plt.ylabel("Frequency")
plt.show()
plt.savefig("pagerank_time.eps")


    print("Probando", max_dic[2])
    print("Probando1", max_dic.get(2))
    print("Probando2", max_dic[2][0])


    for key in max_dic:
        print(key, ":", max_dic[key])


    for key, value in max_dic.items():
        if max_dic[key] != 0:
            #print("Value", key, value)

'''