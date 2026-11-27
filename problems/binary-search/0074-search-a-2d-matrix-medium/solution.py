"""
LeetCode 74: Search a 2D Matrix
Difficulty: Medium
Pattern: Binary Search
Video Reference: https://www.youtube.com/watch?v=Ber2pi2C0j0
Complexity:
    - Time: O(log(mn))
    - Space: O(1)
"""

from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        rows = len(matrix)
        columns = len(matrix[0])
        # Row-major ordering turns each coordinate into one sorted linear index.
        left = 0
        right = rows * columns - 1
        # Empty dimensions were returned above before division by column count.
        # The inclusive range contains every matrix cell not ruled out yet.
        while left <= right:
            middle = (left + right) // 2
            row = middle // columns
            column = middle % columns
            # Division and remainder invert the row-major flattening.
            value = matrix[row][column]
            if value == target:
                # Return as soon as the unique matrix position matches.
                return True
            if value < target:
                # Discard all earlier row-major positions, including this midpoint.
                left = middle + 1
            else:
                # Discard all later positions because their values are no smaller.
                right = middle - 1
            # Each comparison removes at least the midpoint from consideration.
        # Exhausting linear indices means no row contains the target.
        return False


if __name__ == "__main__":
    solution = Solution()
    matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
    assert solution.searchMatrix(matrix, 3) is True
    assert solution.searchMatrix(matrix, 13) is False
    assert solution.searchMatrix([[1]], 1) is True
    assert solution.searchMatrix([[1, 3]], 3) is True
    assert solution.searchMatrix([], 0) is False
    print("All tests passed")
