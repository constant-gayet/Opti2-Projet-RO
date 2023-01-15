# Outils pour gérer les instances
import os
import sys
import networkx as nx
import matplotlib.pyplot as plt
from os import listdir
from os.path import isfile, join

import heuristiques
import plnecpm
import plnecp


def build_example_graph():
    G = nx.empty_graph()
    G.add_node(1)
    G.add_node(2)
    G.add_node(3)
    G.add_node(4)
    G.add_node(5)
    G.add_node(6)
    G.add_edge(1, 5)
    G.add_edge(2, 4)
    G.add_edge(2, 5)
    G.add_edge(3, 5)
    G.add_edge(3, 6)
    G.add_edge(4, 5)
    G.add_edge(5, 6)
    return G


def build_graph(file):
    n, m, zero = file.readline().split()  # n nombre de noeuds, m nombre d'arrêtes
    n = int(n)
    m = int(m)
    zero = int(zero)
    graph = nx.Graph()

    for i in range(1, int(n + 1)):
        graph.add_node(
            i)  # on ajoute tous les noeuds au graphe (en supposant que tous les noeuds soient numérotés de# 1 à n)

    for line in file:
        u, v, zero = line.split()
        graph.add_edge(int(u), int(v))
    return graph


def draw_graph(title,graph):
    nx.draw(graph, with_labels=True)
    plt.title(title)
    plt.show()


def main_plnecpm(dir):
    # G = build_example_graph()

    fichiers = [join(dir,f) for f in listdir(dir) if isfile(join(dir, f))]
    # On enlève les fichiers qui ont déjà été calculés
    if not os.path.exists('./Results/plnecpm/Spd_Inst_Rid_Final2_0-500'):
        os.makedirs('./Results/plnecpm/Spd_Inst_Rid_Final2_0-500')
    result_dir = './Results/plnecpm/Spd_Inst_Rid_Final2_0-500'
    result_fichiers = [join(result_dir, f) for f in listdir(result_dir) if isfile(join(result_dir, f))]
    for file in fichiers:
        if file in result_fichiers:
            fichiers.remove(file)

    print(fichiers)
    for file in fichiers:
        currentFile = open(file, "r")
        G = build_graph(currentFile)
        currentFile.close()
        # print("G : ", G)
        # plnecp.plne_cp(G,file)
        plnecpm.plne_cpm(G,file)


    #plnecp.heuristique(G)
    # draw_graph("Graphe de base à 6 noeuds",G)
def main_plnecp(dir):
    # G = build_example_graph()

    fichiers = [join(dir,f) for f in listdir(dir) if isfile(join(dir, f))]
    # On enlève les fichiers qui ont déjà été calculés
    if not os.path.exists('./Results/plnecp/Spd_Inst_Rid_Final2_0-500'):
        os.makedirs('./Results/plnecp/Spd_Inst_Rid_Final2_0-500')
    result_dir = './Results/plnecp/Spd_Inst_Rid_Final2_0-500'
    result_fichiers = [join(result_dir,f) for f in listdir(result_dir) if isfile(join(result_dir, f))]
    for file in fichiers:
        if file in result_fichiers:
            fichiers.remove(file)

    print(fichiers)
    for file in fichiers:
        currentFile = open(file, "r")
        G = build_graph(currentFile)
        currentFile.close()
        # print("G : ", G)
        plnecp.plne_cp(G,file)
        # plnecpm.plne_cpm(G,file)

def main_heuristiques(dir):
    # G = build_example_graph()

    fichiers = [join("Instances/Instances/Spd_Inst_Rid_Final2/",f[7:]) for f in listdir(dir) if isfile(join(dir, f))]
    # On enlève les fichiers qui ont déjà été calculés
    if not os.path.exists('Results/heuristiques/color/Spd_Inst_Rid_Final2_0-500'):
        os.makedirs('Results/heuristiques/color/Spd_Inst_Rid_Final2_0-500')

    print(fichiers)
    for file in fichiers:
        currentFile = open(file, "r")
        G = build_graph(currentFile)
        currentFile.close()
        heuristiques.color_weight_heuristic(G,file)

if __name__ == '__main__':
    if len(sys.argv) >= 3:
        print("Invalid number of arguments \n")
        exit()

    try:
        main_heuristiques(sys.argv[1])
    except IOError:
        print("The file does not exist, exiting", file=sys.stderr)
