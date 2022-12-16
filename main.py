# Outils pour gérer les instances


import sys
import networkx as nx
import matplotlib.pyplot as plt
import plnecp
import PLNE_CPM


def build_graph(file):
    n, m, zero = file.readline().split()  # n nombre de noeuds, m nombre d'arrêtes
    n = int(n)
    m = int(m)
    zero = int(zero)
    graph = nx.Graph()

    for i in range(1, int(n+1)):
        graph.add_node(i)   # on ajoute tous les noeuds au graphe (en supposant que tous les noeuds soient numérotés de# 1 à n)

    for line in file:
        u, v, zero = line.split()
        graph.add_edge(int(u), int(v))
    return graph


def draw_graph(graph):
    nx.draw(graph)
    plt.show()


def main(file):
    G = build_graph(file)
    print("G : " , G)
    #plnecp.define_problem(G)
    PLNE_CPM.plne_cpm(G)

    plnecp.define_problem(G)

if __name__ == '__main__':
    if len(sys.argv) >= 3:
        print("Invalid number of arguments \n")
        exit()

    try:
        currentFile = open(sys.argv[1], "r")
        main(currentFile)
        currentFile.close()
    except IOError:
        print("The file does not exist, exiting", file=sys.stderr)
