from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        # Preserve original first-row and first-column zero state before using them as markers.
        rows, cols = len(matrix), len(matrix[0])
        first_row = any(matrix[0][c] == 0 for c in range(cols))
        first_col = any(matrix[r][0] == 0 for r in range(rows))
        # The first row and column serve as in-place flags for the interior.
        # Separate flags preserve zeros that would otherwise be overwritten as markers.
        for r in range(1, rows):
            for c in range(1, cols):
                # Marker writes happen only in the interior, avoiding loss of saved flags.
                if matrix[r][c] == 0:
                    matrix[r][0] = matrix[0][c] = 0
        for r in range(1, rows):
            for c in range(1, cols):
                # Marker zeroes encode original zero rows and columns.
                if matrix[r][0] == 0 or matrix[0][c] == 0:
                    matrix[r][c] = 0
        # Defer these boundary writes until all interior marker reads are finished.
        if first_row:
            # Apply the saved row flag after marker lookups are complete.
            for c in range(cols):
                matrix[0][c] = 0
        if first_col:
            # Clearing the first column last cannot erase markers needed above.
            for r in range(rows):
                matrix[r][0] = 0


if __name__ == "__main__":
    solution = Solution()
    a = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
    assert solution.setZeroes(a) is None and a == [[1, 0, 1], [0, 0, 0], [1, 0, 1]]
    b = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]
    solution.setZeroes(b)
    assert b == [[0, 0, 0, 0], [0, 4, 5, 0], [0, 3, 1, 0]]
    c = [[0]]
    solution.setZeroes(c)
    assert c == [[0]]
    print("All tests passed")
