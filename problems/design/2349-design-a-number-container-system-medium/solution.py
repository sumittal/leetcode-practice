"""
LeetCode 2349: Design a Number Container System
Difficulty: Medium
Pattern: Hash Table
Video Reference: https://www.youtube.com/results?search_query=leetcode+2349+Design+a+Number+Container+System+neetcode
Complexity:
    - Time: change O(log n), find O(log n) amortized
    - Space: O(n)
"""

import heapq
from collections import defaultdict
from typing import DefaultDict, Dict, List, Optional


class NumberContainers:
    def __init__(self):
        # This map is authoritative; per-number heaps are candidate indexes.
        self.number_at: Dict[int, int] = {}
        # A heap is created on demand for each number requested by change().
        self.indices: DefaultDict[int, List[int]] = defaultdict(list)

    def change(self, index: int, number: int) -> None:
        # Overwrite the authoritative assignment before adding its new candidate.
        self.number_at[index] = number
        # Old heaps are left intact; find validates candidates against this map.
        heapq.heappush(self.indices[number], index)
        # Repeated assignment is harmless; stale duplicate candidates validate.

    def find(self, number: int) -> int:
        # Amortized cost is logarithmic because each stale candidate is popped once.
        heap = self.indices[number]
        # Each stale index is popped only once across all future queries.
        while heap and self.number_at.get(heap[0]) != number:
            heapq.heappop(heap)
        # A valid heap top is the smallest index currently assigned this number.
        return heap[0] if heap else -1


def replay(ops: List[str], args: List[List[int]]) -> List[Optional[int]]:
    outputs: List[Optional[int]] = []
    containers = None
    for operation, values in zip(ops, args):
        if operation == "NumberContainers":
            containers = NumberContainers()
            outputs.append(None)
        else:
            outputs.append(getattr(containers, operation)(*values))
    return outputs


if __name__ == "__main__":
    assert replay(
        ["NumberContainers", "find", "change", "change", "change", "change",
         "find", "change", "find"],
        [[], [10], [2, 10], [1, 10], [3, 10], [5, 10], [10], [1, 20],
         [10]],
    ) == [None, -1, None, None, None, None, 1, None, 2]
    assert replay(
        ["NumberContainers", "change", "change", "change", "find", "change",
         "find"],
        [[], [4, 8], [2, 8], [2, 8], [8], [4, 9], [8]],
    ) == [None, None, None, None, 2, None, 2]
    print("All tests passed")
