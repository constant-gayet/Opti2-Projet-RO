# Outils pour gérer les instances


import sys
import networkx as nx
import matplotlib.pyplot as plt
from os import listdir
from os.path import isfile, join
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


def main(dir):
    # G = build_example_graph()
    fichiers = [join(dir,f) for f in listdir(dir) if isfile(join(dir, f))]
    print(fichiers)
    for file in fichiers:
        currentFile = open(file, "r")
        G = build_graph(currentFile)
        currentFile.close()
        # print("G : ", G)
        # plnecp.plne_cp(G,file)
        plnecpm.plne_cpm(G)


    #plnecp.heuristique(G)
    # draw_graph("Graphe de base à 6 noeuds",G)

if __name__ == '__main__':
    if len(sys.argv) >= 3:
        print("Invalid number of arguments \n")
        exit()

    try:
        main(sys.argv[1])
    except IOError:
        print("The file does not exist, exiting", file=sys.stderr)
