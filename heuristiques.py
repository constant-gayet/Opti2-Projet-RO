import pulp
import networkx as nx

import plnecpm
import plnecp
import utils

path_to_cplex = "/opt/ibm/ILOG/CPLEX_Studio221/cplex/bin/x86-64_linux/cplex"
solver = pulp.CPLEX(path=path_to_cplex)

def weight_heuristic(graph,file):
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
        print(u,v)
        print(cover_tree)

        # Si u* et v* sont dans deux composantes connexes différentes, ajouter l'arête à l'arbre de recouvrement
        # cependant, je ne comprends pas ici si u* et v* doivent être dans deux composantes connexes de l'arbre ou du graphe.
        # Si les composantes sont celles de l'arbre : les deux sommets n'appartiennent pas nécessairement à l'arbre
        # Si le graphe est connexe : l'algorithme boucle à l'infini.

        if nx.node_connected_component(cover_tree, u) != nx.node_connected_component(cover_tree, v):
            cover_tree.add_edge(u, v)
            # Supprimer l'arête du graphe
            graph.remove_edge(u, v)
            # Incrémenter le poids des arêtes incidentes à u* et v* de 1
            for w in graph[u]:
                graph[u][w]['weight'] += 1
            for w in graph[v]:
                graph[v][w]['weight'] += 1

    utils.result_in_txt_heuristiques(file,cover_tree)
    return cover_tree

# Exemple d'utilisation de l'heuristique
# graph = nx.Graph()
# graph.add_edges_from([(1, 2), (1, 3), (2, 4), (3, 4)])
# cover_tree = weight_heuristic(graph)
# print(cover_tree.edges)  # affiche [(1, 3), (3, 4)]

def color_heuristic(graph,file):
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
    utils.result_in_txt_heuristiques(file,cover_tree)
    return cover_tree

# Exemple d'utilisation de l'heuristique
# graph = nx.Graph()
# graph.add_edges_from([(1, 2), (1, 3), (2, 3)])
# cover_tree = color_heuristic(graph)
# print(cover_tree.edges)  # affiche [(1, 2)]

def color_weight_heuristic(graph,file):
    # Création de l'arbre de recouvrement vide
    cover_tree = nx.Graph()
    # Attribution de la couleur verte et du poids 1 à chaque sommet
    for node in graph.nodes():
        graph.nodes[node]['color'] = 'V'
    for edge in graph.edges():
        graph.edges[edge]['weight'] = 1
    # Répéter jusqu'à ce que l'arbre de recouvrement ait |VG| - 1 arêtes
    while cover_tree.number_of_edges() < graph.number_of_nodes() - 1:
        print(graph.edges(data=True))
        # Sélection de l'arête ayant le poids minimum et le moins de sommets jaunes et bleus comme extrémités
        min_edge = min(graph.edges(data=True), key=lambda x: (x[2]['weight'], graph.nodes[x[0]]['color'] == 'J' or graph.nodes[x[1]]['color'] == 'J', graph.nodes[x[0]]['color'] == 'B' or graph.nodes[x[1]]['color'] == 'B'))
        u, v, d = min_edge
        cover_tree.add_edge(u, v)
        # Supprimer l'arête du graphe
        graph.remove_edge(u, v)
        # Mise à jour des couleurs et poids des sommets
        for node in (u, v):
            for edge in graph.edges(node):
                edge['weight'] += 1
            if graph.degree[node] == 1:
                graph.nodes[node]['color'] = 'B'
            elif graph.degree[node] == 2:
                graph.nodes[node]['color'] = 'J'
            else:
                graph.nodes[node]['color'] = 'R'
    utils.result_in_txt_heuristiques(file,cover_tree)
    return cover_tree

# Exemple d'utilisation de l'heuristique
# graph = nx.Graph()
# graph.add_edges_from([(1, 2), (1, 3), (2, 3)])
# cover




