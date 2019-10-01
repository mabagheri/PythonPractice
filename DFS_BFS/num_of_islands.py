"""
https://colorfulcodesblog.wordpress.com/2018/09/06/number-of-islands-tutorial-python/
"""
def num_of_islands(matrix):
    if not matrix:
        return 0

    n_row = len(matrix)
    n_col = len(matrix[0])
    count = 0

    for i in range(n_row):
        for j in range(n_col):
            if matrix[i][j] == 1:
                print(matrix)
                # dfs(copy.deepcopy(matrix), n_row, n_col, i, j)  # in this case, it does not work ! just to check
                dfs(matrix, n_row, n_col, i, j)
                count += 1
    return count


def dfs(g, n_rows, n_cols, x, y):
    print("x=", x, "y=", y, "matrix=", g)
    if g[x][y] == 0:
        return
    g[x][y] = 0

    if x != 0:
        dfs(g, n_rows, n_cols, x - 1, y)

    if x != n_rows - 1:
        dfs(g, n_rows, n_cols, x + 1, y)

    if y != 0:
        dfs(g, n_rows, n_cols, x, y - 1)

    if y != n_cols - 1:
        dfs(g, n_rows, n_cols, x, y + 1)

sample = [[1, 1, 0, 0, 0],
          [0, 1, 0, 0, 1],
          [1, 0, 0, 1, 1],
          [0, 0, 0, 0, 0]]

print(num_of_islands(sample))
