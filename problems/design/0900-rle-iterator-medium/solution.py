"""
LeetCode 900: RLE Iterator
Difficulty: Medium
Pattern: Array
Video Reference: https://www.youtube.com/results?search_query=leetcode+900+RLE+Iterator+neetcode
Complexity:
    - Time: next O(number of runs crossed), construction O(1)
    - Space: O(1)
"""

from typing import List


class RLEIterator:
    def __init__(self, encoding: List[int]):
        # Counts and values stay paired; no expanded representation is built.
        self.encoding = encoding
        # The index always points to the count slot of the current run.
        self.index = 0

    def next(self, n: int) -> int:
        # Consume complete runs until the requested final item is reached.
        while self.index < len(self.encoding) and n > self.encoding[self.index]:
            # A complete run can be skipped by subtracting its remaining count.
            n -= self.encoding[self.index]
            self.index += 2
        # Exhaustion is detected only after all traversed run counts are spent.
        if self.index >= len(self.encoding):
            return -1
        # Equality consumes the final item of this run without advancing yet.
        # The current count is reduced in place for subsequent operations.
        self.encoding[self.index] -= n
        # Mutating the count makes subsequent calls resume at the right offset.
        return self.encoding[self.index + 1]


def replay(ops: List[str], args: List[list]) -> List[object]:
    outputs: List[object] = []
    iterator = None
    for op, values in zip(ops, args):
        if op == "RLEIterator":
            iterator = RLEIterator(*values)
            outputs.append(None)
        else:
            outputs.append(getattr(iterator, op)(*values))
    return outputs


if __name__ == "__main__":
    assert replay(
        ["RLEIterator", "next", "next", "next", "next"],
        [[[3, 8, 0, 9, 2, 5]], [2], [1], [1], [2]],
    ) == [None, 8, 8, 5, -1]
    assert replay(
        ["RLEIterator", "next", "next"],
        [[[1, 7]], [1], [1]],
    ) == [None, 7, -1]
    print("All tests passed")
