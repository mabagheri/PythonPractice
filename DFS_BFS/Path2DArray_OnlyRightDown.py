"""
The first function is written by me from scratch!
"""

def PrintAllPathIn2DArray_me(arr, c_row, c_col, path):
    n_rows = len(arr)
    n_cols = len(arr[0])
    c_val = arr[c_row][c_col]

    if c_col < n_cols - 1:
        path = PrintAllPathIn2DArray_me(arr, c_row, c_col + 1, path + [c_val])

    if c_row < n_rows - 1:
        path = PrintAllPathIn2DArray_me(arr, c_row + 1, c_col, path + [c_val])

    if (c_row, c_col) == (n_rows - 1, n_cols - 1):
        print(path + [c_val])
        # return

    if len(path) > 0:
        path.pop()
    return path


a = [[1, 2], [4, 5]]
PrintAllPathIn2DArray_me(a, 0, 0, [])


def PrintAllPathIn2DArray(arrA, currentRow, currentColumn, path):
    rowCount = len(arrA)
    colCount = len(arrA[0])

    if currentRow == rowCount - 1:
        for i in range(currentColumn, colCount):
            path += "-" + str(arrA[currentRow][i])
        print(path)
        return

    if currentColumn == colCount - 1:
        for i in range(currentRow, rowCount):
            path += "-" + str(arrA[i][currentColumn])
        print(path)
        return

    path = path + "-" + str(arrA[currentRow][currentColumn])
    PrintAllPathIn2DArray(arrA, currentRow + 1, currentColumn, path)
    PrintAllPathIn2DArray(arrA, currentRow, currentColumn + 1, path)


# a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# PrintAllPathIn2DArray(a, 0, 0, "")

def get_max_coins_helper(matrix, c_row, c_col, rows, cols):
    c_val = matrix[c_row][c_col]

    if c_row == rows - 1 and c_col == cols - 1:
        return c_val

    down, right = c_val, c_val
    if c_row < rows - 1:
        down += get_max_coins_helper(
            matrix, c_row + 1, c_col, rows, cols)

    if c_col < cols - 1:
        right += get_max_coins_helper(
            matrix, c_row, c_col + 1, rows, cols)

    return max(down, right)


def get_max_coins(matrix):
    return get_max_coins_helper(
        matrix, 0, 0, len(matrix), len(matrix[0]))


coins = [[0, 3, 1, 1],
         [2, 0, 0, 4],
         [1, 5, 3, 1]]
assert get_max_coins(coins) == 12

coins = [[0, 3, 1, 1],
         [2, 8, 9, 4],
         [1, 5, 3, 1]]
assert get_max_coins(coins) == 25
