from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        # The square matrix has the same row and column count.
        n = len(matrix)
        # Transposition sends each coordinate (row, column) to (column, row).
        # The diagonal stays fixed because rotating it maps each cell to itself.
        # Restrict transpose pairs to one triangle so each off-diagonal pair swaps once.
        # The diagonal needs no write because its row and column are identical.
        for r in range(n):
            for c in range(r + 1, n):
                matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]  # Transpose.
        # The transpose swaps axes; row reversal moves columns into rotated positions.
        for row in matrix:
            row.reverse()  # Reversing each transposed row yields a clockwise rotation.


if __name__ == "__main__":
    solution = Solution()
    a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    assert solution.rotate(a) is None and a == [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
    b = [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]
    solution.rotate(b)
    assert b == [[15, 13, 2, 5], [14, 3, 4, 1], [12, 6, 8, 9], [16, 7, 10, 11]]
    c = [[1]]
    solution.rotate(c)
    assert c == [[1]]
    print("All tests passed")
