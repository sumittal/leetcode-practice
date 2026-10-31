"""
LeetCode 1584: Min Cost to Connect All Points
Difficulty: Medium
Pattern: Advanced Graphs
Video Reference: https://www.youtube.com/watch?v=f7JOBJIC-NA
Complexity:
    - Time: O(n^2)
    - Space: O(n)
"""

from typing import List


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        point_count = len(points)
        if point_count < 2:
            return 0
        # The complete point graph is connected, so every selection finds a candidate.
        # best_edge stores the cheapest known connection from the growing tree.
        best_edge = [float("inf")] * point_count
        best_edge[0] = 0
        included = [False] * point_count
        total_cost = 0
        for _ in range(point_count):
            # Select the unvisited point with the lightest edge into the current tree.
            # This cut-minimum choice is the next safe edge in Prim's algorithm.
            next_point = -1
            for index in range(point_count):
                if not included[index] and (
                    next_point == -1 or best_edge[index] < best_edge[next_point]
                ):
                    next_point = index
            included[next_point] = True
            total_cost += best_edge[next_point]
            # The selected point's key is finalized and never needs to change again.
            # Adding a point may improve every remaining point's connecting edge.
            for candidate in range(point_count):
                if included[candidate]:
                    continue
                distance = abs(points[next_point][0] - points[candidate][0])
                distance += abs(points[next_point][1] - points[candidate][1])
                best_edge[candidate] = min(best_edge[candidate], distance)
        # Prim's selection adds exactly one edge for every point after the first.
        # Manhattan distance is used directly, without constructing all graph edges.
        return total_cost


if __name__ == "__main__":
    solution = Solution()
    assert (
        solution.minCostConnectPoints([[0, 0], [2, 2], [3, 10], [5, 2], [7, 0]]) == 20
    )
    assert solution.minCostConnectPoints([[3, 12], [-2, 5], [-4, 1]]) == 18
    assert solution.minCostConnectPoints([[1, 1]]) == 0
    assert solution.minCostConnectPoints([[0, 0], [0, 0], [2, 0]]) == 2
    print("All tests passed")
