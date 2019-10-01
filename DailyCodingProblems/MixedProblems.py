# https://www.youtube.com/watch?v=5o-kdjv7FD0&list=PLBZBJbE_rGRVnpitdvpdY9952IsKMDuev&index=3&t=0s
# Recursive Staircase Problem
def path_Staircase_me(N, X):
    stack = [[0]]

    while stack:
        path = stack.pop()

        for _next in X:
            if _next + sum(path) == N:
                yield path + [_next]
            elif _next + sum(path) < N:
                stack.append((path + [_next]))


def path_Staircase_recursive(N):
    if N == 0:
        return 1
    if N == 1:
        return 1
    else:
        return path_Staircase_recursive(N - 1) + path_Staircase_recursive(N - 2)


N = 5
x = [1, 2]
print((list(path_Staircase_me(N, x))))
print(path_Staircase_recursive(N))


# https://www.youtube.com/watch?v=uQdy914JRKQ&list=PLBZBJbE_rGRVnpitdvpdY9952IsKMDuev&index=4
def add_one(arr):
    new_arr = [0 for i in arr]
    carry = 1
    l = len(arr)

    for i in range(l - 1, -1, -1):
        sum_v = arr[i] + carry
        if sum_v == 10:
            carry = 1
            new_arr[i] = 0
        else:
            new_arr[i] = arr[i] + carry
            carry = 0

    if carry == 1:
        new_arr = [0 for i in range(len(arr) + 1)]
        new_arr[0] = 1

    return new_arr


a = [9, 9, 9]
print(add_one(a))

graph = {'A': {'B', 'C'},
         'B': {'A', 'D', 'E'},
         'C': {'A', 'F'},
         'D': {'B'},
         'E': {'B', 'F'},
         'F': {'C', 'E'}}


# https://www.youtube.com/watch?v=JlMyYuY1aXU
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = Node()

    def append(self, value):
        new_node = Node(value)
        cur = self.head

        while cur.next is not None:
            cur = cur.next
        cur.next = new_node

    def display(self):
        cur = self.head

        while cur.next is not None:
            cur = cur.next
            print(cur.data, end=',')


a = LinkedList()
a.append(1)
a.append(6)
a.display()
