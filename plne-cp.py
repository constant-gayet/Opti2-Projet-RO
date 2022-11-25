# Formulation en programme linéaire en nombres entiers basée sur le concept de flot (PLNE-CP) [CGI09]

import pulp as pl
import networkx as nx

# Problem


# Variables
def define_problem(graph):
    problem = pl.LpProblem("CGI09", pl.LpMinimize)
    # ensemble de noeuds
    nodes = graph.nodes
    nodes_s = nodes[1:] # ensemble des noeuds privés de la source
    source = nodes[1]

    # ensemble d'aretes
    edges = graph.edges

    directed_graph = graph.to_directed()

    # ensembes d'arcs
    arcs = directed_graph.edges

    # On créé nos variables xuv et yv

    x = pl.LpVariable.dicts("x", arcs, 0, 1, cat=pl.LpBinary)
    y = pl.LpVariable.dicts("y", nodes, 0, 1, cat=pl.LpBinary)

    # constraint 9
    for x in nodes:
        tmplist = []
        for u in directed_graph.in_edges(x):
            tmplist.append(u)
        in_arcs = pl.LpVariable.dicts("A_moins", tmplist, 0, 1, cat=pl.LpBinary)
        problem += pl.lpSum(in_arcs) == 1

    # constraint 10
    tmplist = []
    tmplist2 = []
    for v in directed_graph.out_edges(source):
        tmplist.append(v)
    for u in directed_graph.in_edges(source):
        tmplist2.append(u)
    f_sv = pl.LpVariable.dicts("flows_sv", tmplist, 0, 1, cat=pl.LpBinary)
    f_uv = pl.LpVariable.dicts("flows_uv", tmplist2, 0, 1, cat=pl.LpBinary)

    problem += (pl.lpSum(f_sv) - pl.lpSum(f_uv)) <= (directed_graph.number_of_nodes() - 1)

    # constraint 11
