import pulp as pl
import networkx as nx
import cplex

G = nx.Graph()
G.add_node(1)
G.add_node(2)
G.add_node(3)
G.add_edge(1,2)
G.add_edge(2,3)
G.add_edge(3,1)

#requires Un graphe networkx
#ensures
def PLNE_CPM(G):
    # Problème de minimisation
    Lp_prob = pl.LpProblem('PLNE_CPM', pl.LpMinimize)

    # Variables utiles au problème
    E = list(G.edges) #E_G : ensemble des arêtes de G
    V = list(G.nodes) #V_G : ensemble des sommets de G

    Gd = G.to_directed() #G' : Version orienté du graphe G
    Ep = list(Gd.edges) #E'_G : ensemble des arcs de G'

    V_s = V[1:] #V_G\{s} (On choisit comme premier noeud la source)

    #Variables du problème
    lyv = pl.LpVariable.dicts("y",V,lowBound=0,upBound=1,cat=pl.LpBinary) # Contrainte 24
    lxuv = pl.LpVariable.dicts("x",Ep,lowBound=0,upBound=1,cat=pl.LpBinary) # Contrainte 25
    s = V[0]

    # Objectif
    Lp_prob += sum(lyv) #Contrainte 17

    #Contraintes 18
    Elist = []
    for v in V_s:
        for u in Gd.in_edges(v): #u est un arc
            Elist.append(u)
        Lp_prob += pl.lpSum(pl.LpVariable.dicts("A_moins",Elist,lowBound=0,upBound=1,cat=pl.LpBinary)) == 1
        Elist = []

    #Contrainte 19
    for v in V_s:
        for u in Gd.out_edges(v): #u est un arc
            Elist.append(u)

    # k va de 1 à n-1
    # Contrainte 20
    Elist2 = []
    for v in V_s:
        for (s,v) in Gd.out_edges(s): #u est un arc
            Elist.append(u)
        for (v,s) in Gd.in_edges(s):
            Elist2.append(u)
        Lp_prob += pl.lpSum(pl.LpVariable.dicts("A_moins",Elist,lowBound=0,upBound=1,cat=pl.LpBinary)) - pl.lpSum(pl.LpVariable.dicts("A_moins",Elist2,lowBound=0,upBound=1,cat=pl.LpBinary)) == 1

    # Contrainte 21

    # Contrainte 22

    # Contrainte 23

    print(Lp_prob)
    Lp_prob.solve()

PLNE_CPM(G)

#requies Un graphe networkx
#ensures


