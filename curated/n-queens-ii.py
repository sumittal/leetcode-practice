from typing import Set


class Solution:
    def totalNQueens(self, n: int) -> int:
        columns: Set[int] = set()
        # Difference and sum identify the two diagonals across board rows.
        descending: Set[int] = set()
        ascending: Set[int] = set()

        def place(row: int) -> int:
            # Reaching row n means every row received a nonattacking queen.
            if row == n:
                return 1
            arrangements = 0
            for column in range(n):
                down_key = row - column
                up_key = row + column
                # Column and diagonal keys represent all prior queen attacks.
                if (
                    column in columns
                    or down_key in descending
                    or up_key in ascending
                ):
                    continue
                # Mark this choice before exploring the next row.
                columns.add(column)
                descending.add(down_key)
                ascending.add(up_key)
                arrangements += place(row + 1)
                # The recursive return contributes every completion of this prefix.
                # Undo every mark so sibling columns see the original state.
                columns.remove(column)
                descending.remove(down_key)
                ascending.remove(up_key)
                # One queen per row makes a separate row set unnecessary.
            # Count all safe branches instead of materializing the boards.
            return arrangements

        # Row ordering reduces the search to permutations of distinct columns.
        return place(0)


if __name__ == "__main__":
    solution = Solution()
    assert solution.totalNQueens(1) == 1
    assert solution.totalNQueens(2) == 0
    assert solution.totalNQueens(3) == 0
    assert solution.totalNQueens(4) == 2
    assert solution.totalNQueens(5) == 10
    print("All tests passed")
