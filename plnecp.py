# Formulation en programme linéaire en nombres entiers basée sur le concept de flot (PLNE-CP) [CGI09]

import pulp as pl
import networkx as nx

import plnecp

# Configuring cplex
path_to_cplex = "/opt/ibm/ILOG/CPLEX_Studio221/cplex/bin/x86-64_linux/cplex"
solver = pl.CPLEX(path=path_to_cplex)




def define_problem(graph):
    source_index = 1
    problem = pl.LpProblem("CGI09", pl.LpMinimize)
    # ensemble de noeuds
    nodes = list(graph.nodes)
    print(nodes)
    nodes_not_list = graph.nodes
    print("nodes : ", nodes)
    source = nodes[source_index]
    print("source: ",source)
    nodes_less_source = nodes.copy()  # ensemble des noeuds privés de la source
    nodes_less_source.pop(source_index)
    print("nodes_less_source : ", nodes_less_source)
    # ensemble d'aretes
    edges = list(graph.edges)

    directed_graph = graph.to_directed()

    # ensembes d'arcs
    arcs = list(directed_graph.edges)

    # On créé nos variables xuv et yv
    x = pl.LpVariable.dicts("x", arcs, cat=pl.LpBinary)
    print("arcs:", arcs)
    print("x :", x)
    y = pl.LpVariable.dicts("y", nodes, cat=pl.LpBinary)

    print("y :", y)

    problem += pl.lpSum(y), 'Total number of branchement nodes'  # on minimise la somme des y

    # constraint 9
    tmplist = []
    for node in nodes_less_source:
        for (u,vp) in directed_graph.in_edges(node):
            if node == vp:
                tmplist.append(x[(u,vp)])
        in_arcs = pl.LpVariable.dicts("A_moins", tmplist, cat=pl.LpBinary)
        problem += pl.lpSum(in_arcs) == 1
        tmplist = []

    # constraint 10
    tmplist = []
    tmplist2 = []
    for v in directed_graph.out_edges(source):
        tmplist.append(v)
    for u in directed_graph.in_edges(source):
        tmplist2.append(u)
    f_sv = pl.LpVariable.dicts("flows_sv", tmplist, 0, len(nodes) - 1, cat=pl.LpInteger)
    f_vs = pl.LpVariable.dicts("flows_vs", tmplist2, 0, len(nodes) - 1, cat=pl.LpInteger)

    problem += (pl.lpSum(f_sv) - pl.lpSum(f_vs)) == (directed_graph.number_of_nodes() - 1)

    # constraint 11
    for v in nodes_less_source:
        tmplist = []
        tmplist2 = []
        for u in directed_graph.out_edges(v):
            tmplist.append(u)
        for u in directed_graph.in_edges(v):
            tmplist2.append(u)
        f_vu = pl.LpVariable.dicts("flows_vu", tmplist, cat=pl.LpBinary)
        f_uv = pl.LpVariable.dicts("flows_uv", tmplist2, cat=pl.LpBinary)

        problem += (pl.lpSum(f_vu) - pl.lpSum(f_uv)) == -1

    # constraint 12
    f_uv_tot = pl.LpVariable.dicts("all_flows_", arcs, 0, len(nodes) - 1, cat=pl.LpInteger)
    print(f_uv_tot)
    for arc in arcs:
        x_uv = x[arc]
        problem += (f_uv_tot[arc] <= len(nodes) * x_uv)
        problem += (x_uv <= f_uv_tot[arc])
        # constraint 16
        problem += (len(nodes) - 1 >= f_uv_tot[arc] >= 0)

    # constraint 13
    for (index, v) in enumerate(nodes):
        tmplist = []
        tmplist2 = []
        for u in directed_graph.out_edges(v):
            tmplist.append(x[(u,v)])
        for u in directed_graph.in_edges(v):
            tmplist2.append(x[(u,v)])
        x_vu = pl.LpVariable.dicts(tmplist, cat=pl.LpBinary)
        x_uv = pl.LpVariable.dicts(tmplist2, cat=pl.LpBinary)
        problem += (pl.lpSum(x_vu) + pl.lpSum(x_uv)) <= int(graph.degree(v)) * y[index+1] + 2


    varsdict = {}
    for v in problem.variables():
        varsdict[v.name] = v.varValue
    print("varsdict : ",varsdict)
    problem.writeLP("./plnecp.pl")
    problem.solve(solver)
