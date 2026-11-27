"""
LeetCode 1157: Online Majority Element In Subarray
Difficulty: Hard
Pattern: Array
Video Reference: https://www.youtube.com/results?search_query=leetcode+1157+Online+Majority+Element+In+Subarray+neetcode
Complexity:
    - Time: construction O(n), query O(log n)
    - Space: O(n)
"""

from bisect import bisect_left, bisect_right
from typing import Dict, List, Tuple


class MajorityChecker:
    def __init__(self, arr: List[int]):
        # A power-of-two base supports an iterative range-summary tree.
        self.length = len(arr)
        self.size = 1
        while self.size < self.length:
            self.size *= 2
        # Segment entries hold a Boyer-Moore candidate and residual balance.
        self.tree: List[Tuple[int, int]] = [(0, 0)] * (2 * self.size)
        self.positions: Dict[int, List[int]] = {}
        for index, value in enumerate(arr):
            self.positions.setdefault(value, []).append(index)
            self.tree[self.size + index] = (value, 1)
        for index in range(self.size - 1, 0, -1):
            # Child summaries combine into a candidate for each parent segment.
            self.tree[index] = self._combine(
                self.tree[2 * index], self.tree[2 * index + 1]
            )

    @staticmethod
    def _combine(
        first: Tuple[int, int], second: Tuple[int, int]
    ) -> Tuple[int, int]:
        # Equal candidates reinforce; different candidates cancel pairwise.
        if first[1] == 0:
            return second
        if second[1] == 0:
            return first
        if first[0] == second[0]:
            return first[0], first[1] + second[1]
        if first[1] > second[1]:
            return first[0], first[1] - second[1]
        return second[0], second[1] - first[1]

    def _candidate(self, left: int, right: int) -> Tuple[int, int]:
        left += self.size
        right += self.size + 1
        before = (0, 0)
        # Empty summaries are neutral elements for the cancellation operation.
        after = (0, 0)
        # Separate accumulators preserve the segment's left-to-right order.
        while left < right:
            if left & 1:
                before = self._combine(before, self.tree[left])
                left += 1
            if right & 1:
                right -= 1
                after = self._combine(self.tree[right], after)
            left //= 2
            right //= 2
        return self._combine(before, after)

    def query(self, left: int, right: int, threshold: int) -> int:
        candidate, _ = self._candidate(left, right)
        # The segment candidate is exact for a strict majority, then verified.
        occurrences = self.positions.get(candidate, [])
        # Since threshold is strictly greater than half, there is at most one.
        count = bisect_right(occurrences, right) - bisect_left(
            occurrences, left
        )
        # Binary-search validation avoids scanning the queried subarray.
        return candidate if count >= threshold else -1


def replay(ops: List[str], args: List[list]) -> List[object]:
    outputs: List[object] = []
    checker = None
    for op, values in zip(ops, args):
        if op == "MajorityChecker":
            checker = MajorityChecker(*values)
            outputs.append(None)
        else:
            outputs.append(getattr(checker, op)(*values))
    return outputs


if __name__ == "__main__":
    assert replay(
        ["MajorityChecker", "query", "query", "query"],
        [[[1, 1, 2, 2, 1, 1]], [0, 5, 4], [0, 3, 3], [2, 3, 2]],
    ) == [None, 1, -1, 2]
    assert replay(
        ["MajorityChecker", "query", "query"],
        [[[2, 2, 1, 1, 1]], [0, 4, 3], [0, 1, 2]],
    ) == [None, 1, 2]
    print("All tests passed")
