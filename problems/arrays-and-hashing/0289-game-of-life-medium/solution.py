"""
LeetCode 289: Game of Life
Difficulty: Medium
Pattern: Array
Video Reference: https://www.youtube.com/results?search_query=leetcode+289+Game+of+Life+neetcode
Complexity:
    - Time: O(mn)
    - Space: O(1)
"""

from typing import List


class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        rows = len(board)
        columns = len(board[0]) if rows else 0
        # Each neighbor coordinate is bounded before it is read.
        # The low bit preserves each cell's original generation during updates.
        for row in range(rows):
            for column in range(columns):
                live_neighbors = 0
                # Count neighbors from their low bits, never their new-state bits.
                for row_delta in (-1, 0, 1):
                    for column_delta in (-1, 0, 1):
                        if row_delta == 0 and column_delta == 0:
                            continue
                        neighbor_row = row + row_delta
                        neighbor_column = column + column_delta
                        if 0 <= neighbor_row < rows and 0 <= neighbor_column < columns:
                            live_neighbors += board[neighbor_row][neighbor_column] & 1
                was_alive = board[row][column] & 1
                # Set the high bit when the next generation is alive.
                # The high bit stores new state without disturbing old-state reads.
                if live_neighbors == 3 or (was_alive and live_neighbors == 2):
                    board[row][column] |= 2
                # All decisions use the unchanged original-state low bits.
        # Shifting discards old states and commits the next generation in place.
        for row in range(rows):
            for column in range(columns):
                board[row][column] >>= 1
        # The operation intentionally returns no replacement board.
        # Two bits per cell are enough to encode both generations temporarily.


if __name__ == "__main__":
    solution = Solution()
    board = [[0, 1, 0], [0, 0, 1], [1, 1, 1], [0, 0, 0]]
    solution.gameOfLife(board)
    assert board == [[0, 0, 0], [1, 0, 1], [0, 1, 1], [0, 1, 0]]
    board = [[1]]
    solution.gameOfLife(board)
    assert board == [[0]]
    board = [[1, 1], [1, 0]]
    solution.gameOfLife(board)
    assert board == [[1, 1], [1, 1]]
    print("All tests passed")
