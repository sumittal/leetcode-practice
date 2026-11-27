"""
LeetCode 251: Flatten 2D Vector
Difficulty: Medium
Pattern: Array
Video Reference: https://www.youtube.com/results?search_query=leetcode+251+Flatten+2D+Vector+neetcode
Complexity:
    - Time: next O(1) amortized, hasNext O(1) amortized
    - Space: O(number of rows)
"""

from typing import Any, Iterator, List


class Vector2D:
    # Rows are consumed lazily, so no flattened copy of all values is needed.
    # A one-value buffer makes repeated hasNext calls non-consuming.
    # Empty rows advance until the next value or the end of the outer iterator.
    # next removes the buffered value while keeping traversal row-major.
    def __init__(self, vec: List[List[int]]):
        # Separate iterators make empty rows cheap to skip.
        self.rows: Iterator[List[int]] = iter(vec)
        self.current: Iterator[int] = iter([])

    def hasNext(self) -> bool:
        if hasattr(self, "buffered"):
            # A successful prior probe leaves its value ready for next().
            return True
        while True:
            try:
                value = next(self.current)
                self.buffered = value
                return True
            except StopIteration:
                try:
                    # Exhausted and empty rows advance until a value or end appears.
                    self.current = iter(next(self.rows))
                except StopIteration:
                    return False

    def next(self) -> int:
        if not self.hasNext():
            raise StopIteration
        value = self.buffered
        del self.buffered
        # Clearing the buffer lets the next probe advance exactly once.
        return value


def replay(ops: List[str], args: List[List[Any]]) -> List[Any]:
    outputs: List[Any] = []
    vector = None
    for operation, values in zip(ops, args):
        if operation == "Vector2D":
            vector = Vector2D(*values)
            outputs.append(None)
        else:
            outputs.append(getattr(vector, operation)(*values))
    return outputs


if __name__ == "__main__":
    assert replay(
        ["Vector2D", "hasNext", "next", "next", "next", "next", "next",
         "next", "hasNext"],
        [[[[1, 2], [3], [4, 5, 6]]], [], [], [], [], [], [], [], []],
    ) == [None, True, 1, 2, 3, 4, 5, 6, False]
    assert replay(
        ["Vector2D", "hasNext", "next", "next", "next", "hasNext"],
        [[[[], [7], [], [8, 9]]], [], [], [], [], []],
    ) == [None, True, 7, 8, 9, False]
    print("All tests passed")
