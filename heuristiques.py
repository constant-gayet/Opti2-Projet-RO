import pulp
import networkx as nx

import plnecpm
import plnecp

path_to_cplex = "/opt/ibm/ILOG/CPLEX_Studio221/cplex/bin/x86-64_linux/cplex"
solver = pulp.CPLEX(path=path_to_cplex)

def remove_elem(list, item):
    new_list = [i for i in list if i != item]
    return new_list

def edge_weight_based_heuristic_aux(G,T,Ew):
    min =Ew[0]
    for ((u,v),w) in Ew:
        if w<min and not T.has_edge(u,v) :
            T.add_edge(u,v)
            G.remove_edge(u,v)
            Ew = remove_elem(Ew,((u,v),w))
            for (u2,v2)in E:
                if (u2==u or u2==v or v2==u or v2==v) :
                    Ew[(u2,v2),w2] = Ew[(u2,v2),w2+1] # On augmente le poids des arêtes incidents à u ou à v
    if T.number_of_nodes() == G.number_of_nodes()-1 :
        return
    edge_weight_based_heuristic_aux(G,T,Ew)

def edge_weight_based_heuristic(G, model):
    T = nx.empty_graph() # L'arbre T que nous allons remplir
    E = list(G.edges) # E_G : ensemble des arêtes de G
    Ew = [] # Liste de tuple contenant les arêtes de G et leur poids
    for e in E:
        Ew.append(e,1) # Toutes les arêtes commencent avec un poids de 1
    edge_weight_based_heuristic_aux(G,T,Ew)



