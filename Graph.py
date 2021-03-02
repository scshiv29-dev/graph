import numpy as np
import networkx as nx
import matplotlib.pyplot as plt


class Graph:
    # initializing the class with no of vertices
    def __init__(self, vertices):
        # declaring labeldict for labeling of graph
        self.labeldict = {}
        # initializing vertices
        self.V = vertices
        # initializing graph with all values to 0
        self.graph = []
        for i in range(self.V):
            self.labeldict[i] = i
            l = []
            for j in range(self.V):
                l.append(0)
            self.graph.append(l)

    def add_edge(self, src, dst):
        # adding path i.e 1 from src to dst
        self.graph[src][dst] = 1

    # checking for simple path
    def check_simple_path(self, src, dst):

        found = False
        if self.graph[src][dst] == 1:
            found = True
        if not found:
            temp = []
            for i in range(self.V):
                if self.graph[src][i] == 1:
                    temp.append(i)

            if temp is not None:
                for t in temp:
                    # print(t)
                    # print(temp)
                    if self.graph[t][dst] == 1:
                        found = True
                        break
                    else:
                        for i in range(self.V):
                            if self.graph[t][i] == 1:
                                temp.append(i)

        if found:
            print("There is a path")

        else:
            print("No path found")

    # printing matrix format of graph

    def print_graph(self):
        print(np.matrix(self.graph))

    # drawing graph using matplotlib and networkx

    def draw_graph(self):
        alg = nx.DiGraph
        G2 = np.array(self.graph)
        G = nx.from_numpy_matrix(G2, create_using=alg)
        nx.draw_circular(G, labels=self.labeldict, with_labels=True)
        plt.show()


g = Graph(8)
g.add_edge(0, 3)
g.add_edge(3, 5)
g.add_edge(5, 6)
g.add_edge(6, 7)
g.add_edge(3, 4)
g.add_edge(1, 0)
g.add_edge(1, 2)
g.add_edge(1, 4)
g.add_edge(4, 6)
g.add_edge(2, 7)
g.add_edge(7, 1)
g.check_simple_path(0, 1)
g.check_simple_path(2, 6)
g.print_graph()
g.draw_graph()
