"""
LeetCode 703: Kth Largest Element in a Stream
Difficulty: Easy
Pattern: Heap / Priority Queue
Video Reference: https://www.youtube.com/watch?v=hOjcdrqMoQ8
Complexity:
    - Time: O(log k) per add after initialization
    - Space: O(k)
"""

import heapq
from typing import List


class KthLargest:
    def __init__(self, k: int, nums: List[int]) -> None:
        self.k = k
        # Keep only the largest k values; the smallest of them is the answer.
        self.values = nums[:]
        heapq.heapify(self.values)
        # Trimming at construction keeps later adds bounded by the same k entries.
        while len(self.values) > self.k:
            heapq.heappop(self.values)
        # Heap order makes index zero the minimum among all retained values.

    def add(self, val: int) -> int:
        # New values may enter the top k, so insert before checking the size.
        heapq.heappush(self.values, val)
        # Push preserves heap order even when the value is smaller than the root.
        if len(self.values) > self.k:
            # Removing the root discards the smallest value outside the top k.
            heapq.heappop(self.values)
        # The problem guarantees enough values for the kth-largest query.
        # With k retained elements, their minimum has exactly k-1 values above it.
        return self.values[0]


if __name__ == "__main__":
    kth_largest = KthLargest(3, [4, 5, 8, 2])
    assert kth_largest.add(3) == 4
    assert kth_largest.add(5) == 5
    assert kth_largest.add(10) == 5
    assert kth_largest.add(9) == 8
    assert kth_largest.add(4) == 8
    kth_largest = KthLargest(1, [])
    assert kth_largest.add(-3) == -3
    assert kth_largest.add(2) == 2
    assert kth_largest.add(-4) == 2
    print("All tests passed")
