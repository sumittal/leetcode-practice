"""
LeetCode 846: Hand of Straights
Difficulty: Medium
Pattern: Greedy
Video Reference: https://www.youtube.com/watch?v=amnrMCVd2YI
Complexity:
    - Time: O(n log n)
    - Space: O(n)
"""

import heapq
from collections import Counter
from typing import List


class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize:
            return False
        # Counts preserve duplicate cards while the heap orders distinct group starts.
        counts = Counter(hand)
        # Each distinct value enters the heap once, regardless of its frequency.
        starts = list(counts)
        heapq.heapify(starts)
        while starts:
            start = heapq.heappop(starts)
            if counts[start] == 0:
                # A prior group may already have consumed this distinct value.
                continue
            # Every copy of the smallest remaining card must begin a group.
            repetitions = counts[start]
            for value in range(start, start + groupSize):
                if counts[value] < repetitions:
                    # A missing or under-counted consecutive value makes grouping impossible.
                    return False
                counts[value] -= repetitions
            # Equal repetitions are consumed together to satisfy the smallest-card invariant.
            # Depleted starts are ignored as they reach the heap root.
        # Divisibility and successful consumption imply every card was grouped once.
        # Depleted keys later rise to the root and are skipped without changing counts.
        return True


if __name__ == "__main__":
    solution = Solution()
    assert solution.isNStraightHand([1, 2, 3, 6, 2, 3, 4, 7, 8], 3) is True
    assert solution.isNStraightHand([1, 2, 3, 4, 5], 4) is False
    assert solution.isNStraightHand([1, 1, 2, 2], 2) is True
    assert solution.isNStraightHand([], 3) is True
    print("All tests passed")
