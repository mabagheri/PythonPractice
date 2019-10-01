"""
# Problem 12
# https://www.youtube.com/watch?v=5o-kdjv7FD0&list=PLBZBJbE_rGRVnpitdvpdY9952IsKMDuev&index=3&t=0s
# Recursive Staircase Problem
"""

def path_Staircase_me(n, X):
    stack = [[0]]

    while stack:
        path = stack.pop()

        for _next in X:
            if _next + sum(path) == n:
                yield path + [_next]
            elif _next + sum(path) < n:
                stack.append((path + [_next]))


def path_Staircase_recursive(n):
    if n == 0:
        return 1
    if n == 1:
        return 1
    else:
        return path_Staircase_recursive(n - 1) + path_Staircase_recursive(n - 2)


N = 5
x = [1, 2]
print((list(path_Staircase_me(N, x))))
print(path_Staircase_recursive(N))
