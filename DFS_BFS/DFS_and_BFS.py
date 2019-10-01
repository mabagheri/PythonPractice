"""
https://eddmann.com/posts/depth-first-search-and-breadth-first-search-in-python/

In this post I will be exploring two of the simpler available algorithms,
Depth-First and Breath-First search to achieve the goals highlighted below:

A) Find all vertices in a subject vertices connected component.
B) Return all available paths between two vertices.
C) And in the case of BFS, return the shortest path (length measured by number of path edges).
"""


sample_graph = {'A': {'B', 'C'},
                'B': {'A', 'D', 'E'},
                'C': {'A', 'F'},
                'D': {'B'},
                'E': {'B', 'F'},
                'F': {'C', 'E'}}


sample_graph2 = {'A': {'B', 'C'},
                 'B': {'A', 'D'},
                 'C': {'A'},
                 'D': {'B', 'F'},
                 'E': {'F', 'E'},
                 'F': {'E'}}
start_node = 'D'
end_node = 'F'
the_graph = sample_graph

# ------------------------------------------------------------------------------------------------------
#                                           Depth First Search
# ------------------------------------------------------------------------------------------------------
def dfs_connected_components(graph, start):
    # A) Find all vertices in a subject vertices connected component.
    visited = set()
    stack = [start]

    while stack:
        current_vertex = stack.pop()
        if current_vertex not in visited:
            visited.add(current_vertex)
            stack.extend(graph[current_vertex] - visited)
    return visited

# print(dfs_connected_components(sample_graph, 'A'))

def dfs_connected_components_recursive(graph, start, visited=None):
    # Second implementation for goal A
    if visited is None:
        visited = set()
    visited.add(start)

    for _next in graph[start] - visited:
        # print(_next, end=',')
        dfs_connected_components_recursive(graph, _next, visited)

    return visited

# print(dfs_connected_components_recursive(sample_graph, 'A'))

def dfs_paths(graph, start, goal):
    # B) Return all available paths between two vertices.
    stack = [(start, [start])]
    while stack:
        (vertex, path) = stack.pop()
        for next_item in graph[vertex] - set(path):
            if next_item == goal:
                yield path + [next_item]
            else:
                stack.append((next_item, path + [next_item]))

# print(list(dfs_paths(sample_graph, start_node, end_node)))

def dfs_paths_recursive(graph, start, goal, path=None):
    if path is None:
        path = [start]
    if start == goal:
        yield path
    for _next in graph[start] - set(path):
        yield from dfs_paths_recursive(graph, _next, goal, path + [_next])

# ------------------------------------------------------------------------------------------------------
#                                           Breath First Search
# ------------------------------------------------------------------------------------------------------
"""
Breath First Search implementation is very close to the DFS, except that for the next item, we pop the first element of
the candidates. So, we use pop(0) instead of pop()=pop(-1)
"""
def bfs_connected_components(graph, start):
    # A) Find all vertices in a subject vertices connected component.
    visited, queue = set(), [start]
    while queue:
        vertex = queue.pop(0)
        if vertex not in visited:
            visited.add(vertex)
            queue.extend(graph[vertex] - visited)
    return visited

# print(bfs(sample_graph, 'A'))

def bfs_paths(graph, start, goal):
    # B) Return all available paths between two vertices.
    queue = [(start, [start])]
    while queue:
        (vertex, path) = queue.pop(0)
        for next_item in graph[vertex] - set(path):
            if next_item == goal:
                yield path + [next_item]
            else:
                queue.append((next_item, path + [next_item]))

# print(list(bfs_paths(the_graph, start_node, end_node)))


def bfs_is_reachable_count(graph, s, d):
    """
    This is the code from below, that I modified to return number of ways
    https://www.geeksforgeeks.org/find-if-there-is-a-path-between-two-vertices-in-a-given-graph/ (with small modification)
    """
    visited, queue = set(), [s]
    count = 0
    visited.add(s)
    while queue:
        vertex = queue.pop(0)

        # # Else, continue to do BFS
        for i in graph[vertex] - visited:
            if i == d:
                count += 1  # yield
            else:
                queue.append(i)
                visited.add(i)

    # If BFS is complete without visited d
    return count

# print((bfs_is_reachable_count(the_graph, start_node, end_node)))

def bfs_is_reachable2(graph, s, d):
    """
    This is the code from below, that I modified to return "is reachable?"
    https://www.geeksforgeeks.org/find-if-there-is-a-path-between-two-vertices-in-a-given-graph/ (with small modification)
    """
    visited, queue = set(), [s]
    while queue:
        vertex = queue.pop(0)

        # Else, continue to do BFS
        if vertex == d:
            yield True  # yield
        else:
            if vertex not in visited:
                visited.add(vertex)
                queue.extend(graph[vertex] - visited)

    # If BFS is complete without visited d
    return False

# print(list(bfs_is_reachable2(the_graph, start_node, end_node)))


def bfs_is_reachable3(graph, s, d):
    # Mark all the vertices as not visited
    visited = [False] * len(graph)

    # Create a queue for BFS
    queue = []

    # Mark the source node as visited and enqueue it
    queue.append(s)
    visited[s] = True

    while queue:

        # Dequeue a vertex from queue
        n = queue.pop(0)

        # If this adjacent node is the destination node,
        # then return true
        if n == d:
            yield True

    #  Else, continue to do BFS
    for i in graph[n]:
        if visited[i] == False:
            queue.append(i)
            visited[i] = True
    # If BFS is complete without visited d

    yield False

# print(list(bfs_is_reachable3(the_graph, start, end)))
