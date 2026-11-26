r"""
Assessment 3.6: DFS Method in Tree
Reference: Assessment 3.5 (Last Name: GENTICA)

Binary Tree (7 Nodes: G, E, N, T, I, C, A):

            G
          /   \
         E     N
        / \   / \
       T   I C   A

DFS Methods:
- Pre-Order  : Root -> Left -> Right
- In-Order   : Left -> Root -> Right
- Post-Order : Left -> Right -> Root
"""


class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def build_gentica_binary_tree():
    # Level 0 (Root)
    root = TreeNode("G")

    # Level 1
    root.left = TreeNode("E")
    root.right = TreeNode("N")

    # Level 2
    root.left.left = TreeNode("T")
    root.left.right = TreeNode("I")
    root.right.left = TreeNode("C")
    root.right.right = TreeNode("A")

    return root


def preorder_traversal(node, visited=None):
    """DFS Pre-Order: Root -> Left -> Right"""
    if visited is None:
        visited = []
    if node is None:
        return visited

    visited.append(node.value)
    preorder_traversal(node.left, visited)
    preorder_traversal(node.right, visited)
    return visited


def inorder_traversal(node, visited=None):
    """DFS In-Order: Left -> Root -> Right"""
    if visited is None:
        visited = []
    if node is None:
        return visited

    inorder_traversal(node.left, visited)
    visited.append(node.value)
    inorder_traversal(node.right, visited)
    return visited


def postorder_traversal(node, visited=None):
    """DFS Post-Order: Left -> Right -> Root"""
    if visited is None:
        visited = []
    if node is None:
        return visited

    postorder_traversal(node.left, visited)
    postorder_traversal(node.right, visited)
    visited.append(node.value)
    return visited


def dfs_iterative(root):
    """Iterative DFS (Pre-Order) using a stack."""
    if root is None:
        return []

    visited = []
    stack = [root]

    while stack:
        current = stack.pop()
        visited.append(current.value)

        # Push right first so left is processed first
        if current.right:
            stack.append(current.right)
        if current.left:
            stack.append(current.left)

    return visited


def main():
    try:
        print("=== DFS METHODS IN TREE ===")
        print("Last Name: GENTICA")
        print()

        root = build_gentica_binary_tree()

        preorder = preorder_traversal(root)
        inorder = inorder_traversal(root)
        postorder = postorder_traversal(root)
        iterative = dfs_iterative(root)

        print("1. DFS Preorder (Root -> Left -> Right):")
        print("   " + " -> ".join(preorder))
        print()

        print("2. DFS Inorder (Left -> Root -> Right):")
        print("   " + " -> ".join(inorder))
        print()

        print("3. DFS Postorder (Left -> Right -> Root):")
        print("   " + " -> ".join(postorder))
        print()

        print("4. DFS Iterative using Stack (Pre-Order):")
        print("   " + " -> ".join(iterative))

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()