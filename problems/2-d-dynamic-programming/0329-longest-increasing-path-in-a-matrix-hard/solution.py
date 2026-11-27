"""
LeetCode 329: Longest Increasing Path in a Matrix
Difficulty: Hard
Pattern: 2-D Dynamic Programming
Video Reference: https://www.youtube.com/watch?v=wCc_nd-GiEc
Complexity:
    - Time: O(mn)
    - Space: O(mn)
"""

from functools import lru_cache
from typing import List


class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        rows = len(matrix)
        columns = len(matrix[0])

        @lru_cache(maxsize=None)
        def path_from(row: int, column: int) -> int:
            # The state is the longest increasing path that starts at this cell.
            longest = 1
            # Only strictly larger neighbors extend this state's path.
            for next_row, next_column in (
                (row + 1, column),
                (row - 1, column),
                (row, column + 1),
                (row, column - 1),
            ):
                if (
                    0 <= next_row < rows
                    and 0 <= next_column < columns
                    and matrix[next_row][next_column] > matrix[row][column]
                ):
                    # Bounds prevent row wraparound and the value test enforces direction.
                    # The recurrence adds this cell to a larger neighbor's best suffix.
                    longest = max(longest, 1 + path_from(next_row, next_column))
            # A cell with no larger neighbor contributes the one-cell base path.
            return longest

        # Strictly increasing edges form a DAG, so recursion cannot cycle.
        # Memoization computes each cell state once regardless of how many paths reach it.
        # The helper returns an optimal suffix length, independent of its caller.
        # Each cell considers only its four outgoing DAG edges.
        # Thus memoized work is bounded by cells plus their constant-degree edges.
        # No iteration order is required because recursive dependencies are evaluated first.
        # Any cell may start the global optimum, so compare all memoized roots.
        return max(
            path_from(row, column)
            for row in range(rows)
            for column in range(columns)
        )


if __name__ == "__main__":
    solution = Solution()
    assert solution.longestIncreasingPath([[9, 9, 4], [6, 6, 8], [2, 1, 1]]) == 4
    assert solution.longestIncreasingPath([[3, 4, 5], [3, 2, 6], [2, 2, 1]]) == 4
    assert solution.longestIncreasingPath([[1]]) == 1
    assert solution.longestIncreasingPath([[7, 7], [7, 7]]) == 1
    print("All tests passed")
