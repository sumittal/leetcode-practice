"""
LeetCode 1046: Last Stone Weight
Difficulty: Easy
Pattern: Heap / Priority Queue
Video Reference: https://www.youtube.com/watch?v=B-QCq79-Vfw
Complexity:
    - Time: O(n log n)
    - Space: O(n)
"""

import heapq
from typing import List


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # Negation makes Python's min-heap expose the heaviest remaining stone.
        heaviest = [-stone for stone in stones]
        heapq.heapify(heaviest)
        # Heap construction happens once; each collision then removes its two roots.
        while len(heaviest) > 1:
            # Remove both largest stones before deciding whether a fragment remains.
            first = -heapq.heappop(heaviest)
            second = -heapq.heappop(heaviest)
            if first != second:
                # Only the positive difference survives a collision.
                heapq.heappush(heaviest, -(first - second))
            # Equal weights vanish together and add no replacement to the heap.
            # Each pass shrinks the heap by at least one, guaranteeing termination.
            # The heap always represents the complete multiset of surviving stones.
        # An empty heap represents a final weight of zero.
        return -heaviest[0] if heaviest else 0


if __name__ == "__main__":
    solution = Solution()
    assert solution.lastStoneWeight([2, 7, 4, 1, 8, 1]) == 1
    assert solution.lastStoneWeight([1]) == 1
    assert solution.lastStoneWeight([2, 2]) == 0
    assert solution.lastStoneWeight([]) == 0
    assert solution.lastStoneWeight([10, 4, 2]) == 4
    print("All tests passed")
