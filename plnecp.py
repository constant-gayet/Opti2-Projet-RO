# Formulation en programme linéaire en nombres entiers basée sur le concept de flot (PLNE-CP) [CGI09]

import pulp as pl
import networkx as nx

# Problem

G = nx.Graph()
G.add_node(1)
G.add_node(2)
G.add_node(3)
G.add_edge(1,2)
G.add_edge(2,3)
G.add_edge(3,1)

# Configuring cplex
path_to_cplex = "/opt/ibm/ILOG/CPLEX_Studio221/cplex/bin/x86-64_linux/cplex"
solver = pl.CPLEX(path=path_to_cplex)

def define_problem(graph):

    source_index = 1
    problem = pl.LpProblem("CGI09", pl.LpMinimize)
    # ensemble de noeuds
    nodes = list(graph.nodes)
    print(nodes)
    source = nodes[source_index]
    print(source)
    nodes_less_source = nodes # ensemble des noeuds privés de la source
    nodes_less_source.pop(source)
    # ensemble d'aretes
    edges = list(graph.edges)

    directed_graph = graph.to_directed()

    # ensembes d'arcs
    arcs = list(directed_graph.edges)

    # On créé nos variables xuv et yv
    x = pl.LpVariable.dicts("x", arcs, cat=pl.LpBinary)
    print("arcs:",arcs)
    print("x :", x)
    y = pl.LpVariable.dicts("y", nodes, cat=pl.LpBinary)

    problem += sum(y) #on minimise la somme des y

    # constraint 9
    for node in nodes:
        tmplist = []
        for u in directed_graph.in_edges(node):
            tmplist.append(u)
        in_arcs = pl.LpVariable.dicts("A_moins", tmplist, cat=pl.LpBinary)
        problem += pl.lpSum(in_arcs) == 1

    # constraint 10
    tmplist = []
    tmplist2 = []
    for v in directed_graph.out_edges(source):
        tmplist.append(v)
    for u in directed_graph.in_edges(source):
        tmplist2.append(u)
    f_sv = pl.LpVariable.dicts("flows_sv", tmplist, cat=pl.LpBinary)
    f_vs = pl.LpVariable.dicts("flows_vs", tmplist2, cat=pl.LpBinary)

    problem += (pl.lpSum(f_sv) - pl.lpSum(f_vs)) == (directed_graph.number_of_nodes() - 1)

    # constraint 11
    for v in nodes_less_source:
        tmplist=[]
        tmplist2=[]
        for u in directed_graph.out_edges(v):
            tmplist.append(u)
        for u in directed_graph.in_edges(v):
            tmplist2.append(u)
        f_vu = pl.LpVariable.dicts("flows_vu", tmplist, cat=pl.LpBinary)
        f_uv = pl.LpVariable.dicts("flows_uv", tmplist2, cat=pl.LpBinary)

        problem += (pl.lpSum(f_vu) - pl.lpSum(f_uv)) == -1

    # constraint 12
    f_uv_tot = pl.LpVariable.dicts("all_flows_", arcs, cat=pl.LpBinary)
    print(f_uv_tot)
    for arc in arcs:
        x_uv = x[arc]
        problem += (x_uv <= f_uv_tot[arc] <= len(nodes) * x_uv)
        # constraint 16
        problem += (len(nodes) - 1 >= f_uv_tot[arc] >= 0)

    # constraint 13
    for v in nodes:
        tmplist = []
        tmplist2 = []
        for u in directed_graph.out_edges(v):
            tmplist.append(u)
        for u in directed_graph.in_edges(v):
            tmplist2.append(u)
        x_vu = pl.LpVariable.dicts("x_vu", tmplist, cat=pl.LpBinary)
        x_uv = pl.LpVariable.dicts("x_uv", tmplist2, cat=pl.LpBinary)

        problem += (pl.lpSum(x_vu) - pl.lpSum(x_uv)) <= (len(tmplist) + len(tmplist2)) + 2


    problem.solve(solver)



define_problem(G)
