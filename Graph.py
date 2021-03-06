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
            print(f"There is a simple path from {src} to {dst}")

        else:
            print(f"No path found from {src} to {dst} ")

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


n = int(input("Enter no of vertices in Graph   "))
g = Graph(n)
while True:
    ch = int(input("1. Add an Edge   \n 2.Check if path exists   \n 3.Print Graph Matrix   \n4.Show Graph  \n5.quit \n"))
    if ch == 1:
        s = int(input("Enter Source Vertex "))
        d = int(input("Enter Destination Vertex "))
        g.add_edge(s, d)
    elif ch == 2:
        s = int(input("Enter Source Vertex "))
        d = int(input("Enter Destination Vertex "))
        g.check_simple_path(s, d)
    elif ch == 3:
        g.print_graph()
    elif ch == 4:
        g.draw_graph()
    elif ch == 5:
        quit()




