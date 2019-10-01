class Node:
    # constructor to create tree node
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    # another solution
    def binaryTreePaths(self, root):
        if not root:
            return []
        if not root.left and not root.right:
            return [str(root.data)]
        tree_paths = [str(root.data) + '->' + path for path in self.binaryTreePaths(root.left)]
        tree_paths += [str(root.data) + '->' + path for path in self.binaryTreePaths(root.right)]
        return tree_paths


r = Node(10)
r.left = Node(8)
r.right = Node(4)
r.left.left = Node(3)
r.left.right = Node(5)
print(r.binaryTreePaths(r))
# node2 = Node(7, 6)
# node4 = Node()
