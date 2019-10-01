"""
https://www.geeksforgeeks.org/lowest-common-ancestor-in-a-binary-search-tree/

"""

# A recursive python program to find LCA of two nodes
# n1 and n2

# A Binary tree node
class Node:

    # Constructor to create a new node
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# Function to find LCA of n1 and n2. The function assumes that both n1 and n2 are present in BST
def lca(root_node, node1, node2):
    # Base Case
    if root_node is None:
        return None

    # If both n1 and n2 are smaller than root, then LCA
    # lies in left
    if (root_node.data > node1) and (root_node.data > node2):
        return lca(root_node.left, node1, node2)

    # If both n1 and n2 are greater than root, then LCA
    # lies in right
    if (root_node.data < node1) and (root_node.data < node2):
        return lca(root_node.right, node1, node2)

    return root_node.data


# Driver program to test above function
""" 
Constructed binary tree is 
		   20 
		  /  \ 
		8	  22 
	   / \    
	  4   12 
	     /  \ 
	   10   14 
"""
# Let us construct the BST shown in the figure
root = Node(20)
root.left = Node(8)
root.right = Node(22)
root.left.left = Node(4)
root.left.right = Node(12)
root.left.right.left = Node(10)
root.left.right.right = Node(14)

n1 = 10
n2 = 14
t = lca(root, n1, n2)
print("LCA of %d and %d is %d" % (n1, n2, t))

n1 = 14
n2 = 4
t = lca(root, n1, n2)
print("LCA of %d and %d is %d" % (n1, n2, t))

n1 = 10
n2 = 22
t = lca(root, n1, n2)
print("LCA of %d and %d is %d" % (n1, n2, t))

# This code is contributed by Nikhil Kumar Singh(nickzuck_007)

# ------------------------------------ Another Solution -------------------------------------------------
def lca_iterative(root_node, n1, n2):
    """
    Time complexity of above solution is O(h) where h is height of tree.
    Also, the above solution requires O(h) extra space in function call stack for recursive function calls.
    We can avoid extra space using iterative solution.
    """
    # Function to find LCA of n1 and n2.
    while root_node:
        # If both n1 and n2 are smaller than root,
        # then LCA lies in left
        if root_node.data > n1 and root_node.data > n2:
            root_node = root_node.left

            # If both n1 and n2 are greater than root,
        # then LCA lies in right
        elif root_node.data < n1 and root_node.data < n2:
            root_node = root_node.right

        else:
            break

    return root_node

    # This Code is Contributed by Sumit Bhardwaj (Timus)