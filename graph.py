"""
Assessment 3.4: Non-linear Data Structure
Program 2: Graph Traversal (BFS and DFS)
Reference: Assessment 3.3 (Last Name: GENTICA)

Graph Structure (7 Vertices: G, E, N, T, I, C, A):
- Level 0: G
- Level 1: E, I, N
- Level 2: T, A, C
"""

from collections import deque


def build_gentica_graph():
    """Adjacency list mirroring the 7-vertex graph diagram in Assessment 3.3."""
    graph = {
        "G": ["E", "I", "N"],
        "E": ["G", "T", "I"],
        "I": ["G", "E", "N", "A"],
        "N": ["G", "I", "C"],
        "T": ["E", "A"],
        "A": ["T", "I"],
        "C": ["N"],
    }
    return graph


def bfs_graph(graph, start):
    """Breadth-First Search (BFS) Traversal for an Undirected Graph."""
    visited = set([start])
    queue = deque([start])
    order = []

    while queue:
        vertex = queue.popleft()
        order.append(vertex)

        for neighbor in graph[vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return order


def dfs_graph(graph, start, visited=None, order=None):
    """Depth-First Search (DFS) Traversal for an Undirected Graph."""
    if visited is None:
        visited = set()
    if order is None:
        order = []

    visited.add(start)
    order.append(start)

    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs_graph(graph, neighbor, visited, order)

    return order


if __name__ == "__main__":
    try:
        gentica_graph = build_gentica_graph()
        start_vertex = "G"

        bfs_result = bfs_graph(gentica_graph, start_vertex)
        dfs_result = dfs_graph(gentica_graph, start_vertex)

        print("=== Graph Traversal (Last Name: GENTICA) ===")
        print(f"BFS Traversal: {' -> '.join(bfs_result)}")
        print(f"DFS Traversal: {' -> '.join(dfs_result)}")
    except Exception as e:
        print(f"An error occurred during graph traversal: {e}")