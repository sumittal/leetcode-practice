from typing import List, Set


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        result = []
        columns: Set[int] = set()
        descending_diagonals: Set[int] = set()
        ascending_diagonals: Set[int] = set()
        queen_columns = []

        def place(row: int) -> None:
            # A full row assignment is safe because every placement passed all attacks.
            # Row order ensures no separate row-occupancy structure is needed.
            if row == n:
                board = []
                for queen_column in queen_columns:
                    # Exactly one stored column selects the queen in this board row.
                    board_row = "." * queen_column + "Q" + "." * (n - queen_column - 1)
                    board.append(board_row)
                result.append(board)
                return
            for column in range(n):
                descending = row - column
                ascending = row + column
                # Equal row-column differences share one diagonal slope.
                # Column and diagonal sets reject every queen attack in constant time.
                if (
                    column in columns
                    or descending in descending_diagonals
                    or ascending in ascending_diagonals
                ):
                    continue
                # Record all three constraints before descending to the next row.
                columns.add(column)
                descending_diagonals.add(descending)
                ascending_diagonals.add(ascending)
                queen_columns.append(column)
                place(row + 1)
                queen_columns.pop()  # Undo this row's placement after exploring it.
                columns.remove(column)
                descending_diagonals.remove(descending)
                ascending_diagonals.remove(ascending)
                # Clearing all marks makes this column available to sibling branches.
                # Backtracking restores the full constraint state before the next column.
                # Since one queen is fixed per earlier row, row conflicts cannot occur.
            # Exhausting columns proves no remaining safe placement exists in this row.

        # Row-by-row placement guarantees exactly one queen per row.
        place(0)
        return result


if __name__ == "__main__":
    solution = Solution()
    four_queens = solution.solveNQueens(4)
    assert sorted(tuple(board) for board in four_queens) == sorted(
        [
            (".Q..", "...Q", "Q...", "..Q."),
            ("..Q.", "Q...", "...Q", ".Q.."),
        ]
    )
    assert solution.solveNQueens(1) == [["Q"]]
    assert solution.solveNQueens(2) == []
    assert solution.solveNQueens(3) == []
    print("All tests passed")
