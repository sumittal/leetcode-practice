"""
LeetCode 308: Range Sum Query 2D - Mutable
Difficulty: Medium
Pattern: Array
Video Reference: https://www.youtube.com/results?search_query=leetcode+308+Range+Sum+Query+2D+-+Mutable+neetcode
Complexity:
    - Time: update O(log rows * log columns), sumRegion O(log rows * log columns)
    - Space: O(rows * columns)
"""

from typing import List


class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        self.rows = len(matrix)
        self.cols = len(matrix[0]) if matrix else 0
        self.values = [row[:] for row in matrix]
        # One-based tree coordinates make low-bit increments straightforward.
        # Fenwick cells store aggregated deltas over low-bit regions.
        self.tree = [[0] * (self.cols + 1) for _ in range(self.rows + 1)]
        for row in range(self.rows):
            for col in range(self.cols):
                self._add(row, col, self.values[row][col])

    def _add(self, row: int, col: int, delta: int) -> None:
        r = row + 1
        # Each loop visits Fenwick blocks containing the updated cell.
        while r <= self.rows:
            c = col + 1
            while c <= self.cols:
                self.tree[r][c] += delta
                c += c & -c
            r += r & -r

    def update(self, row: int, col: int, val: int) -> None:
        # Convert replacement into a point delta for the Fenwick tree.
        delta = val - self.values[row][col]
        # The cached matrix is needed to compute the replacement delta.
        self.values[row][col] = val
        self._add(row, col, delta)

    def _prefix(self, row: int, col: int) -> int:
        total = 0
        # Descending low bits partitions the rectangle into disjoint blocks.
        r = row + 1
        while r > 0:
            c = col + 1
            while c > 0:
                total += self.tree[r][c]
                c -= c & -c
            r -= r & -r
        return total

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        # Inclusion-exclusion combines four 2D prefix totals.
        total = self._prefix(row2, col2)
        # Subtract strips above and left, then restore their intersection.
        if row1:
            total -= self._prefix(row1 - 1, col2)
        if col1:
            total -= self._prefix(row2, col1 - 1)
        if row1 and col1:
            total += self._prefix(row1 - 1, col1 - 1)
        return total


def replay(ops: List[str], args: List[list]) -> List[object]:
    outputs: List[object] = []
    matrix = None
    for op, values in zip(ops, args):
        if op == "NumMatrix":
            matrix = NumMatrix(*values)
            outputs.append(None)
        else:
            outputs.append(getattr(matrix, op)(*values))
    return outputs


if __name__ == "__main__":
    assert replay(
        ["NumMatrix", "sumRegion", "update", "sumRegion"],
        [[[[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5],
           [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]]], [2, 1, 4, 3],
         [3, 2, 2], [2, 1, 4, 3]],
    ) == [None, 8, None, 10]
    print("All tests passed")
