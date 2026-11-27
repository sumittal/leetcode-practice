"""
LeetCode 307: Range Sum Query - Mutable
Difficulty: Medium
Pattern: Array
Video Reference: https://www.youtube.com/results?search_query=leetcode+307+Range+Sum+Query+-+Mutable+neetcode
Complexity:
    - Time: update O(log n), sumRange O(log n)
    - Space: O(n)
"""

from typing import List, Optional


class NumArray:
    # Fenwick partial sums support both point deltas and prefix decomposition.
    def __init__(self, nums: List[int]):
        # Keep source values so each update can calculate its exact delta.
        self.values = nums[:]
        self.tree: List[int] = [0] * (len(nums) + 1)
        for index, value in enumerate(nums):
            self._add(index, value)

    def _add(self, index: int, delta: int) -> None:
        position = index + 1
        # Advancing by the low bit visits each containing Fenwick range.
        while position < len(self.tree):
            # Each Fenwick node covers a low-bit-sized suffix of its prefix.
            self.tree[position] += delta
            position += position & -position

    def _prefix(self, index: int) -> int:
        total = 0
        position = index + 1
        # Descending by low bits decomposes the prefix into disjoint blocks.
        while position > 0:
            # Clearing the low bit visits disjoint stored partial sums.
            total += self.tree[position]
            position -= position & -position
        return total

    def update(self, index: int, val: int) -> None:
        delta = val - self.values[index]
        self.values[index] = val
        # Propagate only the changed amount to affected Fenwick ancestors.
        self._add(index, delta)

    def sumRange(self, left: int, right: int) -> int:
        # Inclusive interval total is the difference of adjacent prefixes.
        return self._prefix(right) - self._prefix(left - 1)


def replay(ops: List[str], args: List[list]) -> List[Optional[int]]:
    outputs: List[Optional[int]] = []
    array = None
    for operation, values in zip(ops, args):
        if operation == "NumArray":
            array = NumArray(*values)
            outputs.append(None)
        else:
            outputs.append(getattr(array, operation)(*values))
    return outputs


if __name__ == "__main__":
    assert replay(
        ["NumArray", "sumRange", "update", "sumRange"],
        [[[1, 3, 5]], [0, 2], [1, 2], [0, 2]],
    ) == [None, 9, None, 8]
    assert replay(
        ["NumArray", "update", "sumRange", "update", "sumRange"],
        [[[4]], [0, 4], [0, 0], [0, -2], [0, 0]],
    ) == [None, None, 4, None, -2]
    print("All tests passed")
