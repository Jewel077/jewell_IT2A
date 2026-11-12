

from collections import deque


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


def bfs_traversal(root):
    if not root:
        return []

    visited = []
    queue = deque([root])

    while queue:
        current = queue.popleft()
        visited.append(current.value)

        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)

    return visited


def dfs_traversal(node, visited=None):
    if visited is None:
        visited = []

    if node is None:
        return visited

    visited.append(node.value)
    dfs_traversal(node.left, visited)
    dfs_traversal(node.right, visited)

    return visited


def main():
    try:
        print("=== Binary Tree Traversal (Last Name: GENTICA) ===")
        root = build_gentica_binary_tree()

        bfs_result = bfs_traversal(root)
        dfs_result = dfs_traversal(root)

        print(f"BFS Traversal (Level-Order): {' -> '.join(bfs_result)}")
        print(f"DFS Traversal (Pre-Order):   {' -> '.join(dfs_result)}")
    except Exception as e:
        print(f"An error occurred during binary tree traversal: {e}")


if __name__ == "__main__":
    main()