"""
LeetCode 909: Snakes and Ladders
Difficulty: Medium
Pattern: Graphs
Video Reference: https://www.youtube.com/watch?v=6lH4nO3JfLk
Complexity:
    - Time: O(n^2)
    - Space: O(n^2)
"""

from collections import deque
from typing import List


class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        # Board dimensions determine both the destination and roll boundaries.
        size = len(board)
        destination = size * size
        # Convert square numbering into its alternating row and column.

        def cell(square: int) -> int:
            row_from_bottom, offset = divmod(square - 1, size)
            row = size - row_from_bottom - 1
            if row_from_bottom % 2 == 0:
                column = offset
            else:
                column = size - offset - 1
            return board[row][column]

        # BFS distance is the minimum number of dice throws to each square.
        # FIFO order explores every state with fewer rolls before deeper states.
        queue = deque([(1, 0)])
        visited = {1}
        while queue:
            square, moves = queue.popleft()
            # Each throw can reach at most the next six numbered squares.
            for landing in range(square + 1, min(square + 6, destination) + 1):
                jump = cell(landing)
                next_square = landing if jump == -1 else jump
                # A snake or ladder is applied exactly once on this throw.
                if next_square == destination:
                    return moves + 1
                if next_square not in visited:
                    visited.add(next_square)
                    queue.append((next_square, moves + 1))
                # First visit is shortest because the queue is breadth-first.
        # A board may contain jumps that make the destination unreachable.
        return -1


if __name__ == "__main__":
    solution = Solution()
    board = [
        [-1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1],
        [-1, 35, -1, -1, 13, -1],
        [-1, -1, -1, -1, -1, -1],
        [-1, 15, -1, -1, -1, -1],
    ]
    assert solution.snakesAndLadders(board) == 4
    assert solution.snakesAndLadders([[-1, -1], [-1, 3]]) == 1
    assert solution.snakesAndLadders([[-1, -1], [-1, -1]]) == 1
    print("All tests passed")
