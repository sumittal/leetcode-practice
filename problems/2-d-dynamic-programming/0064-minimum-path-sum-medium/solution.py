"""
LeetCode 64: Minimum Path Sum
Difficulty: Medium
Pattern: 2-D Dynamic Programming
Video Reference: https://www.youtube.com/watch?v=pGMsrvt0fpk
Complexity:
    - Time: O(m n)
    - Space: O(n)
"""

from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        columns = len(grid[0])
        # One row stores the cheapest path reaching each column.
        costs = [float("inf")] * columns
        costs[0] = 0
        # Infinity marks cells without a predecessor before they are visited.
        # Row-major iteration makes the left state current and above state saved.
        for row in range(rows):
            for column in range(columns):
                # The origin has no predecessor and starts with its own cost.
                if row == 0 and column == 0:
                    costs[column] = grid[row][column]
                else:
                    from_above = costs[column]
                    from_left = costs[column - 1] if column else float("inf")
                    # Recurrence adds this cell to the cheaper reachable predecessor.
                    costs[column] = grid[row][column] + min(from_above, from_left)
                # Values left of the current column already represent this row.
            # The array now stores the completed minimum costs for this row.
        # The destination cost is the minimum sum over right-and-down paths.
        return int(costs[-1])


if __name__ == "__main__":
    solution = Solution()
    assert solution.minPathSum([[1, 3, 1], [1, 5, 1], [4, 2, 1]]) == 7
    assert solution.minPathSum([[1, 2, 3], [4, 5, 6]]) == 12
    assert solution.minPathSum([[5]]) == 5
    print("All tests passed")
