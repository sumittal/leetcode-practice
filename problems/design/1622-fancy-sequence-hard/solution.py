"""
LeetCode 1622: Fancy Sequence
Difficulty: Hard
Pattern: Math
Video Reference: https://www.youtube.com/results?search_query=leetcode+1622+Fancy+Sequence+neetcode
Complexity:
    - Time: append O(log MOD), addAll O(1), multAll O(1), getIndex O(1)
    - Space: O(n)
"""

from typing import List


class Fancy:
    MOD = 10 ** 9 + 7

    def __init__(self):
        # Every active element follows one shared affine transformation.
        self.values: List[int] = []
        self.multiplier = 1
        self.offset = 0
        self.zero_boundary = 0

    def append(self, val: int) -> None:
        # Invert the current affine transform to store a stable base value.
        inverse = pow(self.multiplier, self.MOD - 2, self.MOD)
        # Fermat's theorem gives the inverse because MOD is prime and multiplier nonzero.
        self.values.append((val - self.offset) * inverse % self.MOD)

    def addAll(self, inc: int) -> None:
        # Addition changes only the affine offset shared by active elements.
        self.offset = (self.offset + inc) % self.MOD

    def multAll(self, m: int) -> None:
        if m == 0:
            # Every existing value becomes zero; later operations transform it
            # identically, so earlier entries can share the current offset.
            self.zero_boundary = len(self.values)
            # Appends after this point belong to a fresh normalization epoch.
            self.multiplier = 1
            self.offset = 0
            return
        # Scale both terms of y = multiplier * base + offset.
        self.multiplier = self.multiplier * m % self.MOD
        # Multiplying the offset preserves the affine form for every old value.
        self.offset = self.offset * m % self.MOD

    def getIndex(self, idx: int) -> int:
        if idx >= len(self.values):
            return -1
        if idx < self.zero_boundary:
            # Those entries were zeroed by the latest zero-multiply epoch.
            return self.offset
        # New-epoch values are restored through the current multiplier and offset.
        return (self.values[idx] * self.multiplier + self.offset) % self.MOD


def replay(ops: List[str], args: List[list]) -> List[object]:
    outputs: List[object] = []
    sequence = None
    for op, values in zip(ops, args):
        if op == "Fancy":
            sequence = Fancy()
            outputs.append(None)
        else:
            outputs.append(getattr(sequence, op)(*values))
    return outputs


if __name__ == "__main__":
    assert replay(
        ["Fancy", "append", "addAll", "append", "multAll", "getIndex",
         "addAll", "append", "multAll", "getIndex", "getIndex", "getIndex"],
        [[], [2], [3], [7], [2], [0], [3], [10], [2], [0], [1], [2]],
    ) == [None, None, None, None, None, 10, None, None, None, 26, 34, 20]
    assert replay(
        ["Fancy", "append", "multAll", "addAll", "getIndex", "append",
         "getIndex"],
        [[], [5], [0], [7], [0], [4], [1]],
    ) == [None, None, None, None, 7, None, 4]
    print("All tests passed")
