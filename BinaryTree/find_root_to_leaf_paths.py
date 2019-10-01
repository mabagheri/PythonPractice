"""
Python program to print all path from root to leaf in a binary tree

https://www.geeksforgeeks.org/given-a-binary-tree-print-out-all-of-its-root-to-leaf-paths-one-per-line/
"""

# Python3 program to print all of its root-to-leaf paths for a tree
class Node:

    # A binary tree node has data,
    # pointer to left child and a
    # pointer to right child
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None


def printRoute(stack, node):
    if node is None:
        return

    # append this node to the path array
    stack.append(node.data)
    if (node.left is None) and (node.right is None):
        # print out all of its
        # root - to - leaf
        print(' '.join([str(i) for i in stack]))

    # otherwise try both subtrees
    printRoute(stack, node.left)
    printRoute(stack, node.right)
    stack.pop()


# Driver program to test above function
""" 
Constructed binary tree is 
		   10 
		  /  \ 
		8	  4 
	   / \    
	  3   5   
"""
root = Node(10)
root.left = Node(8)
root.right = Node(4)
root.left.left = Node(3)
root.left.right = Node(5)
# root.right.left = Node(2)
printRoute([], root)

