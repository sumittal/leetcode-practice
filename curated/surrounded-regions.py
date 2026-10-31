from collections import deque
from typing import Deque, List, Tuple


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        if not board or not board[0]:
            return
        # Temporary S marks are safe cells and are restored after all flips.
        rows = len(board)
        columns = len(board[0])
        safe: Deque[Tuple[int, int]] = deque()
        # Border O cells are the only possible seeds for uncaptured regions.
        # The two passes cover corners as well as each edge's interior cells.
        for row in range(rows):
            for column in (0, columns - 1):
                if board[row][column] == "O":
                    board[row][column] = "S"
                    safe.append((row, column))
        for column in range(columns):
            for row in (0, rows - 1):
                if board[row][column] == "O":
                    board[row][column] = "S"
                    safe.append((row, column))
        # Multi-source traversal marks every O connected to any border seed.
        while safe:
            row, column = safe.popleft()
            # Queue removal gives every safe cell its turn to inspect all neighbors.
            for next_row, next_column in (
                (row + 1, column),
                (row - 1, column),
                (row, column + 1),
                (row, column - 1),
            ):
                if (
                    0 <= next_row < rows
                    and 0 <= next_column < columns
                    and board[next_row][next_column] == "O"
                ):
                    # Mark at discovery time so the cell enters the queue once.
                    board[next_row][next_column] = "S"
                    safe.append((next_row, next_column))
        # Safe markers return to O; remaining O cells are enclosed and become X.
        # This final pass both restores safe cells and captures the unmarked interior.
        for row in range(rows):
            for column in range(columns):
                if board[row][column] == "S":
                    board[row][column] = "O"
                elif board[row][column] == "O":
                    board[row][column] = "X"


if __name__ == "__main__":
    solution = Solution()
    board = [
        list("XXXX"),
        list("XOOX"),
        list("XXOX"),
        list("XOXX"),
    ]
    assert solution.solve(board) is None
    assert board == [
        list("XXXX"),
        list("XXXX"),
        list("XXXX"),
        list("XOXX"),
    ]
    single_cell = [["X"]]
    solution.solve(single_cell)
    assert single_cell == [["X"]]
    border_region = [list("OOO"), list("OXO"), list("OOO")]
    solution.solve(border_region)
    assert border_region == [list("OOO"), list("OXO"), list("OOO")]
    print("All tests passed")
