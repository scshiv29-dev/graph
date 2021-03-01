from Graph import Graph

n = int(input("Enter no of vertices in Graph   "))
g = Graph(n)
while True:
    ch = int(input("1. Add an Edge   \n 2.Check if path exists   \n 3.Print Graph Matrix   \n4.Show Graph  \n5.quit \n"))
    if ch == 1:
        s = int(input("Enter Source Vertex"))
        d = int(input("Enter Destination Vertex"))
        g.add_edge(s, d)
    elif ch == 2:
        s = int(input("Enter Source Vertex"))
        d = int(input("Enter Destination Vertex"))
        g.check_simple_path(s, d)
    elif ch == 3:
        g.print_graph()
    elif ch == 4:
        g.draw_graph()
    elif ch == 5:
        quit()
