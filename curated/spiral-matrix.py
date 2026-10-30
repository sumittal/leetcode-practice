from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # Empty dimensions have no boundary to peel.
        if not matrix or not matrix[0]:
            return []
        top, bottom, left, right = 0, len(matrix) - 1, 0, len(matrix[0]) - 1
        # After each side is emitted, its bound advances so cells are never repeated.
        # Inclusive boundaries shrink inward as their corresponding side is emitted.
        result = []
        # The loop condition keeps scanning only while an unvisited rectangle remains.
        while top <= bottom and left <= right:
            # A complete boundary pass removes at least one row and one column.
            # Each pass consumes the current top, right, bottom, then left boundary.
            result.extend(matrix[top][left : right + 1])
            top += 1
            for r in range(top, bottom + 1):
                result.append(matrix[r][right])
            right -= 1
            if top <= bottom:  # Remaining rows guard against duplicating a single row.
                result.extend(matrix[bottom][left : right + 1][::-1])
                bottom -= 1
            if (
                left <= right
            ):  # Remaining columns guard against duplicating a single column.
                for r in range(bottom, top - 1, -1):
                    result.append(matrix[r][left])
                left += 1
        return result


if __name__ == "__main__":
    solution = Solution()
    assert solution.spiralOrder([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == [
        1,
        2,
        3,
        6,
        9,
        8,
        7,
        4,
        5,
    ]
    assert solution.spiralOrder([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]) == [
        1,
        2,
        3,
        4,
        8,
        12,
        11,
        10,
        9,
        5,
        6,
        7,
    ]
    assert solution.spiralOrder([[1, 2, 3]]) == [1, 2, 3]
    assert solution.spiralOrder([[1], [2], [3]]) == [1, 2, 3]
    print("All tests passed")
