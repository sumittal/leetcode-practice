"""
LeetCode 120: Triangle
Difficulty: Medium
Pattern: 1-D Dynamic Programming
Video Reference: https://www.youtube.com/watch?v=OM1MTokvxs4
Complexity:
    - Time: O(n^2)
    - Space: O(n)
"""

from typing import List


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        # dp[column] is the cheapest path from that cell to the bottom.
        costs = triangle[-1][:]
        # In-place one-row storage replaces the full triangular DP table.
        # Bottom-row values are the base cases because no choices remain there.
        for row in range(len(triangle) - 2, -1, -1):
            # Rows run upward after child costs have already been computed.
            for column in range(row + 1):
                # Each parent chooses its cheaper directly reachable child.
                costs[column] = triangle[row][column] + min(
                    costs[column], costs[column + 1]
                )
                # Descending columns preserve the right-child value from below.
            # Entries beyond this row are no longer needed by any parent.
        # One value remains for the apex's minimum complete path.
        return costs[0]


if __name__ == "__main__":
    solution = Solution()
    assert solution.minimumTotal(
        [[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]
    ) == 11
    assert solution.minimumTotal([[-10]]) == -10
    assert solution.minimumTotal([[1], [-2, -3]]) == -2
    print("All tests passed")
