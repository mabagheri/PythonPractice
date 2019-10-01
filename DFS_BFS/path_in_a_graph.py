"""
Find if there is a path between two vertices in a directed graph
https://www.geeksforgeeks.org/find-if-there-is-a-path-between-two-vertices-in-a-given-graph/

My notes: Generally, this do the same thing as "bfs_paths" or "dfs_paths" in DFS_BFS.py. But, first, we need to define
graph. More specifically, define neighbours of each vertex.
"""
from collections import defaultdict


# This class represents a directed graph using adjacency list representation
class Graph:

    def __init__(self, vertices):
        self.V = vertices  # No. of vertices
        self.graph = defaultdict(list)  # default dictionary to store graph

    # function to add an edge to graph
    def add_edge(self, u, v):
        self.graph[u].append(v)

    # Use BFS to check path between s and d
    def is_reachable(self, s, d):
        # Mark all the vertices as not visited
        visited = [False] * self.V

        # Create a queue for BFS
        queue = [s]
        visited[s] = True

        while queue:

            # Dequeue a vertex from queue
            vertex = queue.pop(0)  # .pop() makes it to DFS

            # If this adjacent node is the destination node, then return true
            if vertex == d:
                return True

            #  Else, continue to do BFS
            for i in self.graph[vertex]:
                if not visited[i]:
                    queue.append(i)
                    visited[i] = True
            # If BFS is complete without visited d

        return False


# Create a graph given in the above diagram
g = Graph(4)
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(2, 3)
g.add_edge(3, 3)

u = 1
v = 3

if g.is_reachable(u, v):
    print("There is a path from %d to %d" % (u, v))
else:
    print("There is no path from %d to %d" % (u, v))

u = 3
v = 1
if g.is_reachable(u, v):
    print("There is a path from %d to %d" % (u, v))
else:
    print("There is no path from %d to %d" % (u, v))
