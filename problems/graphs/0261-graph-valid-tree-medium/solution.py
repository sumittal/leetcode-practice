"""
LeetCode 261: Graph Valid Tree
Difficulty: Medium
Pattern: Graphs
Video Reference: https://www.youtube.com/watch?v=bXsUuownnoQ
Complexity:
    - Time: O(V+E)
    - Space: O(V+E)
"""

from collections import deque
from typing import List


class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # A tree must have exactly n-1 edges; with this count, connectivity implies acyclic.
        if len(edges) != n - 1:
            return False
        # The edge-count condition allows connectivity alone to establish acyclicity.
        graph = [[] for _ in range(n)]
        # Store both directions because each connection is undirected.
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        # Start from vertex zero; n is positive by the problem constraint.
        seen = {0}
        queue = deque([0])
        # Breadth-first traversal discovers each vertex in the connected component once.
        while queue:
            node = queue.popleft()
            # Enqueue-time marking prevents duplicate visits through undirected back-edges.
            for neighbor in graph[node]:
                if neighbor not in seen:
                    # Mark at enqueue time to avoid revisiting a vertex from another edge.
                    seen.add(neighbor)
                    queue.append(neighbor)
        # Reaching all n vertices together with n-1 edges proves the graph is a tree.
        return len(seen) == n


if __name__ == "__main__":
    solution = Solution()
    assert solution.validTree(5, [[0, 1], [0, 2], [0, 3], [1, 4]]) is True
    assert solution.validTree(5, [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]) is False
    assert solution.validTree(1, []) is True
    assert solution.validTree(4, [[0, 1], [2, 3]]) is False
    print("All tests passed")
