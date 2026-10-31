from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        columns = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        # Separate sets keep a digit in one region from affecting another region.
        # The same board cell contributes to exactly one row, one column, and one box.
        # Each filled cell must be unique in all three Sudoku regions.
        for row in range(9):
            for column in range(9):
                digit = board[row][column]
                if digit == ".":
                    # Blank cells impose no constraint until a digit is placed.
                    continue
                # Integer division maps every 3-by-3 square to one box index.
                box = (row // 3) * 3 + column // 3
                # A duplicate in any region invalidates the partial board.
                if (
                    digit in rows[row]
                    or digit in columns[column]
                    or digit in boxes[box]
                ):
                    return False
                # Record the digit in every region so later cells see it.
                rows[row].add(digit)
                columns[column].add(digit)
                boxes[box].add(digit)
        # All filled cells passed their row, column, and box constraints.
        return True


if __name__ == "__main__":
    solution = Solution()
    valid_board = [
        ["5", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"],
    ]
    invalid_board = [
        ["8", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"],
    ]
    assert solution.isValidSudoku(valid_board) is True
    assert solution.isValidSudoku(invalid_board) is False
    assert solution.isValidSudoku([["."] * 9 for _ in range(9)]) is True
    duplicate_box = [row[:] for row in valid_board]
    duplicate_box[1][1] = "5"
    assert solution.isValidSudoku(duplicate_box) is False
    print("All tests passed")
