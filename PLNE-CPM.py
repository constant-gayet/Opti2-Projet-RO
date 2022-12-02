import pulp as pl
import networkx as nx

G = nx.Graph()
G.add_node(1)
G.add_node(2)
G.add_node(3)
G.add_edge(1, 2)
G.add_edge(2, 3)
G.add_edge(3, 1)

path_to_cplex = "/opt/ibm/ILOG/CPLEX_Studio221/cplex/bin/x86-64_linux/cplex"
solver = pl.CPLEX(path=path_to_cplex)


# requires Un graphe networkx
# ensures
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

    s = V[0]

    # Objectif
    prob += pl.lpSum(lyv)  # Contrainte 17

    # Contraintes 18
    for v in V_s:
        for u in Gd.in_edges(v):  # u est un arc
            elist.append(u)
        prob += pl.lpSum(pl.LpVariable.dicts("A_moins_18", elist)) == 1
        elist = []

    # Contrainte 19
    for k in V:
        for v in V:  # v est un sommet
            if v != k:
                for u in V_s:  # u est un sommet
                    for (vp, up) in Gd.out_edges(v):
                        if (vp, up) == (v, u):
                            elist.append(f[(vp, up, k)])
                    for (up, vp) in Gd.in_edges(v):
                        if up != s and (up, vp) == (u, v):
                            elist2.append(f[(up, vp, k)])
                    prob += pl.lpSum(pl.LpVariable.dicts("A_plus_19", elist)) - pl.lpSum(
                        pl.LpVariable.dicts("A_moins_19", elist2)) == 0
                    elist = []
                    elist2 = []

    # k va de 1 à n-1
    # Contrainte 20
    for k in V:
        for v in V_s:  # v est un sommet
            for s in V:  # u est un sommet
                for (sp, vp) in Gd.out_edges(s):
                    if (sp, vp) == (s, v):
                        elist.append(f[(sp, vp, k)])
                for (vp, sp) in Gd.in_edges(s):
                    if (vp, sp) == (v, s):
                        elist2.append(f[(vp, sp, k)])
                prob += pl.lpSum(pl.LpVariable.dicts("A_plus_20", elist)) - pl.lpSum(
                    pl.LpVariable.dicts("A_moins_20", elist2)) == 1
                elist = []
                elist2 = []

    # Contrainte 21
    for k in V_s:
        for (kp, u) in Gd.out_edges(k):
            if k == kp:
                elist.append(f[(kp, u, kp)])
        for (i, kp) in Gd.in_edges(k):
            if k == kp:
                elist2.append(f[(i, kp, kp)])
            prob += pl.lpSum(pl.LpVariable.dicts("A_plus_21", elist)) - pl.lpSum(
                pl.LpVariable.dicts("A_moins_21", elist2)) == -1
            elist = []
            elist2 = []

    # Contrainte 22
    for k in V:
        for (u, v) in E:
            prob += f[(u, v, k)] <= lxuv[(u, v)]

    # Contrainte 23
    for v in V_s:
        for u in V:
            for (vp, up) in Gd.out_edges(v):
                if (vp, up) == (v, u):
                    elist.append(lxuv[(vp, up)])
            for (up, vp) in Gd.in_edges(v):
                if (up, vp) == (u, v):
                    elist2.append(lxuv[(up, vp)])
            prob += pl.lpSum(pl.LpVariable.dicts("A_plus_23", elist)) + pl.lpSum(
                pl.LpVariable.dicts("A_moins_23", elist2)) - 2 <= G.degree(v)
            elist = []
            elist2 = []

    print(prob)
    prob.solve(solver)


plne_cpm(G)

# requies Un graphe networkx
# ensures
