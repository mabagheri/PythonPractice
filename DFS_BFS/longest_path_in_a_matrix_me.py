"""
M = [[3, 3, 3, 0],
     [0, 3, 3, 3],
     [0, 0, 3, 0],
     [0, 3, 3, 3]]
"""
def find_longest_path(matrix):
    visited = set()
    n_rows = len(matrix)
    n_cols = len(matrix[0])

    for i in range(n_rows):
        for j in range(n_cols):
            node = (i, j)
            if node not in visited:
                find_length_longest_path_one_node(matrix, node, max_lengths, visited)

    return max_lengths


def find_length_longest_path_one_node(matrix, start, max_lengths=None, visited=None):
    visited.add(start)

    neighbors = find_neighbors(matrix, start)

    for _next in neighbors:
        if _next not in visited:
            find_length_longest_path_one_node(matrix, _next, max_lengths, visited)

        max_lengths[start[0]][start[1]] = max(max_lengths[start[0]][start[1]], 1 + max_lengths[_next[0]][_next[1]])


def find_neighbors(matrix, node):
    m = node[0]
    n = node[1]

    if matrix[m][n] == 0:
        return []
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


# M = [[3, 3, 0],
#      [0, 0, 0],
#      [0, 0, 3]]
max_lengths = [[0 for i in range(len(M))] for j in range(len(M[0]))]

print(find_longest_path(M))
