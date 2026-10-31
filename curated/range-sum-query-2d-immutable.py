from typing import List


class NumMatrix:
    # The prefix grid stores sums for rectangles anchored at the origin.
    # Four lookups isolate any requested axis-aligned rectangle.
    # Preprocessing visits every cell once; later queries do constant work.
    # A zero border makes edge-touching queries use the same formula.
    def __init__(self, matrix: List[List[int]]):
        rows = len(matrix)
        columns = len(matrix[0]) if rows else 0
        # Padding makes every prefix query safe at row or column zero.
        self.prefix: List[List[int]] = [
            [0] * (columns + 1) for _ in range(rows + 1)
        ]
        for row in range(1, rows + 1):
            for column in range(1, columns + 1):
                # Building row-major ensures the top and left prefixes already exist.
                # Each prefix includes the cell plus two strips minus overlap.
                self.prefix[row][column] = (
                    matrix[row - 1][column - 1]
                    + self.prefix[row - 1][column]
                    + self.prefix[row][column - 1]
                    - self.prefix[row - 1][column - 1]
                )

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        # Inclusion-exclusion removes the two outside strips and restores overlap.
        return (
            self.prefix[row2 + 1][col2 + 1]
            - self.prefix[row1][col2 + 1]
            - self.prefix[row2 + 1][col1]
            + self.prefix[row1][col1]
        )


def replay(ops: List[str], args: List[list]) -> List[object]:
    outputs = []
    matrix = None
    for operation, values in zip(ops, args):
        if operation == "NumMatrix":
            matrix = NumMatrix(*values)
            outputs.append(None)
        else:
            outputs.append(getattr(matrix, operation)(*values))
    return outputs


if __name__ == "__main__":
    assert replay(
        ["NumMatrix", "sumRegion", "sumRegion", "sumRegion"],
        [[[[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5],
           [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]]],
         [2, 1, 4, 3], [1, 1, 2, 2], [1, 2, 2, 4]],
    ) == [None, 8, 11, 12]
    assert replay(
        ["NumMatrix", "sumRegion"],
        [[[[5]]], [0, 0, 0, 0]],
    ) == [None, 5]
    print("All tests passed")
