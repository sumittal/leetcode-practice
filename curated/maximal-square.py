from typing import List


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        columns = len(matrix[0])
        # dp[column] is the largest all-one square ending at this cell.
        dp = [0] * (columns + 1)
        largest = 0
        # The extra leading zero column supplies a boundary base case.
        # Row-major order keeps the previous-row diagonal in one scalar.
        for row in matrix:
            diagonal = 0
            for column in range(1, columns + 1):
                above = dp[column]
                # A zero cell breaks every square ending here.
                if row[column - 1] == "1":
                    # The smallest neighboring square limits this extension.
                    dp[column] = 1 + min(dp[column], dp[column - 1], diagonal)
                    largest = max(largest, dp[column])
                else:
                    dp[column] = 0
                # Save the old above value as the next cell's diagonal state.
                diagonal = above
            # Each row overwrites all states before the next row begins.
        # Convert the best side length to the requested area.
        return largest * largest


if __name__ == "__main__":
    solution = Solution()
    assert solution.maximalSquare(
        [
            ["1", "0", "1", "0", "0"],
            ["1", "0", "1", "1", "1"],
            ["1", "1", "1", "1", "1"],
            ["1", "0", "0", "1", "0"],
        ]
    ) == 4
    assert solution.maximalSquare([["0", "1"], ["1", "0"]]) == 1
    assert solution.maximalSquare([["0"]]) == 0
    assert solution.maximalSquare([]) == 0
    print("All tests passed")
