"""
LeetCode 1476: Subrectangle Queries
Difficulty: Medium
Pattern: Array
Video Reference: https://www.youtube.com/results?search_query=leetcode+1476+Subrectangle+Queries+neetcode
Complexity:
    - Time: update O(1), getValue O(number of updates)
    - Space: O(rows * columns + updates)
"""

from typing import List, Tuple


class SubrectangleQueries:
    # Reverse update lookup makes the newest covering rectangle authoritative.
    # The baseline matrix is copied so the caller cannot mutate stored state.
    # This lazy strategy is efficient when updates are frequent and reads limited.
    def __init__(self, rectangle: List[List[int]]):
        # Preserve an immutable baseline and store only subsequent updates.
        self.rectangle = [row[:] for row in rectangle]
        # Updates are kept in call order to resolve overlapping rectangles.
        self.updates: List[Tuple[int, int, int, int, int]] = []

    def updateSubrectangle(
        self, row1: int, col1: int, row2: int, col2: int, newValue: int
    ) -> None:
        # Recording a rectangle is constant time regardless of its area.
        self.updates.append((row1, col1, row2, col2, newValue))

    def getValue(self, row: int, col: int) -> int:
        # Later updates override earlier ones, so search newest-first.
        for row1, col1, row2, col2, value in reversed(self.updates):
            # The first containing update is the latest write to this cell.
            if row1 <= row <= row2 and col1 <= col <= col2:
                return value
        return self.rectangle[row][col]


def replay(ops: List[str], args: List[list]) -> List[object]:
    outputs: List[object] = []
    queries = None
    for op, values in zip(ops, args):
        if op == "SubrectangleQueries":
            queries = SubrectangleQueries(*values)
            outputs.append(None)
        else:
            outputs.append(getattr(queries, op)(*values))
    return outputs


if __name__ == "__main__":
    assert replay(
        ["SubrectangleQueries", "getValue", "updateSubrectangle", "getValue",
         "getValue", "updateSubrectangle", "getValue", "getValue"],
        [[[[1, 2, 1], [4, 3, 4], [3, 2, 1], [1, 1, 1]]], [0, 2],
         [0, 0, 3, 2, 5], [0, 2], [3, 1], [3, 0, 3, 2, 10], [3, 1],
         [0, 1]],
    ) == [None, 1, None, 5, 5, None, 10, 5]
    print("All tests passed")
