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








def weight_heuristic(graph):
    # Création de l'arbre de recouvrement vide
    cover_tree = nx.Graph()

    # Ajout des poids 1 à toutes les arêtes du graphe
    for u, v in graph.edges():
        graph[u][v]['weight'] = 1

    # Répéter jusqu'à ce que l'arbre de recouvrement ait |VG| - 1 arêtes
    while cover_tree.number_of_edges() < graph.number_of_nodes() - 1:
        # Sélection de l'arête {u*, v*} ayant le poids minimum
        min_edge = min(graph.edges(data=True), key=lambda x: x[2]['weight'])
        u, v, _ = min_edge

        # Si u* et v* sont dans deux composantes connexes différentes, ajouter l'arête à l'arbre de recouvrement
        if nx.node_connected_component(cover_tree, u) != nx.node_connected_component(cover_tree, v):
            cover_tree.add_edge(u, v)
            # Supprimer l'arête du graphe
            graph.remove_edge(u, v)
            # Incrémenter le poids des arêtes incidentes à u* et v* de 1
            for w in graph[u]:
                graph[u][w]['weight'] += 1
            for w in graph[v]:
                graph[v][w]['weight'] += 1

    return cover_tree

# Exemple d'utilisation de l'heuristique
# graph = nx.Graph()
# graph.add_edges_from([(1, 2), (1, 3), (2, 4), (3, 4)])
# cover_tree = weight_heuristic(graph)
# print(cover_tree.edges)  # affiche [(1, 3), (3, 4)]

def color_heuristic(graph):
    # Création de l'arbre de recouvrement vide
    cover_tree = nx.Graph()

    # Attribution de la couleur verte à chaque sommet
    for node in graph.nodes():
        graph.nodes[node]['color'] = 'V'

    # Répéter jusqu'à ce que l'arbre de recouvrement ait |VG| - 1 arêtes
    while cover_tree.number_of_edges() < graph.number_of_nodes() - 1:
        # Sélection de l'arête ayant le moins de sommets jaunes et bleus comme extrémités
        min_edge = min(graph.edges(data=True), key=lambda x: (graph.nodes[x[0]]['color'] == 'J' or graph.nodes[x[1]]['color'] == 'J', graph.nodes[x[0]]['color'] == 'B' or graph.nodes[x[1]]['color'] == 'B'))
        u, v, _ = min_edge
        cover_tree.add_edge(u, v)
        # Supprimer l'arête du graphe
        graph.remove_edge(u, v)
        # Mise à jour des couleurs des sommets
        for node in (u, v):
            if graph.degree[node] == 1:
                graph.nodes[node]['color'] = 'B'
            elif graph.degree[node] == 2:
                graph.nodes[node]['color'] = 'J'
            else:
                graph.nodes[node]['color'] = 'R'

    return cover_tree

# Exemple d'utilisation de l'heuristique
# graph = nx.Graph()
# graph.add_edges_from([(1, 2), (1, 3), (2, 3)])
# cover_tree = color_heuristic(graph)
# print(cover_tree.edges)  # affiche [(1, 2)]

def color_weight_heuristic(graph):
    # Création de l'arbre de recouvrement vide
    cover_tree = nx.Graph()

    # Attribution de la couleur verte et du poids 1 à chaque sommet
    for node in graph.nodes():
        graph.nodes[node]['color'] = 'V'
        graph.nodes[node]['weight'] = 1

    # Répéter jusqu'à ce que l'arbre de recouvrement ait |VG| - 1 arêtes
    while cover_tree.number_of_edges() < graph.number_of_nodes() - 1:
        # Sélection de l'arête ayant le poids minimum et le moins de sommets jaunes et bleus comme extrémités
        min_edge = min(graph.edges(data=True), key=lambda x: (x[2]['weight'], graph.nodes[x[0]]['color'] == 'J' or graph.nodes[x[1]]['color'] == 'J', graph.nodes[x[0]]['color'] == 'B' or graph.nodes[x[1]]['color'] == 'B'))
        u, v, _ = min_edge
        cover_tree.add_edge(u, v)
        # Supprimer l'arête du graphe
        graph.remove_edge(u, v)
        # Mise à jour des couleurs et poids des sommets
        for node in (u, v):
            graph.nodes[node]['weight'] += 1
            if graph.degree[node] == 1:
                graph.nodes[node]['color'] = 'B'
            elif graph.degree[node] == 2:
                graph.nodes[node]['color'] = 'J'
            else:
                graph.nodes[node]['color'] = 'R'

    return cover_tree

# Exemple d'utilisation de l'heuristique
# graph = nx.Graph()
# graph.add_edges_from([(1, 2), (1, 3), (2, 3)])
# cover




