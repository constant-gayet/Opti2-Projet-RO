import pulp
import networkx as nx
from random import choice

path_to_cplex = "/opt/ibm/ILOG/CPLEX_Studio221/cplex/bin/x86-64_linux/cplex"
solver = pulp.CPLEX(path=path_to_cplex)

# requires Un graphe networkx
# ensures Un arbre couvrant de poids minimum
def plne_cpm(G):
    # Variables nécessaires au programme
    V = list(G.nodes)  # V_G : ensemble des sommets de G
    Gp = G.to_directed()  # G' : Version orienté du graphe G
    Ep = list(Gp.edges)  # E'_G : ensemble des arcs de G'
    s = choice(V)

    # Création du modèle de programmation linéaire
    model = pulp.LpProblem("Mon_probleme", pulp.LpMinimize)

    # Création et initialisation des variables de décision
    x = pulp.LpVariable.dicts("x", Ep, cat=pulp.LpBinary)
    y = pulp.LpVariable.dicts("y", V, cat=pulp.LpBinary)
    f = pulp.LpVariable.dicts("f", [(u, v, k) for u, v in Ep for k in V], lowBound=0, upBound=G.number_of_nodes()-1, cat=pulp.LpInteger)

    # Ajout de la fonction objectif
    model += sum(y[v] for v in V)

    # Ajout des contraintes
    for v in V :
        if v != s :
            model += sum(x[u,v] for u,v in Gp.in_edges(v)) == 1
    for k in V:
        for v in V:
            if v != k and v != s:
                model += sum(f[v,u,k] for v,u in Gp.out_edges(v)) - sum(f[u,v,k] for u,v in Gp.in_edges(v)) == 0
    for k in V:
        if k != s :
            model += sum(f[s,v,k] for s,v in Gp.out_edges(s)) - sum(f[v,s,k] for v,s in Gp.in_edges(s)) == 1
            model += sum(f[k, u, k] for k, u in Gp.out_edges(k)) - sum(f[i, k, k] for i, k in Gp.in_edges(k)) == -1
    for u,v in Ep:
        for k in V:
            model += f[u,v,k] <= x[u,v]
    for v in V:
        model += sum(x[v,u] for v,u in Gp.out_edges(v)) + sum(x[u,v] for u,v in Gp.in_edges(v)) - 2 <= G.degree(v)*y[v]

    # Résolution du modèle
    model.writeLP("./plnecpm.pl")
    model.solve(solver=solver)

    # Affichage du résultat
    # print(f"Statut de la solution: {pulp.LpStatus[model.status]}")
    # for v in V:
    #     print(f"y_{v} = {y[v].value()}")
    # for u,v in Ep:
    #     print(f"x_{u}_{v} = {x[u,v].value()}")
    # for u,v in Ep:
    #     for k in V:
    #         print(f"f_{u}_{v}_{k} = {f[u,v,k].value()}")
    return model