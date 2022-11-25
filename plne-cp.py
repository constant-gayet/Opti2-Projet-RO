# Formulation en programme linéaire en nombres entiers basée sur le concept de flot (PLNE-CP) [CGI09]

from pulp import *
import networkx as nx

# Problem
problem = LpProblem("CGI09", LpMinimize)


# Variables
def create_variables(graph):
    # ensemble de noeuds
    nodes = graph.nodes

    # ensemble d'aretes
    edges = graph.edges

    directed_graph = graph.to_directed()

    # ensembes d'arcs
    arcs = directed_graph.edges

    x = []
    x = [LpVariable("x" + arc[0] + arc[1], 0, 1, cat=LpInteger) for arc in arcs]

    y = []
    y = [LpVariable("y" + node.value, 0, 1, cat="Integer") for node in nodes]


