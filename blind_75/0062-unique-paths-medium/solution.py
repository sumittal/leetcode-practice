"""
LeetCode 62: Unique Paths
Difficulty: Medium
Pattern: 2-D Dynamic Programming
Video Reference: https://www.youtube.com/watch?v=IlEsdxuD4lY
Complexity:
    - Time: O(m*n)
    - Space: O(n)
"""

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # With one row, every column has one path because only right moves are possible.
        # The first row is reachable in exactly one way by moving only right.
        dp = [1] * n
        # Initially each entry counts paths across the first row.
        # At each row, columns are updated left-to-right so dp[col-1] is current-row data.
        for _ in range(1, m):
            # The outer loop advances one grid row at a time.
            # Each subsequent row reuses the array as the prior row is overwritten.
            for col in range(1, n):
                # Current cell combines the updated left cell and prior-row value above.
                dp[col] += dp[col - 1]
        # The bottom-right cell stores the total number of routes.
        return dp[-1]


if __name__ == "__main__":
    solution = Solution()
    assert solution.uniquePaths(3, 7) == 28
    assert solution.uniquePaths(3, 2) == 3
    assert solution.uniquePaths(1, 1) == 1
    assert solution.uniquePaths(1, 5) == 1
    print("All tests passed")
