# Formulation en programme linéaire en nombres entiers basée sur le concept de flot (PLNE-CP) [CGI09]
import os.path
from shlex import join

import pulp as pl
import networkx as nx
from ast import literal_eval as make_tuple

import main
import utils

# Configuring cplex
path_to_cplex = "/opt/ibm/ILOG/CPLEX_Studio221/cplex/bin/x86-64_linux/cplex"
solver = pl.CPLEX(path=path_to_cplex)


def plne_cp(graph,file):
    source_index = 1
    problem = pl.LpProblem("CGI09", pl.LpMinimize)
    # ensemble de noeuds
    nodes = list(graph.nodes)
    print(nodes)
    print("nodes : ", nodes)
    source = nodes[source_index]
    print("source: ", source)
    nodes_less_source = nodes.copy()  # ensemble des noeuds privés de la source
    nodes_less_source.pop(source_index)
    print("nodes_less_source : ", nodes_less_source)

    # ensemble d'aretes
    directed_graph = graph.to_directed()

    # ensembes d'arcs
    arcs = list(directed_graph.edges)
    n = int(graph.number_of_nodes())
    print("n",n)
    # On créé nos variables xuv et yv
    x = pl.LpVariable.dicts("x", arcs, cat=pl.LpBinary)
    y = pl.LpVariable.dicts("y", nodes, cat=pl.LpBinary)
    f = pl.LpVariable.dicts("f", arcs, 0, n-1, cat=pl.LpInteger)
    print("arcs:", arcs)
    print("x :", x)
    print("y :", y)
    print("flows :", y)

    problem += pl.lpSum(y.values()), 'Total number of branchement nodes'  # on veut minimiser la somme des y

    for node in nodes_less_source:
        # constraint 9
        problem += pl.lpSum(x[arc] for arc in directed_graph.in_edges(node)) == 1
        # constraint 11
        problem += pl.lpSum(f[arc] for arc in directed_graph.out_edges(node)) - pl.lpSum(
            f[arc] for arc in directed_graph.in_edges(node)) == -1

    # constraint 10
    print("source out edges", directed_graph.out_edges(source))
    problem += (pl.lpSum(f[arc] for arc in directed_graph.out_edges(source)) - pl.lpSum(
        f[arc] for arc in directed_graph.in_edges(source))) == (directed_graph.number_of_nodes() - 1)

    for arc in arcs:
        # constraint 12
        problem += (f[arc] <= len(nodes) * x[arc])
        problem += (x[arc] <= f[arc])

    # constraint 13
    for node in nodes:
        problem += pl.lpSum(x[arc] for arc in directed_graph.out_edges(node)) + pl.lpSum(
            x[arc] for arc in directed_graph.in_edges(node)) <= int(graph.degree[node]) * y[node] + 2

    problem.writeLP("./plnecp.pl")
    problem.solve(solver)



    varsdict = {}
    result = []
    cover_tree = nx.Graph()
    for v in problem.variables():
        varsdict[v.name] = v.varValue
        if v.name[0]=="x" and v.varValue !=0:
            res =v.name.split('_')
            result.append(res[-2] + res[-1])

    print("sorted result", sorted(result, key=lambda x: make_tuple(x)[0]))
    cover_tree_edges = map(lambda x: make_tuple(x), result)
    cover_tree.add_edges_from(cover_tree_edges)
    print("cover tree nodes",cover_tree.nodes)
    print("cover tree edges",cover_tree.edges)
    print(file)

    utils.result_in_txt(file, cover_tree)


