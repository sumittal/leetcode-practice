"""
LeetCode 3242: Design Neighbor Sum Service
Difficulty: Easy
Pattern: Array
Video Reference: https://www.youtube.com/results?search_query=leetcode+3242+Design+Neighbor+Sum+Service+neetcode
Complexity:
    - Time: construction O(n^2), adjacentSum/diagonalSum O(1)
    - Space: O(n^2)
"""

from typing import Dict, List, Optional


class NeighborSum:
    def __init__(self, grid: List[List[int]]):
        self.grid = grid
        self.size = len(grid)
        # Values are unique, so each value has one constant-time coordinate.
        self.position: Dict[int, tuple] = {
            value: (row, column)
            for row, values in enumerate(grid)
            for column, value in enumerate(values)
        }
        # Four orthogonal offsets and four diagonal offsets are kept distinct.
        self.adjacent = ((-1, 0), (1, 0), (0, -1), (0, 1))
        self.diagonal = ((-1, -1), (-1, 1), (1, -1), (1, 1))

    def _sum(self, value: int, directions: tuple) -> int:
        # The value-to-coordinate map avoids searching the grid on each call.
        row, column = self.position[value]
        total = 0
        for row_delta, column_delta in directions:
            neighbor_row = row + row_delta
            neighbor_column = column + column_delta
            if 0 <= neighbor_row < self.size and \
                    0 <= neighbor_column < self.size:
                # Bounds checks exclude locations outside the square grid.
                total += self.grid[neighbor_row][neighbor_column]
        # The fixed direction set makes each query O(1), independent of grid size.
        return total

    def adjacentSum(self, value: int) -> int:
        # Delegate to the shared bounds-checked neighborhood routine.
        # Only the four cardinal neighbors contribute here.
        return self._sum(value, self.adjacent)

    def diagonalSum(self, value: int) -> int:
        # Only the offset set differs from adjacentSum.
        return self._sum(value, self.diagonal)


def replay(ops: List[str], args: List[List[object]]) -> List[Optional[int]]:
    outputs: List[Optional[int]] = []
    service = None
    for operation, values in zip(ops, args):
        if operation == "NeighborSum":
            service = NeighborSum(*values)
            outputs.append(None)
        else:
            outputs.append(getattr(service, operation)(*values))
    return outputs


if __name__ == "__main__":
    assert replay(
        ["NeighborSum", "adjacentSum", "adjacentSum", "diagonalSum",
         "diagonalSum"],
        [[[[0, 1, 2], [3, 4, 5], [6, 7, 8]]], [1], [4], [4], [8]],
    ) == [None, 6, 16, 16, 4]
    assert replay(
        ["NeighborSum", "adjacentSum", "diagonalSum"],
        [[[[1, 2, 0, 3], [4, 7, 15, 6], [8, 9, 10, 11],
           [12, 13, 14, 5]]], [15], [9]],
    ) == [None, 23, 45]
    print("All tests passed")
