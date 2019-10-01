"""
Python3 program to find path between two cell in matrix
https://www.geeksforgeeks.org/find-whether-path-two-cells-matrix/

My notes: Generally, this do the same thing as "bfs_paths" or "dfs_paths" in DFS_BFS.py. But, first, we need to define
graph. More specifically, define neighbours of each vertex.
"""
from collections import defaultdict


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    # add edge to graph
    def addEdge(self, u, v):
        self.graph[u].append(v)

    # BFS function to find path from source to sink
    def BFS(self, s, d):

        # Base case
        if s == d:
            return True

        # Mark all the vertices as not visited
        visited = [False] * (len(self.graph) + 1)

        queue = [s]
        visited[s] = True

        while queue:

            # Dequeue a vertex from queue
            vertex = queue.pop(0)  # .pop() makes it to DFS

            # If this adjacent node is the destination node, then return true
            if vertex == d:
                return True

            # Get all adjacent vertices of the dequeued vertex s. If a adjacent has
            # not been visited, then mark it visited and enqueue it
            for i in self.graph[vertex]:

                # Else, continue to do BFS
                if not visited[i]:
                    queue.append(i)
                    visited[i] = True

        # If BFS is complete without visiting d
        return False


def isSafe(i, j, matrix):
    if (i >= 0) and (i <= len(matrix)) and (j >= 0) and (j <= len(matrix[0])):
        return True
    else:
        return False


# Returns true if there is a path from a source (a
# cell with value 1) to a destination (a cell with
# value 2)
def findPath(matrix):
    s, d = None, None  # source and destination
    N = len(matrix)
    g = Graph()

    # create graph with n*n node
    # each cell consider as node
    k = 1  # Number of current vertex
    for i in range(N):
        for j in range(N):
            if matrix[i][j] != 0:

                # connect all 4 adjacent cell to
                # current cell
                if isSafe(i, j + 1, matrix):
                    g.addEdge(k, k + 1)
                if isSafe(i, j - 1, matrix):
                    g.addEdge(k, k - 1)
                if (j < N - 1) and (isSafe(i + 1, j, matrix)):
                    g.addEdge(k, k + N)
                if (i > 0) and (isSafe(i - 1, j, matrix)):
                    g.addEdge(k, k - N)

            if matrix[i][j] == 1:
                s = k

            # destination index
            if matrix[i][j] == 2:
                d = k
            k += 1

    # find path Using BFS
    return g.BFS(s, d)

M = [[0, 3, 0, 1],
     [3, 0, 3, 3],
     [2, 3, 3, 3],
     [0, 3, 3, 3]]

if findPath(M):
    print("Yes")
else:
    print("No")
