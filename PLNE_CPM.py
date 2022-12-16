import pulp as pl
import networkx as nx

path_to_cplex = "/opt/ibm/ILOG/CPLEX_Studio221/cplex/bin/x86-64_linux/cplex"
solver = pl.CPLEX(path=path_to_cplex)

G = nx.empty_graph()
G.add_node(1)
G.add_node(2)
G.add_node(3)
G.add_node(4)
G.add_node(5)
G.add_node(6)
G.add_edge(1,2)
G.add_edge(1,4)
G.add_edge(1,5)
G.add_edge(2,4)
G.add_edge(2,5)
G.add_edge(3,5)
G.add_edge(3,6)
G.add_edge(4,5)
G.add_edge(5,6)

# requires Un graphe networkx
# ensures Un arbre couvrant de poids minimum
def plne_cpm(G):
    # Problème de minimisation
    prob = pl.LpProblem('plne_cpm', pl.LpMinimize)

    # Variables utiles au problème
    E = list(G.edges)  # E_G : ensemble des arêtes de G
    V = list(G.nodes)  # V_G : ensemble des sommets de G

    Gd = G.to_directed()  # G' : Version orienté du graphe G
    Ep = list(Gd.edges)  # E'_G : ensemble des arcs de G'

    V_s = V[1:]  # V_G\{s} (On choisit comme premier noeud la source)

    # listes utilisées pour stocker les éléments des contraintes
    elist = []
    elist2 = []

    # Variables du problème
    lyv = pl.LpVariable.dicts("y", V, cat=pl.LpBinary)  # Contrainte 24
    lxuv = pl.LpVariable.dicts("x", Ep, cat=pl.LpBinary)  # Contrainte 25
    # Contrainte 26
    for k in V:
        for (u, v) in E:
            elist.append((u, v, k))
            elist.append((v, u, k))
    f = pl.LpVariable.dicts("f", elist, lowBound=0, upBound=len(V) - 1)
    elist = []

    s = V[0]

    # Objectif
    prob += pl.lpSum(lyv)  # Contrainte 17

    # Contraintes 18
    for v in V_s:
        for (u,vp) in Gd.in_edges(v):  # u est un arc
            if vp == v:
                elist.append(lxuv[(u,vp)])
        prob += pl.lpSum(pl.LpVariable.dicts("A_moins_18", elist)) == 1
        elist = []

    # Contrainte 19
    for k in V:
        for v in V_s:  # v est un sommet
            if v != k:
                for (vp, u) in Gd.out_edges(v):
                    if vp == v:
                        elist.append(f[(v, u, k)])
                for (u, vp) in Gd.in_edges(v):
                    if vp == v:
                        elist2.append(f[(u, v, k)])
                prob += pl.lpSum(pl.LpVariable.dicts("A_plus_19", elist)) - pl.lpSum(
                    pl.LpVariable.dicts("A_moins_19", elist2)) == 0
                elist = []
                elist2 = []

    # k va de 1 à n-1
    # Contrainte 20
    for k in V_s:
        for (sp, v) in Gd.out_edges(s):
            if sp == s:
                elist.append(f[(s, v, k)])
        for (v, sp) in Gd.in_edges(s):
            if sp == s:
                elist2.append(f[(v, s, k)])
        prob += pl.lpSum(pl.LpVariable.dicts("A_plus_20", elist)) - pl.lpSum(
            pl.LpVariable.dicts("A_moins_20", elist2)) == 1
        elist = []
        elist2 = []

    # Contrainte 21
    for k in V_s:
        for (kp, u) in Gd.out_edges(k):
            if k == kp:
                elist.append(f[(k, u, k)])
        for (i, kp) in Gd.in_edges(k):
            if k == kp:
                elist2.append(f[(i, k, k)])
            prob += pl.lpSum(pl.LpVariable.dicts("A_plus_21", elist)) - pl.lpSum(
                pl.LpVariable.dicts("A_moins_21", elist2)) == -1
            elist = []
            elist2 = []

    # Contrainte 22
    for k in V:
        for (u, v) in Ep:
            prob += f[(u, v, k)] <= lxuv[(u, v)]

    # Contrainte 23
    for v in V:
        for (vp, u) in Gd.out_edges(v):
            if vp == v:
                elist.append(lxuv[(v, u)])
        for (u, vp) in Gd.in_edges(v):
            if vp == v:
                elist2.append(lxuv[(u, v)])
        prob += pl.lpSum(pl.LpVariable.dicts("A_plus_23", elist)) + pl.lpSum(
            pl.LpVariable.dicts("A_moins_23", elist2)) - 2 <= G.degree(v)
        elist = []
        elist2 = []

    #print(prob)
    sol = prob.solve(solver)

# requires Un graphe networkx
# ensures Un arbre couvrant de poids minimum
def plne_cpm_heuristique(G):
    # Problème de minimisation
    prob = pl.LpProblem('plne_cpm', pl.LpMinimize)

    # Variables utiles au problème
    E = list(G.edges)  # E_G : ensemble des arêtes de G
    V = list(G.nodes)  # V_G : ensemble des sommets de G

    Gd = G.to_directed()  # G' : Version orienté du graphe G
    Ep = list(Gd.edges)  # E'_G : ensemble des arcs de G'

    V_s = V[1:]  # V_G\{s} (On choisit comme premier noeud la source)

    # listes utilisées pour stocker les éléments des contraintes
    elist = []
    elist2 = []

    # Variables du problème
    lyv = pl.LpVariable.dicts("y", V, cat=pl.LpBinary)  # Contrainte 24
    lxuv = pl.LpVariable.dicts("x", Ep, cat=pl.LpBinary)  # Contrainte 25
    # Contrainte 26
    for k in V:
        for (u, v) in E:
            elist.append((u, v, k))
            elist.append((v, u, k))
    f = pl.LpVariable.dicts("f", elist, lowBound=0, upBound=len(V) - 1)
    elist = []

    s = V[0]

    # Objectif
    prob += pl.lpSum(lyv)  # Contrainte 17

    # Contraintes 18
    for v in V_s:
        for (u,vp) in Gd.in_edges(v):  # u est un arc
            if vp == v:
                elist.append(lxuv[(u,vp)])
        prob += pl.lpSum(pl.LpVariable.dicts("A_moins_18", elist)) == 1
        elist = []

    # Contrainte 19
    for k in V:
        for v in V_s:  # v est un sommet
            if v != k:
                for (vp, u) in Gd.out_edges(v):
                    if vp == v:
                        elist.append(f[(v, u, k)])
                for (u, vp) in Gd.in_edges(v):
                    if vp == v:
                        elist2.append(f[(u, v, k)])
                prob += pl.lpSum(pl.LpVariable.dicts("A_plus_19", elist)) - pl.lpSum(
                    pl.LpVariable.dicts("A_moins_19", elist2)) == 0
                elist = []
                elist2 = []

    # k va de 1 à n-1
    # Contrainte 20
    for k in V_s:
        for (sp, v) in Gd.out_edges(s):
            if sp == s:
                elist.append(f[(s, v, k)])
        for (v, sp) in Gd.in_edges(s):
            if sp == s:
                elist2.append(f[(v, s, k)])
        prob += pl.lpSum(pl.LpVariable.dicts("A_plus_20", elist)) - pl.lpSum(
            pl.LpVariable.dicts("A_moins_20", elist2)) == 1
        elist = []
        elist2 = []

    # Contrainte 21
    for k in V_s:
        for (kp, u) in Gd.out_edges(k):
            if k == kp:
                elist.append(f[(k, u, k)])
        for (i, kp) in Gd.in_edges(k):
            if k == kp:
                elist2.append(f[(i, k, k)])
            prob += pl.lpSum(pl.LpVariable.dicts("A_plus_21", elist)) - pl.lpSum(
                pl.LpVariable.dicts("A_moins_21", elist2)) == -1
            elist = []
            elist2 = []

    # Contrainte 22
    for k in V:
        for (u, v) in Ep:
            prob += f[(u, v, k)] <= lxuv[(u, v)]

    # Contrainte 23
    for v in V:
        for (vp, u) in Gd.out_edges(v):
            if vp == v:
                elist.append(lxuv[(v, u)])
        for (u, vp) in Gd.in_edges(v):
            if vp == v:
                elist2.append(lxuv[(u, v)])
        prob += pl.lpSum(pl.LpVariable.dicts("A_plus_23", elist)) + pl.lpSum(
            pl.LpVariable.dicts("A_moins_23", elist2)) - 2 <= G.degree(v)
        elist = []
        elist2 = []

    # Contraintes pour l'heuristique
    lx = pl.LpVariable.dicts("xh", E, cat=pl.LpBinary)
    # 1 - Récupérer toutes les bases de cycles de G
    cycles = nx.cycle_basis(G)
    # 2 - PL en cassant les bases de cycles
    prob += pl.lpSum(lx) == G.number_of_nodes() - 1
    for c in cycles:
        for (i,j) in zip(c[:-1],c[1:]):
            elist.append(lxuv[(i,j)])
        prob += pl.lpSum(pl.LpVariable.dicts("xij_in_C", elist)) <= sum(1 for cycle in c) - 1
        elist = []
        # 3 - Calculer le nombre de composantes connexes (CC)
        CC = nx.connected_components(G)
        nb_CC = sum(1 for cc in CC)
        # 4 -
        if nb_CC == 1:  # Si nb_CC = 1 on a un Arbre
            # print(prob)
            prob.solve(solver)
        else:  # Sinon ajouter toutes les arêtes de G entre les composantes connexes
            graph_list = []
            E = list(G.edges)
            for c in CC: # Créer les composantes connexes
                H = nx.subgraph(G, c)
                graph_list.append(H)
            H = nx.empty_graph
            for g in graph_list: # Fusion des composantes connexes en un seul grapge
                H = compose(H, g)
            for (i,j) in E: # Ajout des arêtes de G entre les composantes connexes
                if not nx.has_path(H, i, j):
                    H.add_edge(i,j)
            plne_cpm_heuristique(H)

plne_cpm_heuristique(G)