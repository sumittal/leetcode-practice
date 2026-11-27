"""
LeetCode 994: Rotting Oranges
Difficulty: Medium
Pattern: Graphs
Video Reference: https://www.youtube.com/watch?v=y704fEOx0s0
Complexity:
    - Time: O(mn)
    - Space: O(mn)
"""

from collections import deque
from typing import Deque, List, Tuple


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0
        rows = len(grid)
        columns = len(grid[0])
        rotten: Deque[Tuple[int, int]] = deque()
        fresh = 0
        # Counting fresh cells lets BFS stop as soon as all have changed state.
        # Seed all existing rot sources so they spread in the same time layers.
        for row in range(rows):
            for column in range(columns):
                if grid[row][column] == 2:
                    rotten.append((row, column))
                elif grid[row][column] == 1:
                    fresh += 1
        minutes = 0
        while rotten and fresh:
            # One fixed queue layer represents one minute of simultaneous spread.
            # Newly rotten oranges are appended but excluded from this saved layer size.
            layer_size = len(rotten)
            for _ in range(layer_size):
                row, column = rotten.popleft()
                for next_row, next_column in (
                    (row + 1, column),
                    (row - 1, column),
                    (row, column + 1),
                    (row, column - 1),
                ):
                    if (
                        0 <= next_row < rows
                        and 0 <= next_column < columns
                        and grid[next_row][next_column] == 1
                    ):
                        # Mark immediately so the orange is counted as rotten once.
                        grid[next_row][next_column] = 2
                        fresh -= 1
                        rotten.append((next_row, next_column))
            # Each successful neighbor transition reduces fresh by exactly one.
            # Advancing after the whole layer counts simultaneous rot as one minute.
            minutes += 1
        # Remaining fresh fruit is isolated from every initial rot source.
        return minutes if fresh == 0 else -1


if __name__ == "__main__":
    solution = Solution()
    first = [[2, 1, 1], [1, 1, 0], [0, 1, 1]]
    second = [[2, 1, 1], [0, 1, 1], [1, 0, 1]]
    assert solution.orangesRotting(first) == 4
    assert solution.orangesRotting(second) == -1
    assert solution.orangesRotting([[0, 2]]) == 0
    assert solution.orangesRotting([[1]]) == -1
    assert solution.orangesRotting([[2]]) == 0
    print("All tests passed")
