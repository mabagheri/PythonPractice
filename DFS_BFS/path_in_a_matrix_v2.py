"""

"""

def find_path(matrix, start, end, visited=None):
    # if visited is None:
    #     visited = set()
    # visited.add(start)

    q = [(start, [start])]
    while q:
        node, path = q.pop()

        neighbors = find_neighbors(matrix, node)
        for _next in neighbors - set(path):
            # if _next not in visited:
            if _next == end:
                return True
            else:
                q.append((_next, path + [_next]))
                # visited.add(node)
    return False

def find_neighbors(matrix, node):
    m = node[0]
    n = node[1]

    n_rows = len(matrix)
    n_cols = len(matrix[0])
    neighbors = []

    if (m < n_rows-1) and (matrix[m+1][n] == 3):
        neighbors.append((m+1, n))

    if (m > 0) and (matrix[m-1][n] == 3):
        neighbors.append((m-1, n))

    if (n < n_cols-1) and (matrix[m][n+1] == 3):
        neighbors.append((m, n+1))

    if (n > 0) and (matrix[m][n-1] == 3):
        neighbors.append((m, n-1))

    return set(neighbors)


M = [[3, 3, 3, 0],
     [0, 3, 3, 3],
     [0, 0, 3, 0],
     [0, 3, 3, 3]]

print(find_path(M, (0, 0), (3, 2)))
print(find_path(M, (0, 0), (3, 0)))
