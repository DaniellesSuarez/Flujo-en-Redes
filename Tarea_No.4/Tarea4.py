import networkx as nx
from networkx.algorithms.flow import dinitz
from networkx.algorithms.flow import preflow_push
from networkx.algorithms.flow import shortest_augmenting_path
import matplotlib.pyplot as plt
import numpy as np
import random
from time import time
import pandas as pd
import seaborn as sns
import statsmodels.api as sm
from statsmodels.formula.api import ols

table = pd.DataFrame()

total_time_stars = []
total_time_lollipop = []
total_time_wheel = []


def ndistribution_weight(media, sigma, Gname):
    weights = np.random.normal(media, sigma, nx.number_of_edges(Gname))
    m = 0
    for t, s, p in Gname.edges(data=True):
        p['weight'] = weights[m]
        m += 1

for j in range(10):
    for i in range(2, 6):
        i = 2 ** i

        stars_time_G = time()
        G = nx.star_graph(i)
        end_time_G = time()
        total_time_G = end_time_G - stars_time_G
        total_time_stars.append(total_time_G)
        ndistribution_weight(8, 0.3, G)

        stars_time_A = time()
        A = nx.lollipop_graph(3, i)
        end_time_A = time()
        total_time_A = end_time_A - stars_time_A
        total_time_lollipop.append(total_time_A)
        ndistribution_weight(8, 0.3, A)

        stars_time_D = time()
        D = nx.wheel_graph(i)
        end_time_D = time()
        total_time_D = end_time_D - stars_time_D
        total_time_wheel.append(total_time_D)
        ndistribution_weight(8, 0.3, D)

        for r in range(5):

            for k in range(1, 6):
                list_random_G = random.sample(range(len(G)), 2)
                inicial_time_G = time()
                for s in range(1, 6):
                    value_dinitz = dinitz(G, list_random_G[0], list_random_G[1], capacity="weight")
                final_time_G = time()
                execution_time_G = final_time_G - inicial_time_G

            table1 = pd.DataFrame({'Generador': ['Star_Graph'],
                                   'Algoritmo': ['Dinitz'],
                                   'Orden': i,
                                   'Densidad': round(G.size() / nx.complete_graph(i).size(),2),
                                   'Tiempo': execution_time_G + total_time_G})
            table = table.append(table1)

            for h in range(1, 6):
                list_random_G = random.sample(range(len(G)), 2)
                inicial_time_G = time()
                for s in range(1, 6):
                    value_preflow_push = preflow_push(G, list_random_G[0], list_random_G[1], capacity="weight")
                final_time_G = time()
                execution_time_G = final_time_G - inicial_time_G

            table4 = pd.DataFrame({'Generador': ['Star_Graph'],
                                       'Algoritmo': ['Preflow_Push'],
                                       'Orden': i,
                                       'Densidad': round(G.size() / nx.complete_graph(i).size(),2),
                                       'Tiempo': execution_time_G + total_time_G})
            table = table.append(table4)

            for f in range(1, 6):
                list_random_G = random.sample(range(len(G)), 2)
                inicial_time_G = time()
                for s in range(1, 6):
                    value_shortest_augmenting_path = shortest_augmenting_path(G, list_random_G[0], list_random_G[1], capacity="weight")
                final_time_G = time()
                execution_time_G = final_time_G - inicial_time_G

            table5 = pd.DataFrame({'Generador': ['Star_Graph'],
                                       'Algoritmo': ['Shortest'],
                                       'Orden': i,
                                       'Densidad': round(G.size() / nx.complete_graph(i).size(),2),
                                       'Tiempo': execution_time_G + total_time_G})
            table = table.append(table5)

    #############################################################################################################################################

            for k in range(1, 6):
                list_random_A = random.sample(range(len(A)), 2)
                inicial_time_A = time()
                for s in range(1, 6):
                    value_dinitz = dinitz(A, list_random_A[0], list_random_A[1], capacity="weight")
                final_time_A = time()
                execution_time_A = final_time_A - inicial_time_A

            table6 = pd.DataFrame({'Generador': ['Lollipop'],
                                   'Algoritmo': ['Dinitz'],
                                   'Orden': i,
                                   'Densidad': round(A.size() / nx.complete_graph(i).size(),2),
                                   'Tiempo': execution_time_A + total_time_A})
            table = table.append(table6)

            for h in range(1, 6):
                list_random_A = random.sample(range(len(A)), 2)
                inicial_time_A = time()
                for s in range(1, 6):
                    value_preflow_push = preflow_push(A, list_random_A[0], list_random_A[1], capacity="weight")
                final_time_A = time()
                execution_time_A = final_time_A - inicial_time_A

            table2 = pd.DataFrame({'Generador': ['Lollipop'],
                                       'Algoritmo': ['Preflow_Push'],
                                       'Orden': i,
                                       'Densidad': round(A.size() / nx.complete_graph(i).size(),2),
                                       'Tiempo': execution_time_A + total_time_A})
            table = table.append(table2)

            for h in range(1, 6):
                list_random_A = random.sample(range(len(A)), 2)
                inicial_time_A = time()
                for s in range(1, 6):
                    value_preflow_push = preflow_push(A, list_random_A[0], list_random_A[1], capacity="weight")
                final_time_A = time()
                execution_time_A = final_time_A - inicial_time_A

            table7 = pd.DataFrame({'Generador': ['Lollipop'],
                                   'Algoritmo': ['Preflow_Push'],
                                   'Orden': i,
                                   'Densidad': round(A.size() / nx.complete_graph(i).size(),2),
                                   'Tiempo': execution_time_A + total_time_A})
            table = table.append(table7)

    #################################################################################################################################################
            for f in range(1, 6):
                list_random_D = random.sample(range(len(D)), 2)
                inicial_time_D = time()
                for s in range(1, 6):
                    value_shortest_augmenting_path = shortest_augmenting_path(D, list_random_D[0], list_random_D[1], capacity="weight")
                final_time_D = time()
                execution_time_D = final_time_D - inicial_time_D

            table3 = pd.DataFrame({'Generador': ['Wheel'],
                                       'Algoritmo': ['Shortest'],
                                       'Orden': i,
                                       'Densidad':round(D.size() / nx.complete_graph(i).size(),2),
                                       'Tiempo': execution_time_D + total_time_D})
            table = table.append(table3)

            for k in range(1, 6):
                list_random_D = random.sample(range(len(D)), 2)
                inicial_time_D = time()
                for s in range(1, 6):
                    value_dinitz = dinitz(D, list_random_D[0], list_random_D[1], capacity="weight")
                final_time_D = time()
                execution_time_D = final_time_D - inicial_time_D

            table8 = pd.DataFrame({'Generador': ['Wheel'],
                                   'Algoritmo': ['Dinitz'],
                                   'Orden': i,
                                   'Densidad': round(D.size() / nx.complete_graph(i).size(),2),
                                   'Tiempo': execution_time_D + total_time_D})
            table = table.append(table8)

            for h in range(1, 6):
                list_random_D = random.sample(range(len(D)), 2)
                inicial_time_D = time()
                for s in range(1, 6):
                    value_preflow_push = preflow_push(D, list_random_D[0], list_random_D[1], capacity="weight")
                final_time_D = time()
                execution_time_D = final_time_D - inicial_time_D

            table9 = pd.DataFrame({'Generador': ['Wheel'],
                                   'Algoritmo': ['Preflow_Push'],
                                   'Orden': i,
                                   'Densidad': round(D.size() / nx.complete_graph(i).size(),2),
                                   'Tiempo': execution_time_D + total_time_D})
            table = table.append(table9)

print(table)

table.to_csv('data.csv', index=False)

sns.boxplot(x = 'Generador', y = 'Tiempo', data = table)
plt.savefig("box_generador.eps")
plt.show()

sns.boxplot(x = 'Orden', y = 'Tiempo', data = table)
plt.savefig("box_orden.eps")
plt.show()

sns.boxplot(x = 'Algoritmo', y = 'Tiempo', data = table)
plt.savefig("box_algoritmo.eps")
plt.show()

sns.boxplot(x = 'Densidad', y = 'Tiempo', data = table)
plt.savefig("box_densidad.eps")
plt.show()

model = ols('Tiempo ~ Generador + Orden + Algoritmo + Densidad + Generador*Orden + Generador*Algoritmo + Generador*Densidad + Orden*Algoritmo + Orden*Densidad + Algoritmo*Densidad',\
           data= table).fit()

ANOVA = sm.stats.anova_lm(model, typ=2)
print(ANOVA)

for i in range(len(ANOVA)):
    print("{:s} {:s}is significative".format(ANOVA.index[i], "" if ANOVA['PR(>F)'][i] < 0.05 else "It is not "))

'''
mean=table.groupby('Orden',as_index=False)['Tiempo'].mean()
print(mean)
std_dev=table.groupby('Orden')['Tiempo'].std()
print(std_dev)
'''

sns.heatmap(table.corr(), square=True, annot=True)
plt.savefig("matriz_correlacion.eps")
plt.show()
