from typing import List


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        largest_node = max(max(edge) for edge in edges)
        # Each vertex begins in a component containing only itself.
        parent = list(range(largest_node + 1))
        size = [1] * (largest_node + 1)

        def find(node: int) -> int:
            # Path compression points every visited node directly at its component root.
            if parent[node] != node:
                parent[node] = find(parent[node])
            return parent[node]

        def union(first: int, second: int) -> bool:
            # The same root means this edge would close a cycle.
            first_root = find(first)
            second_root = find(second)
            if first_root == second_root:
                return False
            # Distinct roots can be joined without introducing a cycle.
            # Attach the smaller component to keep trees shallow.
            if size[first_root] < size[second_root]:
                first_root, second_root = second_root, first_root
            parent[second_root] = first_root
            size[first_root] += size[second_root]
            return True

        # Input order ensures the returned edge is the one that first closes a cycle.
        # Path compression and union by size keep the amortized operation cost near constant.
        for edge in edges:
            if not union(edge[0], edge[1]):
                return edge
        # The problem guarantees exactly one redundant connection.
        return []


if __name__ == "__main__":
    solution = Solution()
    assert solution.findRedundantConnection([[1, 2], [1, 3], [2, 3]]) == [2, 3]
    assert solution.findRedundantConnection(
        [[1, 2], [2, 3], [3, 4], [1, 4], [1, 5]]
    ) == [1, 4]
    assert solution.findRedundantConnection([[1, 2], [2, 3], [3, 1]]) == [3, 1]
    print("All tests passed")
