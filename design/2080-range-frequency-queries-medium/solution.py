"""
LeetCode 2080: Range Frequency Queries
Difficulty: Medium
Pattern: Array
Video Reference: https://www.youtube.com/results?search_query=leetcode+2080+Range+Frequency+Queries+neetcode
Complexity:
    - Time: construction O(n), query O(log n)
    - Space: O(n)
"""

from bisect import bisect_left, bisect_right
from typing import Dict, List


class RangeFreqQuery:
    # Value-to-index lists make each inclusive frequency query logarithmic.
    # The constructor builds all lists in one pass through the input.
    def __init__(self, arr: List[int]):
        self.positions: Dict[int, List[int]] = {}
        # A single pass builds sorted occurrence lists for every value.
        # Appending indices preserves the order required by binary search.
        for index, value in enumerate(arr):
            self.positions.setdefault(value, []).append(index)
        # Each dictionary value is a strictly increasing position sequence.

    def query(self, left: int, right: int, value: int) -> int:
        # Missing values use an empty list, which yields a zero difference.
        positions = self.positions.get(value, [])
        # Lower/upper bounds implement the inclusive [left, right] range.
        # Their difference counts exactly the positions between both endpoints.
        return bisect_right(positions, right) - bisect_left(positions, left)


def replay(ops: List[str], args: List[list]) -> List[object]:
    outputs: List[object] = []
    ranges = None
    for op, values in zip(ops, args):
        if op == "RangeFreqQuery":
            ranges = RangeFreqQuery(*values)
            outputs.append(None)
        else:
            outputs.append(getattr(ranges, op)(*values))
    return outputs


if __name__ == "__main__":
    assert replay(
        ["RangeFreqQuery", "query", "query", "query"],
        [[[12, 33, 4, 56, 22, 2, 34, 33, 22, 12, 34, 56]],
         [1, 2, 4], [0, 11, 33], [0, 3, 99]],
    ) == [None, 1, 2, 0]
    print("All tests passed")
