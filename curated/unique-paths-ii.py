from typing import List


class Solution:
    def uniquePathsWithObstacles(
        self, obstacleGrid: List[List[int]]
    ) -> int:
        rows = len(obstacleGrid)
        columns = len(obstacleGrid[0])
        # dp[column] counts paths reaching the current row at that column.
        paths = [0] * columns
        paths[0] = 1
        # This base path is cleared if the starting cell contains an obstacle.
        # Row-major order lets each state combine above and current-row left paths.
        for row in range(rows):
            for column in range(columns):
                # An obstacle blocks every route through this cell.
                if obstacleGrid[row][column] == 1:
                    paths[column] = 0
                elif column > 0:
                    # Keep the above count and add the updated left count.
                    paths[column] += paths[column - 1]
                # The start's initial one is retained unless it is blocked.
            # After each row, entries describe paths through all processed cells.
        # The destination count is zero when no obstacle-avoiding route exists.
        return paths[-1]


if __name__ == "__main__":
    solution = Solution()
    assert solution.uniquePathsWithObstacles(
        [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
    ) == 2
    assert solution.uniquePathsWithObstacles([[0, 1], [0, 0]]) == 1
    assert solution.uniquePathsWithObstacles([[1]]) == 0
    assert solution.uniquePathsWithObstacles([[0]]) == 1
    assert solution.uniquePathsWithObstacles([[0, 0], [0, 1]]) == 0
    print("All tests passed")
