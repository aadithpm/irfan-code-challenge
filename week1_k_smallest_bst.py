"""
Question: Find the kth smallest element in a Binary Search Tree

Approach used:
--> Inorder traversal prints nodes in ascending order
--> (k - 1)th index of elements returned by inorder is kth smallest element

Complexity: O(n)
"""

class Node:
    """
    Constructor for Node class with attributes:
    l_child = None
    r_child = None
    data = val
    """

    def __init__(self, val, l = None, r = None):
        self.l_child = None
        self.r_child = None
        self.data = val

def multi_bst_insert(root, nodes):
    # Insert multiple nodes into tree
    for node in nodes:
        bst_insert(root, node)

def bst_insert(root, node):
    # If tree is empty
    if not root:
        root = node
    else:
        # If data is greater, we insert it to the right
        if root.data > node.data:
            # If there's no left child
            if not root.l_child:
                root.l_child = node
            
            # If there is a left child already
            else:
                bst_insert(root.l_child, node)
        # If data is lesser, we insert it to the left
        elif root.data < node.data:
            # If there's no right child
            if not root.r_child:
                root.r_child = node
            
            # If there is a right child already
            else:
                bst_insert(root.r_child, node)
        
        # If data is the same
        else:
            print("Node already exists in tree")

def inorder(root):
    # In order prints the nodes in ascending order
    # Read more about tree traversal here: https://en.wikipedia.org/wiki/Tree_traversal#Data_structures_for_tree_traversal
    if not root:
        return
    inorder(root.l_child)
    inorder_tree.append(root.data)
    inorder(root.r_child)



# Empty variable for storing node values
inorder_tree = []

# Initialise root node
root = Node(5)

# Node values for tree. Change this to try out different values.
nodes = [4, 6, 3, 1, 2, 7]

# Converts nodes to set so all values are distinct, maps Node() constructor on all items in list to get Node objects
nodes = set(nodes)
nodes = list(map(lambda x: Node(x), nodes))

# Insert all the nodes into the tree
multi_bst_insert(root, nodes)

# Perform inorder traversal
inorder(root)

# Loop to help in getting input again in case of exceptions
while True:
    try:
        # Get value of k
        k = int(input("k? "))

        # Print the k smallest element in tree
        print("The {0} smallest element is {1}".format(k, inorder_tree[k-1]))

    # Illegal base conversion
    except ValueError:
        print("k takes positive integer values only.")

    # List index out of range
    except IndexError:
        print("There are only {0} elements in the list".format(len(inorder_tree)))
    
    else:
        break